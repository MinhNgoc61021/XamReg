<template>
  <a-layout-content style="padding: 0 50px;margin-top: 70px;">
    <div id="spin-container">
      <a-spin />
    </div>
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
