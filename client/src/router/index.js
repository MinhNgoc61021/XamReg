import Vue from 'vue'
import Router from 'vue-router'
import register from '@/components/Register/register';
import VeeValidate from 'vee-validate'
import admin_page from "../components/Admin/admin_page";
import Student_Page from '../components/Student/student-page';
import upload from "../components/Admin/student_management/import/upload/upload";
import student_management from "../components/Admin/student_management/student_management";
import schedule_management from "../components/Admin/schedule_management/schedule_management";
import subjects_management from "../components/Admin/subjects_management/subjects_management";
import log_management from "../components/Admin/log_management/log_management";
import home_page from "../components/Student/home_page";
import shift_register from "../components/Student/shift_register/shift_register";

import { getToken } from "../components/api/jwt_handling";
import {store} from "../store/store";
Vue.use(VeeValidate);
Vue.use(Router);

export const router = new Router({
  mode: 'history',
  routes: [
    { path: '/register', name: 'register', component: register },
    { path: '/admin', name: 'admin', component: Admin_Page, redirect: '/student-management',
      children: [ { path: '/student-management', component: student_management },
                  { path: '/schedule-management', component: schedule_management },
                  { path: '/log-management', component: log_management },
                  { path: '/subjects-management', component: subjects_management }, ]
    },
    { path: '/student', name: 'student', component: Student_Page, redirect: '/student-home',
      children: [ { path: '/student-home', component: home_page },
                  { path: '/shift-register/:studentid', component: shift_register, name: 'shift_register' , props: true } ]
    },
    { path: '/upload', name: 'upload', component: upload },
    { path: '/*', redirect: '/register'},
  ],
});

router.beforeEach ((to, from, next) => {

    // redirect to register page if not logged in or trying to access a restricted page
    // redirect to admin page if the user is an admin
    // redirect to student page if the user is a student
    const publicPages = ['/register'];
    const adminPage = ['/admin', '/student-management', '/schedule-management', '/log-management', '/subject-management', '/upload'];
    const studentPage = ['/student', '/student-home', '/shift-register'];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = getToken(localStorage.getItem('user'));

    // When logging in
    if (loggedIn) {
      if (loggedIn.type === 'Admin') {
        if (!authRequired) { // When location is register page
          return next('/admin');
        }
        else if (studentPage.includes(to.path)) { // When location is student-page
          return next('/admin');
        }
        else { // Move to a new hook
          return next();
        }
      }
      else if (loggedIn.type === 'Student') {
        if (!authRequired) { // When location is register page
          return next('/student');
        }
        else if (adminPage.includes(to.path)) { // When location is student-page
          return next('/student');
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

