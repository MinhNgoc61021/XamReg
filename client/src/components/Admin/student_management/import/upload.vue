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
                // send each file using axios
                // the loop is to put each file in to the formData
                // after every request, the formData will delete the file
                for (const file of this.dropFiles) {
                    formData.append('student_list_excel', file);
                    const loadingComponent = this.$buefy.loading.open({
                      container: this.isFullPage ? null : this.$refs.element.$el
                    });
                    try {
                        console.log(formData);
                      const excel_upload = await axios.post('/handling/upload', formData, {
                        headers: {
                          'Content-Type': 'multipart/form-data',
                          'Authorization': 'Bearer: ' + JSON.parse(localStorage.getItem('user')).token,
                        }
                      });
                      if (excel_upload.status === 200) {
                          loadingComponent.close();

                          this.$buefy.notification.open({
                              duration: 3000,
                              message: 'Dữ liệu sinh viên từ file ' + file.name + ' đã được tạo thành công!',
                              position: 'is-bottom-right',
                              type: 'is-success',
                          });
                      }
                    } catch (e) {
                        loadingComponent.close();
                        if (e['message'].includes('400')) {
                            this.$buefy.notification.open({
                              duration: 3000,
                              message: 'HTTP Status 400: Kiểm tra lại, dữ liệu bạn nhập trong file ' + file.name + ' đang có vấn đề!',
                              position: 'is-bottom-right',
                              type: 'is-danger',
                            })
                        }
                        else if (e['message'].includes('401')) {
                            this.$buefy.notification.open({
                              duration: 3000,
                              message: 'HTTP Status 401: Không được quyền sử dụng!',
                              position: 'is-bottom-right',
                              type: 'is-danger',
                            })
                        }
                    } finally {
                        formData.delete('student_list_excel')
                    }
                }
            }
        }
    }
</script>
