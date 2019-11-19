<template>
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
              <span slot="title"><a-icon type="upload" :size="32"/>Nhập</span>
              <a-menu-item v-on:click="component='upload_student_list'" key="1"><a-icon type="file-add" />Nhập file</a-menu-item>
              <a-menu-item v-on:click="component='input_student'"><a-icon type="edit" />Nhập tay</a-menu-item>
            </a-sub-menu>
          </a-menu>
        </a-layout-sider>
        <a-layout-content :style="{ padding: '0 24px', minHeight: '280px' , position: 'relative', margin: 'auto' }">
            <keep-alive>
              <component v-bind:is="component" />
            </keep-alive>
        </a-layout-content>
      </a-layout>
    </a-layout-content>
</template>
<script>
  import upload_student_list from './import/upload.vue';
  import input_student from './import/input.vue';
  export default {
      name: 'student_management',
      components: {
          upload_student_list, input_student
      },
      data() {
          return {
              component: upload_student_list,
          }
      },
  }
</script>
<style>
</style>
