// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from './router';
import iView from 'iview';
import 'iview/dist/styles/iview.css';
import Vuex from 'vuex'
import VueCookies from 'vue-cookies'
Vue.use(VueCookies)

Vue.use(iView);
Vue.config.productionTip = false
Vue.use(Vuex)
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
});

const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment (state) {
      state.count++
    }
  }
})
