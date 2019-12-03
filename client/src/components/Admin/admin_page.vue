<template>
  <section style="max-width: 1200px; margin: auto; background: #ffffff;">
    <!--header-->
    <div id="header">
      <b-navbar mobile-burger fixed-top style="max-width: 1200px; margin: auto" shadow>
          <template slot="brand">
              <b-navbar-item title="ExamReg">
                  <img src="static/img/favicon-32x32.png"
                   alt="ExamReg">
              </b-navbar-item>
          </template>
          <template slot="start">
              <b-navbar-item tag="router-link" :to="{ path: '/student-management' }" class="routing-link">
                  Quản lý sinh viên
              </b-navbar-item>
              <b-navbar-item tag="router-link" :to="{ path: '/schedule-management' }" class="routing-link">
                  Quản lý lịch thi
              </b-navbar-item>
          </template>

          <template slot="end">
              <b-navbar-dropdown right arrowless v-bind:label="fullname">
                  <b-navbar-item>
                    <b-icon icon-pack="fas" icon="id-badge"></b-icon>
                    <strong>{{ ID }}</strong>
                  </b-navbar-item>
                  <hr class="dropdown-divider" aria-role="menuitem">
                  <b-navbar-item>
                    <b-icon icon-pack="fas" icon="user"></b-icon>
                    <span>Cập nhật thông tin người dùng</span>
                  </b-navbar-item>
                  <b-navbar-item v-on:click="admin_signOut()" >
                    <b-icon icon-pack="fas" icon="sign-out-alt"></b-icon>
                    <span>Đăng xuất</span>
                  </b-navbar-item>
              </b-navbar-dropdown>
          </template>
      </b-navbar>
    </div>
    <!--header-->

    <!--content-->
    <div class="hero-body">
          <router-view></router-view>
    </div>
    <!--content-->

    <footer class="footer">
      <div class="content has-text-centered" >
        <p>

          <span>ExamReg</span>
          <a href=""> <span>Github</span> </a>
        </p>
      </div>
    </footer>
  </section>
</template>

<script>
  import student_management from './student_management/student_management.vue';
  import schedule_management from './schedule_management/schedule_management.vue';
  import Register_form from '../Register/register.vue';
  import  { mapState, mapActions, mapMutations } from 'vuex';
  export default {
      name: 'Admin_Page',
      components: {
          Register_form,
          student_management, schedule_management,
      },
      data() {
          return {
              component: student_management,
          }
      },
      computed: {
          ...mapState([
              'user', 'ID', 'fullname', 'userStatus', 'current_location',
          ]),
      },
      methods: {
          ...mapMutations([
              'setCurrentLocation',
          ]),
          ...mapActions([
              'SignOut', 'GetUserData'
          ]),
          admin_signOut: function() {
              this.SignOut();
          },
      },
      created() {
          this.GetUserData();
      }
  }
</script>
<style>

</style>
