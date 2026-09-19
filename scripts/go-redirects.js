const yaml = require('js-yaml');
const fs = require('fs');
const path = require('path');

hexo.extend.generator.register('go_redirects', function(locals) {
  const dataPath = path.join(hexo.source_dir, '_data', 'providers.yml');
  if (!fs.existsSync(dataPath)) return [];
  
  const providers = yaml.load(fs.readFileSync(dataPath, 'utf8'));
  if (!providers || !Array.isArray(providers)) return [];
  
  const results = [];
  const slugs = new Set();
  
  providers.forEach(p => {
    if (!p.name) throw new Error('Provider missing name');
    if (!p.slug) throw new Error('Provider missing slug for ' + p.name);
    
    const targetUrl = p.affUrl || p.officialUrl;
    if (!targetUrl) throw new Error('Provider missing affUrl and officialUrl for ' + p.name);
    
    if (slugs.has(p.slug)) throw new Error('Duplicate slug found: ' + p.slug);
    slugs.add(p.slug);
    
    // HTML Escape the name and URL for safe output
    const safeName = p.name.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    const safeUrl = targetUrl.replace(/"/g, '&quot;');
    const jsonUrl = JSON.stringify(targetUrl);
    
    const content = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="robots" content="noindex,nofollow">
  <title>正在前往 ${safeName}</title>
  <meta http-equiv="refresh" content="0; url=${safeUrl}">
  <script>window.location.replace(${jsonUrl});</script>
</head>
<body>
  <p>正在前往 ${safeName} 套餐页面……</p>
  <noscript>
    <p>如果没有自动跳转，请点击<a href="${safeUrl}" rel="nofollow sponsored noopener">继续前往 ${safeName}</a>。</p>
  </noscript>
</body>
</html>`;

    results.push({
      path: `go/${p.slug}/index.html`,
      data: content
    });
  });
  
  return results;
});
