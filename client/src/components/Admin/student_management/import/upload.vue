<!--<template>-->
<!--  <div id="dragger-container">-->
<!--    <a-upload-dragger-->
<!--    name="student_list_excel"-->
<!--    :multiple="false"-->
<!--    action="/handling/upload"-->
<!--    :headers="headers"-->
<!--    @change="handleChange">-->
<!--      <p class="ant-upload-drag-icon">-->
<!--        <a-icon type="inbox" />-->
<!--      </p>-->
<!--      <p class="ant-upload-text">Chọn hoặc kéo thả file của bạn để tải lên</p>-->
<!--      <p class="ant-upload-hint">-->
<!--        Hỗ trợ tải một hoặc nhiều file <a-icon type="file-excel" /> Excel.-->
<!--        <strong>(Hãy dùng định dạng .xlsx)</strong>-->
<!--      </p>-->
<!--    </a-upload-dragger>-->
<!--  </div>-->
<!--</template>-->
<!--<script>-->
<!--  import { authHeader } from "../../../api/jwt_handling";-->
<!--  export default {-->
<!--    data() {-->
<!--      return {-->
<!--          upload_status: '',-->
<!--          headers: authHeader(),-->
<!--      }-->
<!--    },-->
<!--    methods: {-->
<!--      handleChange(info) {-->
<!--        const status = info.file.status;-->
<!--        if (status !== 'uploading') {-->
<!--            console.log(info.file, info.fileList);-->
<!--        }-->
<!--        if (status === 'done') {-->
<!--            this.$message.success(`${info.file.name} đã được tải lên và dữ liệu được thành công.`);-->
<!--        }-->
<!--        else if (status === 'error') {-->
<!--            this.$message.error(`${info.file.name} không được tải lên thành công hoặc có lỗi trong file.`);-->
<!--        }-->
<!--      },-->
<!--    },-->
<!--  };-->
<!--</script>-->
<!--<style scoped>-->
<!--  #dragger-container {-->
<!--    margin: auto;-->
<!--    width: 70%;-->
<!--    left: 15%;-->
<!--    position: absolute;-->
<!--    top: 20%;-->
<!--  }-->
<!--</style>-->

<template>
  <section>
        <b-field>
            <b-upload v-model="dropFiles"
                multiple
                drag-drop ref="element">
                <section class="section">
                    <div class="content has-text-centered">
                        <p>
                            <b-icon
                                icon="upload"
                                size="is-large">
                            </b-icon>
                        </p>
                        <p>Chọn hoặc kéo thả file Excel (.xlsx) của bạn để tải lên</p>
                    </div>
                </section>
            </b-upload>
        </b-field>
        <b-field>
            <div class="buttons" style="float: right;">
              <b-button @click="uploadExcelFile()" outlined>Nhập</b-button>
            </div>
        </b-field>
        <div class="tags">
            <span v-for="(file, index) in dropFiles"
                :key="index"
                class="tag is-primary" >
                {{file.name}}
                <button class="delete is-small"
                    type="button"
                    @click="deleteDropFile(index)">
                </button>
            </span>
        </div>
    </section>
</template>

<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                dropFiles: [],
            }
        },
        methods: {
            deleteDropFile(index) {
                this.dropFiles.splice(index, 1)
            },
            async uploadExcelFile() {
                let formData = new FormData();
                formData.append('student_list_excel', this.dropFiles[0]);
                const loadingComponent = this.$buefy.loading.open({
                    container: this.isFullPage ? null : this.$refs.element.$el
                });
                const excel_upload = await axios.post('/handling/upload', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                        'Authorization': 'Bearer: ' + JSON.parse(localStorage.getItem('user')).token,
                    }
                });
                console.log(excel_upload);
                loadingComponent.close();

            }

        }
    }
</script>
