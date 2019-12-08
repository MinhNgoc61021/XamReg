import Vue from 'vue'
import Router from 'vue-router'
import register from '@/components/Register/register';
import VeeValidate from 'vee-validate'
import Admin_Page from "../components/Admin/admin_page";
import Student_Page from '../components/Student/student-page';
import upload from "../components/Admin/student_management/import/upload/upload";
import student_management from "../components/Admin/student_management/student_management";
import schedule_management from "../components/Admin/schedule_management/schedule_management";
import log_management from "../components/Admin/log_management/log_management";
import subject_management from "../components/Admin/subject_management/subject_management";
import { getToken } from "../components/api/jwt_handling";
Vue.use(VeeValidate);
Vue.use(Router);

export const router = new Router({
  mode: 'history',
  routes: [
    { path: '/register', name: 'register', component: register },
    { path: '/admin-page', name: 'admin', component: Admin_Page, redirect: '/student-management',
      children: [ { path: '/student-management', component: student_management },
                  { path: '/schedule-management', component: schedule_management },
                  { path: '/log-management', component: log_management },
                  { path: '/subject-management', component: subject_management }, ]
    },
    { path: '/student-page', name: 'student', component: Student_Page },
    { path: '/upload', name: 'upload', component: upload },
    { path: '/*', redirect: '/register'},
  ],
});


router.beforeEach ((to, from, next) => {

    // redirect to register page if not logged in or trying to access a restricted page
    // redirect to admin page if the user is an admin
    const publicPages = ['/register'];
    const adminPage = ['/admin-page', '/student-management', '/schedule-management', '/log-management', '/subject-management', '/upload'];
    const studentPage = ['/student-page'];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = getToken(localStorage.getItem('user'));

    // When logging in
    if (loggedIn) {
      if (loggedIn.type === 'Admin') {
        if (!authRequired) { // When location is register page
          return next('/admin-page');
        }
        else if (studentPage.includes(to.path)) { // When location is student-page
          return next('/admin-page');
        }
        else { // Move to a new hook
          return next();
        }
      }
      else if (loggedIn.type === 'Student') {
        if (!authRequired) { // When location is register page
          return next('/student-page');
        }
        else if (adminPage.includes(to.path)) { // When location is student-page
          return next('/student-page');
        }
        else { // Move to a new hook
          return next();
        }
      }
    }
    // When not logging in
    else if (!loggedIn) {
      if (authRequired) { // When there is no register page
        return next('/register');
      }
      else { // Move to a new hook
        return next();
      }
    }
    //else next();

});

