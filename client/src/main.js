// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import { router }  from './router/index.js';
import { store } from './store/store.js';
import Buefy from 'buefy';
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

export const eventBus = new Vue();

library.add(fas);
Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.use(Buefy, {
    defaultIconPack: 'fas',
    // ...
});
Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
