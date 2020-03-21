/* global gaEvent */
'use strict';

// Verify customElements and beforeInstallPromptEvent is supported.
if (('customElements' in window) && ('BeforeInstallPromptEvent' in window)) {
  const button = document.getElementById('butPWAInstall');
  button.addEventListener('pwa-install', (e) => {
    const d = e.detail;
    gaEvent('PWAInstall', d.action, d.label, d.value, d.nonInteraction);
  });
}
