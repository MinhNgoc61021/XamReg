<template>
  <a-layout-content style="padding: 0 50px;margin-top: 70px;">
    <a-layout-content style="padding: 0 50px;margin-top: 70px;">
      <a-layout-sider width="200" style="background: #fff">
        <a-menu
          mode="inline"
          :defaultSelectedKeys="['1']"
          :defaultOpenKeys="['sub1']"
          style="height: 100%">
            <a-menu-item v-on:click="component='student_info_lookup'" key="1"><a-icon type="edit" />Tra cứu sinh viên</a-menu-item>
            <a-menu-item v-on:click="component='create_exam'"><a-icon type="file-add" />Tạo kì thi</a-menu-item>
        </a-menu>
      </a-layout-sider>
    </a-layout-content>

    <a-layout-content :style="{ padding: '0 24px', minHeight: '280px' , position: 'relative', margin: 'auto' }">
      <div>
        asckascokma
      </div>
    </a-layout-content>
  </a-layout-content>
</template>
<script>
    export default {
        name: "schedule_management"
    }
</script>

<style scoped>
  #spin-container {
    text-align: center;
    background: rgba(0, 0, 0, 0.05);
    border-radius: 4px;
    margin-bottom: 20px;
    padding: 30px 50px;
    margin: 20px 0;
  }
</style>
