import Vue from 'vue'
import Router from 'vue-router'
import register from '@/components/Register/register';
import VeeValidate from 'vee-validate'
import Admin_Page from "../components/Admin/admin_page";
import upload from "../components/Admin/student_management/import/upload";
Vue.use(VeeValidate);
Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    { path: '/register', name: 'register', component: register },
    { path: '/admin-page', name: 'admin', component: Admin_Page },
    { path: '/upload', name: 'upload', component: upload },
    { path: '*', redirect: '/register'}
  ],
  beforeEach: function (to, from, next) {
    // redirect to register page if not logged in and trying to access a restricted page
    const publicPages = ['/register'];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = localStorage.getItem('user');

    if (authRequired && !loggedIn) {
      return next('/register');
    }

    else { next(); }
  }
});
