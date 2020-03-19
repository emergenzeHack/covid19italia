self.addEventListener('install', (event) => {
    console.info('service-worker', 'install');
self.skipWaiting();
});

self.addEventListener('activate', (event) => {
    console.info('service-worker', 'activate');
return self.clients.claim();
});

self.addEventListener('fetch', function(e) {
    e.respondWith(fetch(e.request));
});