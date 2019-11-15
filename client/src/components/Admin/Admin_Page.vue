<template>
  <a-layout id="components-layout-top-side">

    <!--    header-->
    <a-layout-header class="header" :style="{ position: 'fixed', zIndex: 1, width: '100%', background: '#fff' }" style="border-bottom: 1px solid #e8e8e8; min-height: 66px;">
      <div class="logo" />
      <a-menu
        theme="light"
        mode="horizontal"
        :defaultSelectedKeys="['1']"
        :style="{ lineHeight: '64px' }">
        <a-menu-item key="1">Quản lý sinh viên</a-menu-item>
        <a-menu-item key="2">Quản lý ca thi</a-menu-item>
      </a-menu>
    </a-layout-header>
    <!--    header-->

    <!--    content-->
    <a-layout-content style="padding: 0 50px;margin-top: 70px;">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>Home</a-breadcrumb-item>
      </a-breadcrumb>
      <a-layout style="padding: 24px 0; background: #fff">
        <a-layout-sider width="200" style="background: #fff">
          <a-menu
            mode="inline"
            :defaultSelectedKeys="['1']"
            :defaultOpenKeys="['sub1']"
            style="height: 100%">
            <a-sub-menu key="sub1">
              <span slot="title"><a-icon type="upload" />Nhập sinh viên</span>
              <a-menu-item key="1">Nhập file</a-menu-item>
              <a-menu-item key="2">Nhập tay</a-menu-item>
            </a-sub-menu>
          </a-menu>
        </a-layout-sider>
        <a-layout-content :style="{ padding: '0 24px', minHeight: '280px' , position: 'relative', margin: 'auto' }">
          <div>
            <upload_student_list/>
          </div>
        </a-layout-content>
      </a-layout>
    </a-layout-content>
    <!--    content-->

    <!--    footer-->
    <a-layout-footer style="text-align: center; color: #1890ff">
      ExamReg
    </a-layout-footer>
    <!--    footer-->

  </a-layout>
</template>
<script>
  import upload_student_list from '../Admin/student_management/upload.vue';
  export default {
      name: 'Admin_Page',
      components: {
          upload_student_list,
      },
  }
</script>
<style>
  #components-layout-top-side .logo {
    width: 32px;
    height: 32px;
    background-image: url('/static/favicon-32x32.png');
    background-size: contain;
    margin: 16px 28px 16px 0;
    float: left;
  }
</style>
