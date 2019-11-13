<template>
  <a-layout id="components-layout-demo-top-side">
    <a-layout-header class="header">
      <div class="logo" />
      <a-menu
        theme="dark"
        mode="horizontal"
        :defaultSelectedKeys="['2']"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="1">Trang chủ</a-menu-item>
        <a-menu-item key="2">Khóa học</a-menu-item>
        <a-menu-item key="3">Thống kê</a-menu-item>
        <a-menu-item key="4"></a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout-content style="padding: 0 50px">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>Home</a-breadcrumb-item>
        <a-breadcrumb-item>Admin</a-breadcrumb-item>
        <a-breadcrumb-item>Student Management</a-breadcrumb-item>
      </a-breadcrumb>
      <a-layout style="padding: 24px 0; background: #fff">
        <a-layout-sider width="200" style="background: #fff">
          <a-menu
            mode="inline"
            :defaultSelectedKeys="['1']"
            :defaultOpenKeys="['sub1']"
            style="height: 100%"
          >
            <a-sub-menu key="sub1">
              <span slot="title"><a-icon type="user" />Caccac1</span>
              <a-menu-item key="1">Quản lý tài khoản</a-menu-item>
              <a-menu-item key="2">Quản lý môn thi</a-menu-item>
            </a-sub-menu>
            <a-sub-menu key="sub2">
              <span slot="title"><a-icon type="user" />CACLC-2</span>
              <a-menu-item key="1">Quản lý tài khoản</a-menu-item>
              <a-menu-item key="2">Quản lý môn thi</a-menu-item>
            </a-sub-menu>
            <a-sub-menu key="sub3">
              <span slot="title"><a-icon type="user" />CACLC-3</span>
              <a-menu-item key="1">Quản lý tài khoản</a-menu-item>
              <a-menu-item key="2">Quản lý môn thi</a-menu-item>
            </a-sub-menu>
          </a-menu>
        </a-layout-sider>
        <a-layout-content :style="{ padding: '0 24px', minHeight: '280px' }">
          Content
        </a-layout-content>
      </a-layout>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
    </a-layout-footer>
  </a-layout>
</template>
<script>
    export default {
        name: 'Admin_Page'
    }
</script>

<style scoped>
</style>
