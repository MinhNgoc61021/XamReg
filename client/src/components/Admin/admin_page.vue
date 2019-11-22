<template>
  <a-layout id="components-layout-top-side">

    <!--    header-->
    <a-layout-header class="header" :style="{ position: 'fixed', zIndex: 2, width: '100%', background: '#fff' }" style="border-bottom: 1px solid #e8e8e8; min-height: 66px;">
      <div class="logo" />
      <a-menu
        theme="light"
        mode="horizontal"
        :defaultSelectedKeys="['1']"
        :style="{ lineHeight: '64px' }">
        <a-menu-item key="1" v-on:click="component='student_management'" >Quản lý sinh viên</a-menu-item>
        <a-menu-item key="2" v-on:click="component='schedule_management'">Quản lý kỳ thi</a-menu-item>
        <a-dropdown :style="{ float: 'right' }" :trigger="['click']">
          <a class="ant-dropdown-link" href="javascript:void(0)"><a-avatar size="large" icon="user" /></a>
          <a-menu slot="overlay">
            <a-menu-item key="0" href="javascript:void(0)">
              <span style="text-align: center" ><strong>{{ fullname }}</strong> (ID: {{ ID }})</span>
            </a-menu-item>
            <a-menu-item key="1">
              <a><a-icon type="user" class="logo-align"/><span>Cập nhật tài khoản</span></a>
            </a-menu-item>
            <a-menu-divider />
            <a-menu-item key="2" v-on:click="admin_signOut()">
              <a-icon type="logout" class="logo-align"/><span>Đăng xuất</span>
            </a-menu-item>
          </a-menu>
        </a-dropdown>
      </a-menu>
    </a-layout-header>
    <!--    header-->

    <!--    content-->
    <keep-alive>
      <component v-bind:is="component" />
    </keep-alive>
    <!--    content-->

    <!--    footer-->
    <a-layout-footer style="text-align: center; color: #1890ff">
      ExamReg
    </a-layout-footer>
    <!--    footer-->

  </a-layout>
</template>
<script>
  import student_management from './student_management/student_management.vue';
  import schedule_management from './schedule_management/schedule_management.vue';
  import Register_form from '../Register/register.vue';
  import  { mapState, mapActions } from 'vuex';

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
              'user', 'ID', 'fullname', 'userStatus'
          ]),
      },
      methods: {
          ...mapActions([
              'SignOut', 'GetUserData'
          ]),
          admin_signOut: function() {
              this.SignOut();
          }
      },
      created() {
          this.GetUserData();
      }
  }
</script>
<style>
  .logo-align {
    padding-right: 5px;
    transform: translate(-2px, -4px);
  }
  #components-layout-top-side .logo {
    width: 32px;
    height: 32px;
    background-image: url('/static/img/favicon-32x32.png');
    background-size: contain;
    margin: 16px 28px 16px 0;
    float: left;
  }
</style>
