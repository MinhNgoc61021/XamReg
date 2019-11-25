<!--<template>-->
<!--  <a-layout id="components-layout-top-side">-->

<!--    &lt;!&ndash;    header&ndash;&gt;-->
<!--    <a-layout-header class="header" :style="{ position: 'fixed', zIndex: 2, width: '100%', background: '#fff' }" style="border-bottom: 1px solid #e8e8e8; min-height: 66px;">-->
<!--      <div class="logo" />-->
<!--      <a-menu-->
<!--        theme="light"-->
<!--        mode="horizontal"-->
<!--        :defaultSelectedKeys="[{ current_location }]"-->
<!--        :style="{ lineHeight: '64px' }">-->
<!--        <a-menu-item key="1" v-on:click="setLocation('1')"><router-link to="/student-management">Quản lý sinh viên</router-link></a-menu-item>-->
<!--        <a-menu-item key="2" v-on:click="setLocation('2')"><router-link to="/schedule-management">Quản lý kỳ thi</router-link></a-menu-item>-->
<!--        <a-dropdown :style="{ float: 'right' }" :trigger="['click']">-->
<!--          <a class="ant-dropdown-link" href="javascript:void(0)"><a-avatar size="large" icon="user" /></a>-->
<!--          <a-menu slot="overlay">-->
<!--            <a-menu-item key="0" href="javascript:void(0)">-->
<!--              <span style="text-align: center" ><strong>{{ fullname }}</strong> (ID: {{ ID }})</span>-->
<!--            </a-menu-item>-->
<!--            <a-menu-item key="1">-->
<!--              <a><a-icon type="user" class="logo-align"/><span>Cập nhật tài khoản</span></a>-->
<!--            </a-menu-item>-->
<!--            <a-menu-divider />-->
<!--            <a-menu-item key="2" v-on:click="admin_signOut()">-->
<!--              <a-icon type="logout" class="logo-align"/><span>Đăng xuất</span>-->
<!--            </a-menu-item>-->
<!--          </a-menu>-->
<!--        </a-dropdown>-->
<!--      </a-menu>-->
<!--    </a-layout-header>-->
<!--    &lt;!&ndash;    header&ndash;&gt;-->

<!--    &lt;!&ndash;    content&ndash;&gt;-->
<!--    &lt;!&ndash; component matched by the route will render here &ndash;&gt;-->
<!--    <router-view></router-view>-->
<!--    &lt;!&ndash;    content&ndash;&gt;-->

<!--    &lt;!&ndash;    footer&ndash;&gt;-->
<!--    <a-layout-footer style="text-align: center; color: #1890ff">-->
<!--      ExamReg-->
<!--    </a-layout-footer>-->
<!--    &lt;!&ndash;    footer&ndash;&gt;-->

<!--  </a-layout>-->
<!--&lt;!&ndash;</template>&ndash;&gt;-->
<!--<script>-->
<!--  import student_management from './student_management/student_management.vue';-->
<!--  import schedule_management from './schedule_management/schedule_management.vue';-->
<!--  import Register_form from '../Register/register.vue';-->
<!--  import  { mapState, mapActions, mapMutations } from 'vuex';-->

<!--  export default {-->
<!--      name: 'Admin_Page',-->
<!--      components: {-->
<!--          Register_form,-->
<!--          student_management, schedule_management,-->
<!--      },-->
<!--      data() {-->
<!--          return {-->
<!--              component: student_management,-->
<!--          }-->
<!--      },-->
<!--      computed: {-->
<!--          ...mapState([-->
<!--              'user', 'ID', 'fullname', 'userStatus', 'current_location',-->
<!--          ]),-->
<!--      },-->
<!--      methods: {-->
<!--          ...mapMutations([-->
<!--              'setCurrentLocation',-->
<!--          ]),-->
<!--          ...mapActions([-->
<!--              'SignOut', 'GetUserData'-->
<!--          ]),-->
<!--          admin_signOut: function() {-->
<!--              this.SignOut();-->
<!--          },-->
<!--          setLocation: function (index) {-->
<!--              this.setLocation(index);-->
<!--          }-->
<!--      },-->
<!--      created() {-->
<!--          this.GetUserData();-->
<!--      }-->
<!--  }-->
<!--</script>-->

<template>
  <section style="max-width: 1200px; margin: auto; background: #ffffff;">
    <!--header-->
    <div id="header">
      <b-navbar mobile-burger fixed-top style="max-width: 1200px; margin: auto">
          <template slot="brand">
              <b-navbar-item>
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
                      <strong>{{ ID }}</strong>
                  </b-navbar-item>
                  <hr class="dropdown-divider" aria-role="menuitem">
                  <b-navbar-item>
                    Cập nhật thông tin người dùng
                  </b-navbar-item>
                  <b-navbar-item v-on:click="admin_signOut()" >
                    Đăng xuất
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
          ExamReg
          <a href="">Github </a>
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
