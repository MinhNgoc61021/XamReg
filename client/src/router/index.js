import Vue from 'vue'
import Router from 'vue-router'
import register from '@/components/Register/register';
import VeeValidate from 'vee-validate'
import Admin_Page from "../components/Admin/Admin_Page";
import upload from "../components/Admin/student_management/upload";
Vue.use(VeeValidate);
Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'register',
      component: register,
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin_Page,
    },
    {
      path: '/upload',
      name: 'upload',
      component: upload,
    }
  ]
})
