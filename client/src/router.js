// where URLS are defined and mapped to components

import Vue from 'vue';
import Router from 'vue-router';
import register from './components/Register/register';
import Test from './components/Test';
import Password_Change from './components/Register/password-change';
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
    {
      path: '/new-password',
      name: 'password-change',
      component: Password_Change,
    },
  ],
});
