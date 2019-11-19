import Vue from 'vue'
import Router from 'vue-router'
import register from '@/components/Register/register';
import VeeValidate from 'vee-validate'
import Admin_Page from "../components/Admin/admin_page";
import upload from "../components/Admin/student_management/import/upload";
Vue.use(VeeValidate);
Vue.use(Router);

export const router = new Router({
  mode: 'history',
  routes: [
    { path: '/register', name: 'register', component: register },
    { path: '/admin-page', name: 'admin', component: Admin_Page },
    { path: '/upload', name: 'upload', component: upload },
    { path: '/*', redirect: '/register'},
  ],
});
router.beforeEach ((to, from, next) => {
    // redirect to register page if not logged in and trying to access a restricted page
    const publicPages = ['/register'];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = JSON.parse(localStorage.getItem('user'));
    if (loggedIn) {
      if (loggedIn.type === 'admin') {
        if (!authRequired) { // When there is register page
          return next('/admin-page');
        } else { //Move to a new hook
          return next();
        }
      }
      if (loggedIn.type === 'student') {
        if (!authRequired) { // When there is register page
          return next('/student-page');
        } else {
          return next();
        }
      }
    }
    else if (!loggedIn) {
      if (authRequired) { // When there is no register page
        return next('/register');
      }
      else { // Move to a new hook
        return next();
      }
    }
    else next();

});

