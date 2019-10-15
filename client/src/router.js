// where URLS are defined and mapped to components

import Vue from 'vue';
import Router from 'vue-router';
import register_form from './components/register-form'
Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/register-form',
      name: 'Register_form',
      component: register_form,
    }
  ],
});
