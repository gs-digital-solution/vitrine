// Service Worker minimal
const CACHE_NAME = 'vitrine-v1';
const urlsToCache = [
  '/',
  '/static/css/style.css',
  '/static/manifest.json'
  // Ajoutez ici d'autres fichiers statiques si besoin
];

// Installation
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

// Activation (supprime les anciens caches)
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(key => key !== CACHE_NAME)
            .map(key => caches.delete(key))
      );
    })
  );
});

// Interception des requêtes (stratégie "cache first")
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});