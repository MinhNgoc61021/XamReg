<!--<template>-->
<!--  <div class="clearfix">-->
<!--    <a-upload :fileList="excelFileList" :remove="handleRemove" :beforeUpload="beforeUpload">-->
<!--      <a-button> <a-icon type="upload" /> Chọn Tệp Excel </a-button>-->
<!--    </a-upload>-->
<!--    <a-button-->
<!--      type="primary"-->
<!--      @click="handleUpload"-->
<!--      :disabled="excelFileList.length === 0"-->
<!--      :loading="uploading"-->
<!--      style="margin-top: 16px">-->
<!--      {{uploading ? 'Đang tải' : 'Tải lên' }}-->
<!--    </a-button>-->
<!--  </div>-->
<!--</template>-->
<!--<script>-->
<!--  import axios from 'axios';-->
<!--  export default {-->
<!--      name: "upload_student-list",-->
<!--    data() {-->
<!--      return {-->
<!--        excelFileList: [],-->
<!--        uploading: false,-->
<!--      };-->
<!--    },-->
<!--    methods: {-->
<!--        handleRemove: function (file) {-->
<!--          const index = this.excelFileList.indexOf(file);-->
<!--          const newFileList = this.excelFileList.slice();-->
<!--          newFileList.splice(index, 1);-->
<!--          this.excelFileList = newFileList;-->
<!--        },-->
<!--        beforeUpload: function (file) {-->
<!--          this.excelFileList = [...this.excelFileList, file];-->
<!--          return false;-->
<!--        },-->
<!--        handleUpload: function () {-->
<!--          const { excelFileList } = this;-->
<!--          const excelFormData = new FormData();-->
<!--          excelFormData.append('student_list_excel', excelFileList[0]);-->
<!--          this.uploading = true;-->
<!--          axios({-->
<!--              url: '/handling/upload',-->
<!--              method: 'post',-->
<!--              headers: { 'Content-Type': 'multipart/form-data' },-->
<!--              processData: false,-->
<!--              data: excelFormData,-->
<!--              success: (response) => {-->
<!--                  if (response === 'coool') {-->
<!--                      this.excelFileList = [];-->
<!--                      this.uploading = false;-->
<!--                      this.$message.success('tải lên thành công.');-->
<!--                  }-->
<!--              },-->
<!--              error: () => {-->
<!--                this.uploading = false;-->
<!--                this.$message.error('tải lên không thành công');-->
<!--              },-->
<!--          });-->
<!--      },-->
<!--    },-->
<!--  };-->
<!--</script>-->

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

