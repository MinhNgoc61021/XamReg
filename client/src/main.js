// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import { router }  from './router/index.js';
import Buefy from 'buefy';
// import 'buefy/dist/buefy.css'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faUserSecret);

Vue.component('font-awesome-icon', FontAwesomeIcon);
import Antd  from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';
import { store } from './store/store.js';

library.add(faUserSecret);

Vue.use(Buefy);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
