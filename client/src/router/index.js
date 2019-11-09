import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import register from '@/components/Register/register';
import Test from '@/components/Test';
import VeeValidate from 'vee-validate'

Vue.use(VeeValidate);
Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/',
      name: 'register',
      component: register,
    },
    {
      path: '/test',
      name: 'Test',
      component: Test,
    },
  ]
})
