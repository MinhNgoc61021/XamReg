<template>
  <div class="clearfix">
    <a-upload :fileList="excelFileList" :remove="handleRemove" :beforeUpload="beforeUpload">
      <a-button> <a-icon type="upload" /> Chọn Tệp Excel </a-button>
    </a-upload>
    <a-button
      type="primary"
      @click="handleUpload"
      :disabled="excelFileList.length === 0"
      :loading="uploading"
      style="margin-top: 16px">
      {{uploading ? 'Đang tải' : 'Tải lên' }}
    </a-button>
  </div>
</template>
<script>
  import axios from 'axios';
  export default {
    data() {
      return {
        excelFileList: [],
        uploading: false,
      };
    },
    methods: {
        handleRemove: function (file) {
          const index = this.excelFileList.indexOf(file);
          const newFileList = this.excelFileList.slice();
          newFileList.splice(index, 1);
          this.excelFileList = newFileList;
        },
        beforeUpload: function (file) {
          this.excelFileList = [...this.excelFileList, file];
          return false;
        },
        handleUpload: function () {
          const { excelFileList } = this;
          const excelFormData = new FormData();
          excelFormData.append('student_list_excel', excelFileList[0]);
          this.uploading = true;
          axios({
              url: '/handling/upload',
              method: 'post',
              headers: { 'Content-Type': 'multipart/form-data' },
              processData: false,
              data: excelFormData,
              success: (response) => {
                  if (response === 'coool') {
                      this.excelFileList = [];
                      this.uploading = false;
                      this.$message.success('tải lên thành công.');
                  }
              },
              error: () => {
                this.uploading = false;
                this.$message.error('tải lên không thành công');
              },
          });
      },
    },
  };
</script>
