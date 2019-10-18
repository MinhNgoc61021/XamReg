// where URLS are defined and mapped to components

import Vue from 'vue';
import Router from 'vue-router';
import register from './components/register';
import Test from './components/Test';
Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/register',
      name: 'register',
      component: register,
    },
    {
      path: '/test',
      name: 'Test',
      component: Test,
    },
  ],
});
