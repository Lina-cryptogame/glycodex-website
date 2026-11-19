/* Glycodex – schlankes Zählskript für die eigene Umami-Instanz.
   Meldet nur die aufgerufene Seite und die Domain der Herkunftsseite.
   Keine Cookies, kein Speicher, keine Bildschirm- oder Sprachangaben.
   Bei „Do Not Track“ oder „Global Privacy Control“ wird nichts gesendet. */
(function () {
  'use strict';
  try {
    var n = navigator;
    if (n.doNotTrack === '1' || window.doNotTrack === '1' || n.globalPrivacyControl === true) return;
    if (location.hostname !== 'glycodex.de') return;
    var ref = '';
    try {
      if (document.referrer) {
        var r = new URL(document.referrer);
        if (r.hostname && r.hostname !== location.hostname) ref = r.protocol + '//' + r.hostname;
      }
    } catch (e) {}
    var body = JSON.stringify({
      type: 'event',
      payload: { website: '39ac9af5-8920-4e49-b50c-1ceeb03029c5', hostname: location.hostname, url: location.pathname, referrer: ref }
    });
    fetch('https://stats.glycodex.de/api/send', {
      method: 'POST', keepalive: true, credentials: 'omit',
      headers: { 'Content-Type': 'application/json' }, body: body
    }).catch(function () {});
  } catch (e) {}
})();
