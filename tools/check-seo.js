const fs = require('fs');
const path = require('path');

const publicDir = path.join(__dirname, '../public');
const indexPath = path.join(publicDir, 'index.html');

if (!fs.existsSync(indexPath)) {
  console.error('index.html not found');
  process.exit(1);
}

const html = fs.readFileSync(indexPath, 'utf-8');

// Title
const titleMatch = html.match(/<title>(.*?)<\/title>/);
const title = titleMatch ? titleMatch[1] : '';
const titleLen = Array.from(title).length;

// Description
const descMatch = html.match(/<meta\s+name="description"\s+content="(.*?)">/i);
const desc = descMatch ? descMatch[1] : '';
const descLen = Array.from(desc).length;

// H1
const h1Matches = html.match(/<h1.*?>.*?<\/h1>/gi) || [];

console.log('--- SEO CHECK ---');
console.log(`Title: ${title} (${titleLen} chars)`);
console.log(`Description: ${desc} (${descLen} chars)`);
console.log(`H1 count: ${h1Matches.length}`);

let hasError = false;

if (titleLen < 20 || titleLen > 30) {
  console.error(`ERROR: Title length is ${titleLen} (expected 20-30)`);
  hasError = true;
}
if (descLen < 70 || descLen > 80) {
  console.error(`ERROR: Description length is ${descLen} (expected 70-80)`);
  hasError = true;
}
if (h1Matches.length !== 1) {
  console.error(`ERROR: H1 count is ${h1Matches.length} (expected 1)`);
  hasError = true;
}

if (hasError) {
  process.exit(1);
} else {
  console.log('SEO CHECK PASSED!');
}
