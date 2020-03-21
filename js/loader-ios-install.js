/* global gaEvent */
'use strict';

window.addEventListener('load', () => {
  const RE_SAFARI = /safari/i;
  const RE_APPLE_DEVICE = /iphone|ipod|ipad/i;
  const ua = window.navigator.userAgent;
  const supportsStandAlone = 'standalone' in window.navigator;

  if (!supportsStandAlone) {
    return;
  }
  if (navigator.standalone) {
    return;
  }
  if (!RE_SAFARI.test(ua)) {
    return;
  }
  if (!RE_APPLE_DEVICE.test(ua)) {
    return;
  }
  gaEvent('IOSInstall', 'available', null, null, true);

  const scriptElem = document.createElement('script');
  scriptElem.src = '/scripts/ios-install-button.js';
  document.head.append(scriptElem);

  const button = document.createElement('ios-install-button');
  document.querySelector('.bottom-bar-container').prepend(button);
  button.addEventListener('click-install', (e) => {
    gaEvent('IOSInstall', 'banner-shown');
  });
});
