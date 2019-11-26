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
        <div class="tags" style="max-width: 350px;">
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
                for (const element of this.dropFiles) {
                    formData.append('student_list_excel', element);
                    const loadingComponent = this.$buefy.loading.open({
                      container: this.isFullPage ? null : this.$refs.element.$el
                    });
                    try {
                      const excel_upload = await axios.post('/handling/upload', formData, {
                        headers: {
                          'Content-Type': 'multipart/form-data',
                          'Authorization': 'Bearer: ' + JSON.parse(localStorage.getItem('user')).token,
                        }
                      });
                      if (excel_upload.status === 200) {
                          loadingComponent.close();
                          this.dropFiles = [];
                          this.$buefy.notification.open({
                              duration: 3000,
                              message: 'Dữ liệu sinh viên đã được tạo thành công!',
                              position: 'is-top-right',
                              type: 'is-success',
                          });
                      }
                    } catch (e) {
                        loadingComponent.close();
                        if (e['message'].includes('400')) {
                            this.$buefy.notification.open({
                              duration: 3000,
                              message: 'Lỗi 400: Dữ liệu bạn nhập đang có vấn đề!',
                              position: 'is-top-right',
                              type: 'is-danger',
                            })
                        }
                    }
                }
            }
        }
    }
</script>
