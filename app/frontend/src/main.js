// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import iView from 'iview'
import VueCookies from 'vue-cookies'
import 'iview/dist/styles/iview.css'
import VueHeadful from 'vue-headful'
import RTMP from 'rtmp-streamer'
import AudioRecorder from 'vue-audio-recorder'
import VueHighlightJS from 'vue-highlightjs'
import 'highlight.js/styles/default.css'

Vue.component('vue-headful', VueHeadful)
Vue.use(iView)
Vue.use(VueCookies)
Vue.use(RTMP)
Vue.use(AudioRecorder)
Vue.use(VueHighlightJS)
Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
