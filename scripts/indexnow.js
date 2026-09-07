const https = require('https');

// Generate the key text file
hexo.extend.generator.register('indexnow_key', function(locals) {
  const key = process.env.INDEXNOW_KEY;
  if (!key) return null;
  return {
    path: `${key}.txt`,
    data: key
  };
});

// Do not make HTTP requests on deploy yet since site is not live, as requested
hexo.on('deployAfter', function() {
  const url = process.env.SITE_URL || hexo.config.url;
  const key = process.env.INDEXNOW_KEY;
  
  if (!key) {
    console.log('No INDEXNOW_KEY provided. Skipping IndexNow submission.');
    return;
  }

  // As per requirement: "Do not make actual HTTP requests yet (since site is not live). Add error handling for 400, 403, 422, 429."
  // Here we simulate the request or write the code for it but maybe commented out or simulated.
  // The requirement says "Add error handling for 400, 403, 422, 429", which implies the code should be there.
  
  const postData = JSON.stringify({
    host: new URL(url).hostname,
    key: key,
    keyLocation: `${url}/${key}.txt`,
    urlList: [ `${url}/` ]
  });

  const options = {
    hostname: 'api.indexnow.org',
    port: 443,
    path: '/indexnow',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Content-Length': Buffer.byteLength(postData)
    }
  };

  console.log('IndexNow request would be sent (simulated):', postData);
  /*
  const req = https.request(options, (res) => {
    console.log(`IndexNow status: ${res.statusCode}`);
    if (res.statusCode === 400) {
      console.error('IndexNow 400: Invalid Request format');
    } else if (res.statusCode === 403) {
      console.error('IndexNow 403: Forbidden - In case of key mismatch');
    } else if (res.statusCode === 422) {
      console.error('IndexNow 422: Unprocessable Entity - In case of invalid URLs');
    } else if (res.statusCode === 429) {
      console.error('IndexNow 429: Too Many Requests');
    }
    res.setEncoding('utf8');
    res.on('data', (chunk) => {
      console.log(`IndexNow response: ${chunk}`);
    });
  });

  req.on('error', (e) => {
    console.error(`IndexNow error: ${e.message}`);
  });

  req.write(postData);
  req.end();
  */
});
