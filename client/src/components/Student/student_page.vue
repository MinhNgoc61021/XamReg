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
              <b-navbar-item tag="router-link" :to="{ name: 'student-info' }" class="routing-link">
                  Thông tin chung
              </b-navbar-item>
              <b-navbar-item tag="router-link" :to="{ name: 'shift-register', params: { studentid: ID } }" class="routing-link">
                  Đăng ký dự thi
              </b-navbar-item>
              <b-navbar-item tag="router-link" :to="{ name: 'export-ticket', params: { studentid: ID } }" class="routing-link">
                  In phiếu báo dự thi
              </b-navbar-item>
          </template>

          <template slot="end">
              <b-dropdown
                    position="is-bottom-left"
                    aria-role="menu">
                    <a
                        class="navbar-item"
                        slot="trigger"
                        role="button">
                        <span>{{ fullname }}</span>
                    </a>

                    <b-dropdown-item custom aria-role="menuitem">
                        <b-icon icon-pack="fas" icon="id-badge"></b-icon>
                        <strong>{{ ID }}</strong>
                    </b-dropdown-item>
                    <hr class="dropdown-divider">
                    <b-dropdown-item has-link aria-role="menuitem">
                        <a v-on:click="updatePassword" target="_blank">
                            <b-icon icon-pack="fas" icon="lock"></b-icon>
                            <span>Cập nhật mật khẩu</span>
                        </a>
                    </b-dropdown-item>
                    <b-dropdown-item has-link aria-role="menuitem">
                      <router-link :to="{ name: 'student-manual' }">
                        <b-icon icon-pack="fas" icon="question-circle"></b-icon>
                        <span>Trợ giúp</span>
                      </router-link>
                    </b-dropdown-item>
                    <b-dropdown-item has-link aria-role="menuitem">
                      <a v-on:click="admin_signOut">
                        <b-icon icon-pack="fas" icon="sign-out-alt"></b-icon>
                        <span>Đăng xuất</span>
                      </a>
                    </b-dropdown-item>
                </b-dropdown>
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
          <a href=""><span>Github</span> </a>
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
