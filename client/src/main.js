/*app entry point, which loads and initializes Vue along with the root component*/

import Vue from 'vue';
import 'bootstrap/dist/css/bootstrap.css';
import App from './App.vue';
import router from './router';
import {VeeValidate} from 'vee-validate'; //npm i vee-validate --save

Vue.config.productionTip = false;
//Vue.use({VeeValidate});

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
