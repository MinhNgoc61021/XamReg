<template>
  <div id="dragger-container">
    <a-upload-dragger
    name="student_list_excel"
    :multiple="true"
    action="/handling/upload"
    :headers="headers"
    @change="handleChange">
      <p class="ant-upload-drag-icon">
        <a-icon type="inbox" />
      </p>
      <p class="ant-upload-text">Chọn hoặc kéo thả file của bạn để tải lên</p>
      <p class="ant-upload-hint">
        Hỗ trợ tải một hoặc nhiều file <a-icon type="file-excel" /> Excel.
        <strong>(Hãy dùng định dạng .xlsx)</strong>
      </p>
    </a-upload-dragger>
  </div>
</template>
<script>
  import { authHeader } from "../../../api/jwt_handling";
  export default {
    data() {
      return {
          upload_status: '',
          headers: authHeader(),
      }
    },
    methods: {
      handleChange(info) {
        const status = info.file.status;
        if (status !== 'uploading') {
            console.log(info.file, info.fileList);
        }
        if (status === 'done') {
            this.$message.success(`${info.file.name} đã được tải lên thành công.`);
        }
        else if (status === 'error') {
            this.$message.error(`${info.file.name} không được tải lên thành công.`);
        }
      },
    },
  };
</script>
<style scoped>
  #dragger-container {
    margin: auto;
    width: 70%;
    left: 15%;
    position: absolute;
    top: 20%;
  }
</style>

