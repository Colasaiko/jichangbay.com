hexo.extend.generator.register('sitemap', function(locals) {
  const lastUpdated = hexo.config.lastUpdated || new Date().toISOString().split('T')[0];
  const url = hexo.config.url.replace(/\/$/, '');
  
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>${url}/</loc>
    <lastmod>${lastUpdated}</lastmod>
  </url>
</urlset>`;

  return {
    path: 'sitemap.xml',
    data: xml
  };
});
