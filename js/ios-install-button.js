'use strict';

/** Custom Element to prompt Safari users on iOS to install the PWA. */
class IOSInstallButton extends HTMLElement {
  /**
   * Base constructor.
   */
  constructor() {
    super();

    if (!this.canInstall || this.isInstalled) {
      this.setAttribute('disabled', '');
      return;
    }

    const innerHTML = `
      <style>
        #buttonInstall {
          background-color: var(--button-bg-color, blue);
          border: var(--button-border, 1px solid red);
          color: var(--button-color, white);
          font-size: var(--button-font-size, 1em);
          padding: var(--button-padding, 0.75em);
          margin: var(--button-margin, 0);
        }
        div {
          background-color: var(--banner-bg-color, white);
          bottom: 0;
          box-sizing: border-box;
          color: var(--banner-color, black);
          left: 0;
          padding: 1.5em 1em;
          position: fixed;
          width: 100%;
          transform: translateY(250px);
          transition-property: transform;
          transition-duration: 0.4s;
        }
        div.visible {
          transform: translateY(0);
        }
        #buttonClose {
          background-color: transparent;
          border: none;
          color: var(--banner-color, black);
          cursor: pointer;
          font-size: 2em;
          padding: 0 0 16px 16px;
          position: absolute;
          right: 0;
          text-align: center;
          top: -6px;
        }
      </style>
      <button id="buttonInstall" type="button">Install</button>
      <div id="sdInstallIOSBanner">
        To add <slot>this app</slot> to your home screen, press the Share
        button (below), then choose <em>Add to Home Screen</em>.
        <button id="buttonClose" type="button">&times;</button>
      </div>
    `;

    const shadowRoot = this.attachShadow({mode: 'open'});
    shadowRoot.innerHTML = innerHTML;

    const installButton = shadowRoot.querySelector('#buttonInstall');
    installButton.addEventListener('click', () => {
      this._showBanner(true);
      setTimeout(() => {
        installButton.style.display = 'none';
      }, 600);
      const e = new Event('click-install', {bubbles: true, composed: true});
      this.dispatchEvent(e);
    });
    const closeBannerButton = shadowRoot.querySelector('#buttonClose');
    closeBannerButton.addEventListener('click', (e) => {
      e.preventDefault(true);
      this._showBanner(false);
      setTimeout(() => {
        this.setAttribute('disabled', '');
      }, 1000);
    });
  }
  /**
   * Connected callback
   */
  connectedCallback() {
    this.removeAttribute('disabled');
    // eslint-disable-next-line compat/compat
    fetch('/manifest.json')
        .then((resp) => resp.json())
        .then((manifest) => {
          const appName = manifest.name;
          this.innerText = appName;
          const prefix = 'apple-mobile-web-app';
          this._addMetaTag(`${prefix}-title`, appName);
          this._addMetaTag(`${prefix}-capable`, 'yes');
          this._addMetaTag(`${prefix}-status-bar-style`, 'black-translucent');
          let largestIcon = {size: 0};
          const icons = manifest.icons || [];
          icons.forEach((icon) => {
            const opts = {
              href: icon.src,
              sizes: icon.sizes,
            };
            this._addLinkTag('apple-touch-icon', opts);
            const size = parseInt(icon.sizes.match(/\d+/)[0]);
            if (size > 192) {
              return;
            }
            if (size > largestIcon.size) {
              largestIcon.size = size;
              largestIcon.url = icon.src;
            }
          });
          if (largestIcon.url) {
            const splashText = appName;
            const splashIcon = largestIcon.url;
            const splashFg = 'white';
            const splashBg = manifest.theme_color;
            this._addSplash(splashText, splashIcon, splashFg, splashBg);
          }
        });
  }
  /**
   * Adds a splash screen to the app.
   * @param {string} appName - Name of the app.
   * @param {string} iconURL - Path the the icon image.
   * @param {string} fgColor - Color to use for the text.
   * @param {string} bgColor - Color to use for the splash screen background.
   */
  _addSplash(appName, iconURL, fgColor, bgColor) {
    const icon = document.createElement('img');
    icon.src = iconURL;
    icon.onload = function() {
      // Create the canvas
      const dpr = window.devicePixelRatio;
      const width = window.screen.width;
      const height = window.screen.height;
      const canvas = document.createElement('canvas');
      canvas.width = width * dpr;
      canvas.height = height * dpr;
      const ctx = canvas.getContext('2d');
      ctx.scale(dpr, dpr);
      // Fill it with the bgColor
      ctx.fillStyle = bgColor;
      ctx.fillRect(0, 0, width, height);
      ctx.translate(width / 2, (height - 32) / 2);
      // Create the text for the app name
      ctx.font = '24px HelveticaNeue-CondensedBold';
      ctx.fillStyle = fgColor;
      const textWidth = ctx.measureText(appName).width;
      // Draw the icon
      const icWidth = icon.width / dpr;
      const icHeight = icon.height / dpr;
      ctx.drawImage(icon, icWidth / -2, icHeight / -2, icWidth, icHeight);
      // Draw the text for the app name
      ctx.translate(0, icHeight / 2 + 32);
      ctx.fillText(appName, textWidth / -2, 0);
      // Create and add the link tag to the page
      const linkTag = document.createElement('link');
      linkTag.rel = 'apple-touch-startup-image';
      linkTag.href = ctx.canvas.toDataURL();
      document.head.append(linkTag);
    };
  }
  /**
   * Helper function to add a meta tag to the document head.
   * @param {string} name - Name of the meta tag.
   * @param {string} content - Content of the meta tag.
   */
  _addMetaTag(name, content) {
    const tag = document.createElement('meta');
    tag.name = name;
    tag.content = content;
    document.head.append(tag);
  }
  /**
   * Helper function to add a link tag to the document head.
   * @param {string} rel
   * @param {Object} props
   */
  _addLinkTag(rel, props) {
    const tag = document.createElement('link');
    tag.rel = rel;
    // eslint-disable-next-line guard-for-in
    for (const prop in props) {
      tag.setAttribute(prop, props[prop]);
    }
    document.head.append(tag);
  }
  /**
   * Show or hide the banner
   * @private
   * @param {boolean} visible - True to show the banner
   */
  _showBanner(visible) {
    const banner = this.shadowRoot.querySelector('div');
    banner.classList.toggle('visible', visible);
  }
  /**
   * Is the PWA already installed?
   * @readonly
   * @member {boolean}
   */
  get isInstalled() {
    if (this.canInstall && window.navigator.standalone) {
      return true;
    }
    return false;
  }
  /**
   * Can the PWA be installed?
   * @readonly
   * @member {boolean}
   */
  get canInstall() {
    const ua = window.navigator.userAgent;
    const reAppleDevice = /iphone|ipod|ipad/i;
    const isAppleDevice = reAppleDevice.test(ua);
    const reSafari = /safari/i;
    const isSafari = reSafari.test(ua);
    const supportsStandAlone = 'standalone' in window.navigator;
    return isAppleDevice && isSafari && supportsStandAlone;
  }
}

window.customElements.define('ios-install-button', IOSInstallButton);
