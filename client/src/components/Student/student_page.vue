<template>
  <section style="max-width: 1200px; margin: auto; background: #ffffff;">
    <!--header-->
    <div id="header">
      <b-navbar mobile-burger fixed-top style="max-width: 1200px; margin: auto" shadow>
          <template slot="brand">
              <b-navbar-item title="ExamReg">
                  <img :src="'/static/img/favicon-32x32.png'"
                   alt="ExamReg">
              </b-navbar-item>
          </template>

          <template slot="start">
              <b-navbar-item tag="router-link" :to="{ name: 'student-home', params: { studentid: ID } }" class="routing-link">
                  Trang chủ
              </b-navbar-item>
              <b-navbar-item tag="router-link" :to="{ name: 'shift-register', params: { studentid: ID } }" class="routing-link">
                  Đăng ký dự thi
              </b-navbar-item>
          </template>

          <template slot="end">
              <b-navbar-dropdown right arrowless v-bind:label="fullname">
                  <b-navbar-item>
                    <b-icon icon-pack="fas" icon="id-badge"></b-icon>
                    <strong>{{ ID }}</strong>
                  </b-navbar-item>
                  <hr class="dropdown-divider" aria-role="menuitem">
                  <b-navbar-item v-on:click="updatePassword">
                    <b-icon icon-pack="fas" icon="lock"></b-icon>
                    <span>Cập nhật mật khẩu</span>
                  </b-navbar-item>
                  <b-navbar-item tag="router-link" :to="{ path: '/student-manual' }">
                    <b-icon icon-pack="fas" icon="question-circle"></b-icon>
                    <span>Trợ giúp</span>
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
          <a href=""> <b-icon icon-pack="fas" icon="github-circle"></b-icon> <span>Github</span> </a>
        </p>
      </div>
    </footer>
  </section>
</template>

<script>
  import { mapState, mapActions, mapMutations } from 'vuex';
  import update_password from "../Personal_Info/update_password";
  import shift_register from "./shift_register/shift_register";


  export default {
      name: 'Student_Page',
      components: {
          shift_register,
      },
      computed: {
          ...mapState([
              'ID', 'fullname', 'userStatus'
          ]),
      },
      methods: {
          ...mapActions([
              'SignOut', 'GetUserData'
          ]),
          admin_signOut() {
              this.SignOut();
          },
          updatePassword() {
              this.$buefy.modal.open({
                   parent: this,
                   component: update_password,
                   props: {
                       currentUserID: this.ID,
                   },
                   hasModalCard: true,
                   customClass: 'custom-class custom-class-2',
                   canCancel: false,
                })
          },
      },
      created() {
          this.GetUserData();
      }
  }
</script>
<style>

</style>
