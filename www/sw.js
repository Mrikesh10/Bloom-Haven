const V='bloomhaven-v14';
self.addEventListener('install',()=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{
 const r=e.request;if(r.method!=='GET'||new URL(r.url).origin!==location.origin)return;
 // pages: network first (so updates arrive), fall back to the saved copy when offline
 if(r.mode==='navigate'||/index\.html$/.test(r.url)){e.respondWith(fetch(r).then(x=>{const c=x.clone();caches.open(V).then(ch=>ch.put(r,c));return x}).catch(()=>caches.match(r).then(m=>m||caches.match('index.html'))));return}
 // everything else: instant from the saved copy, refreshed in the background
 e.respondWith(caches.match(r).then(m=>{const net=fetch(r).then(x=>{if(x.ok){const c=x.clone();caches.open(V).then(ch=>ch.put(r,c))}return x}).catch(()=>m);return m||net}));
});
