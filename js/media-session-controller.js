'use strict';

/** Custom Element to prompt Safari users on iOS to install the PWA. */
class MediaSessionController extends HTMLElement {
  /**
   * Base constructor.
   */
  constructor() {
    super();
    this._enabled = ('mediaSession' in navigator);
    if (!this.enabled) {
      console.log('🔈', 'Media Session not available.');
      return;
    }
    const innerHTML = `
      <style>
        :host {
          display: none;
        }
      </style>
      <audio controls preload="auto" loop src="/sounds/silence.mp3"></audio>
    `;
    const shadowRoot = this.attachShadow({mode: 'open'});
    shadowRoot.innerHTML = innerHTML;
    this._audioElement = shadowRoot.querySelector('audio');
    this._initMediaSession();
    this.dispatchEvent(new Event('ready'));
  }
  /**
   * Initializes the media session API.
   * @private
   */
  _initMediaSession() {
    const defaultMetadata = {
      title: 'SoundDrown',
      album: 'White Noise Generator',
      artwork: [
        {src: '/icons/48.png', sizes: '48x48', type: 'image/png'},
        {src: '/icons/192.png', sizes: '192x192', type: 'image/png'},
        {src: '/icons/256.png', sizes: '256x256', type: 'image/png'},
        {src: '/icons/512.png', sizes: '512x412', type: 'image/png'},
      ],
    };
    // eslint-disable-next-line no-undef
    navigator.mediaSession.metadata = new MediaMetadata(defaultMetadata);
    navigator.mediaSession.setActionHandler('play', (evt) => {
      this._handlePlay(evt);
    });
    navigator.mediaSession.setActionHandler('pause', (evt) => {
      this._handlePause(evt);
    });
  }
  /**
   * Play or Pause the &lt;audio> player.
   * @private
   * @param {boolean} start - True starts, false pauses the &lt;audio> element.
   * @return {boolean} The current media session play state.
   */
  _toggleAudioElem(start) {
    start = !!start;
    if ((start && this.playing) || (!start && !this.playing)) {
      return this.playing;
    }
    if (start) {
      this._audioElement.play();
      return true;
    }
    this._audioElement.pause();
    return false;
  }
  /**
   * Handle the play event.
   * @private
   * @param {Event} evt - the event that triggered the play.
   * @return {boolean} The current media session play state.
   */
  _handlePlay(evt) {
    if (this.playing) {
      console.log('🔈', 'Already playing, ignore.');
      return true;
    }
    if (this._previousState) {
      for (const key in this._previousState) {
        if (this._previousState[key]) {
          const button = document.querySelector(`#${key}`);
          button.noise.play();
        }
      }
      this._previousState = null;
    } else {
      const selector = this.getAttribute('selector');
      const button = document.querySelector(selector);
      if (button) {
        button.noise.play();
      }
    }
    this._toggleAudioElem(true);
    this.dispatchEvent(new Event('play'));
    return true;
  }
  /**
   * Handle the pause event.
   * @private
   * @param {Event} evt - the event that triggered the pause.
   * @return {boolean} The current media session play state.
   */
  _handlePause(evt) {
    if (!this.playing) {
      console.log('🔈', 'Already paused, ignore.');
      return false;
    }
    this._previousState = {};
    const selector = this.getAttribute('selector');
    const buttons = document.querySelectorAll(selector) || [];
    buttons.forEach((button) => {
      const buttonID = button.id;
      const isPlaying = button.getAttribute('aria-checked') === 'true';
      this._previousState[buttonID] = isPlaying;
      button.noise.pause();
    });
    this._audioElement.pause();
    this._toggleAudioElem(false);
    this.dispatchEvent(new Event('pause'));
    return false;
  }
  /**
   * Is the media session available?
   * @readonly
   * @member {boolean}
   */
  get enabled() {
    return this._enabled;
  }
  /**
   * Get the &lt;audio> player play status
   * @readonly
   * @member {boolean}
   */
  get playing() {
    if (this._audioElement) {
      return !this._audioElement.paused;
    }
    return false;
  }
  /**
   * Update the Media Session Play state.
   * @return {boolean} True if any sounds are currently playing.
   */
  updatePlayState() {
    let playing = false;
    const selector = this.getAttribute('selector');
    const buttons = document.querySelectorAll(selector) || [];
    buttons.forEach((button) => {
      if (button.getAttribute('aria-checked') === 'true') {
        playing = true;
      }
    });
    this._toggleAudioElem(playing);
    return playing;
  }
}

window.customElements.define(
    'media-session-controller', MediaSessionController);
