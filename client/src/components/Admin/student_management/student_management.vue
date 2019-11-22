<template>
  <a-layout-content style="padding: 0 50px;margin-top: 70px;">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>Home</a-breadcrumb-item>
      </a-breadcrumb>
      <a-layout id="main-content" style="padding: 24px 0; background: #fff">

        <!--sider-->
        <a-layout-sider width="200" style="background: #fff">
          <a-menu
            mode="inline"
            :defaultSelectedKeys="['1']"
            :defaultOpenKeys="['sub1']"
            style="height: 100%">
            <a-sub-menu key="sub1">
              <span slot="title" title="Nhập"><a-icon type="upload" :size="32" title="Nhập"/>Nhập (Import)</span>
              <a-menu-item v-on:click="component='upload_student_list'" key="1"><a-icon type="file-add" />Nhập file</a-menu-item>
              <a-menu-item v-on:click="component='input_student'"><a-icon type="edit" />Nhập tay</a-menu-item>
            </a-sub-menu>
            <a-sub-menu>
              <span slot="title" title="Xem & Cập nhật danh sách sinh viên"><a-icon type="upload" :size="32" />Xem & Cập nhật danh sách sinh viên</span>
              <a-menu-item v-on:click="component='record_management'"><a-icon type="ordered-list" />Danh sách</a-menu-item>
            </a-sub-menu>
          </a-menu>

        </a-layout-sider>
        <!--sider-->

        <!--content-->
        <a-layout-content :style="{ padding: '0 24px', minHeight: '280px' , position: 'relative', margin: 'auto' }" >
            <keep-alive>
              <component v-bind:is="component" />
            </keep-alive>
        </a-layout-content>
        <!--content-->

      </a-layout>
    </a-layout-content>
</template>
<script>
  import upload_student_list from './import/upload.vue';
  import input_student from './import/input.vue';
  import record_management from "./student_record_management/record_management";

  export default {
      name: 'student_management',
      components: {
          upload_student_list, input_student, record_management
      },
      data() {
          return {
              component: upload_student_list,
          }
      },
  }
</script>
<style>
  @media screen and (max-width: 400px) {
    #main-content {
      overflow-x: scroll;
    }
  }
  #main-content {

  }
</style>
