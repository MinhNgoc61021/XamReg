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
          </template>

          <template slot="end">
              <b-navbar-dropdown right arrowless v-bind:label="fullname">
                  <b-navbar-item>
                    <b-icon icon-pack="fas" icon="id-badge"></b-icon>
                    <strong>{{ ID }}</strong>
                  </b-navbar-item>
                  <hr class="dropdown-divider" aria-role="menuitem">
                  <b-navbar-item>
                    <b-icon icon-pack="fas" icon="lock"></b-icon>
                    <span>Cập nhật mật khẩu</span>
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
      <div class="container">
        <h1 class="title is-3">Đăng ký thi</h1>
        <h2 class="subtitle is-6">Đăng ký dự thi ca thi theo học phần của sinh viên</h2>
        <b-tabs type="is-toggle" expanded>
          <b-tab-item label="Đăng ký dự thi" icon-pack="fas" icon="calendar-check">
            <shift_register :student-i-d="ID">
            </shift_register>
          </b-tab-item>
          <b-tab-item label="Kiểm tra & xuất (Export) phiếu dự thi" icon-pack="fas" icon="file-export">

          </b-tab-item>
        </b-tabs>
      </div>
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
  import { mapState, mapActions, mapMutations } from 'vuex';
  import shift_register from "./shift_register/shift_register";
  export default {
      name: 'Student_Page',
      components: {
          shift_register,
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
          admin_signOut() {
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
