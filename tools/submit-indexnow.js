const https = require('https');

const key = process.env.INDEXNOW_KEY;
if (!key) {
  console.log('No INDEXNOW_KEY provided. Skipping IndexNow submission.');
  process.exit(0);
}

const siteUrl = 'https://jichangbay.com';
const indexNowEndpoint = 'api.indexnow.org';

const postData = JSON.stringify({
  host: 'jichangbay.com',
  key: key,
  keyLocation: `${siteUrl}/${key}.txt`,
  urlList: [
    `${siteUrl}/`
  ]
});

const options = {
  hostname: indexNowEndpoint,
  path: '/indexnow',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json; charset=utf-8',
    'Content-Length': Buffer.byteLength(postData)
  }
};

const req = https.request(options, (res) => {
  console.log(`IndexNow Submission Status: ${res.statusCode}`);
  
  res.on('data', (d) => {
    process.stdout.write(d);
  });
});

req.on('error', (e) => {
  console.error(`IndexNow submission failed: ${e.message}`);
});

req.write(postData);
req.end();
