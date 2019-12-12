import Vue from 'vue'
import Router from 'vue-router'
import register from '@/components/Register/register';
import VeeValidate from 'vee-validate'
import admin_page from "../components/Admin/admin_page";
import student_page from "../components/Student/student_page";
import upload from "../components/Admin/student_management/import/upload/upload";
import student_management from "../components/Admin/student_management/student_management";
import schedule_management from "../components/Admin/schedule_management/schedule_management";
import log_management from "../components/Admin/log_management/log_management";
import shift_register from "../components/Student/shift_register/shift_register";
import subject_management from "../components/Admin/subject_management/subject_management";
import student_home_page from "../components/Student/home_page";
import shift_register from "../components/Student/shift_register/shift_register";
import exam_room_management from "../components/Admin/exam_room_management/exam_room_management"
import { getToken } from "../components/api/jwt_handling";
Vue.use(VeeValidate);
Vue.use(Router);

export const router = new Router({
  mode: 'history',
  routes: [
    { path: '/register', name: 'register', component: register },
    { path: '/admin', name: 'admin', component: admin_page, redirect: '/student-management',
      children: [ { path: '/student-management', component: student_management },
                  { path: '/schedule-management', component: schedule_management },
                  { path: '/log-management', component: log_management },
                  { path: '/subject-management', component: subject_management },
                  { path: '/exam-room-management', component: exam_room_management },],
    },
    { path: '/student', name: 'student', component: Student_Page, redirect: '/student-home',
      children: [ { path: '/student-home', component: student_home_page },
                  { path: '/shift-register/:studentid', component: shift_register, name: 'shift_register' , props: true,
                    beforeEnter (to, from, next)  {
                        if (getToken(localStorage.getItem('user')).type === 'Admin') {
                            return next('/admin');
                        }
                        else {
                          return next();
                        }
                    }
                  } ],
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
    const adminPage = ['/admin', '/student-management', '/schedule-management', '/log-management', '/subject-management', '/exam-room-management'];
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

