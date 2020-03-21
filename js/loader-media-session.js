/* global gaEvent, soundDrownApp */
'use strict';

window.addEventListener('load', () => {
  const supported = ('mediaSession' in navigator);
  if (!supported) {
    console.log('🔈', 'Media Session not available.');
    return;
  }

  const scriptElem = document.createElement('script');
  scriptElem.src = '/scripts/media-session-controller.js';
  document.head.append(scriptElem);
  scriptElem.addEventListener('load', () => {
    const msController = document.createElement('media-session-controller');
    msController.setAttribute('selector', '.sound-container button');
    msController.addEventListener('play', () => {
      gaEvent('MediaSession', 'play');
    });
    msController.addEventListener('pause', () => {
      gaEvent('MediaSession', 'pause');
    });
    soundDrownApp.mediaSessionController = msController;
    document.body.append(msController);
    gaEvent('MediaSession', 'enabled', null, null, true);
  });
});
