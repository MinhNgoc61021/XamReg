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
                        <p>Chọn hoặc kéo thả file <b-icon icon="file-excel"></b-icon> Excel (.xlsx) của bạn để tải lên</p>
                    </div>
                </section>
            </b-upload>
        </b-field>
        <b-field>
            <div class="buttons" id="button-list">
              <b-button id="on-upload-btn" @click="uploadExcelFile()" v-if="dropFiles.length !== 0" outlined>Tạo</b-button>
              <b-button id="unable-upload-btn" @click="uploadExcelFile()" v-else disabled outlined>Tạo</b-button>
            </div>
        </b-field>
        <div class="tags" style="max-width: 350px;">
            <span v-for="(file, index) in dropFiles"
                :key="index"
                class="tag is-primary" >
                {{ file.name }}
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
    import { authHeader } from "../../../../api/jwt_handling";
    import { eventBus } from "../../../../../main";

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
                      const excel_upload = await axios.post('https://xamreg-uet-vnu-edu.herokuapp.com/handling/upload', formData, {
                        headers: {
                          'Content-Type': 'multipart/form-data',
                          'Authorization': authHeader(),
                        }
                      });
                      if (excel_upload.status === 200) {
                          loadingComponent.close();

                          this.$buefy.notification.open({
                              duration: 2500,
                              message: `Dữ liệu sinh viên từ file <b>${file.name}</b> đã được tạo thành công!`,
                              position: 'is-bottom-right',
                              type: 'is-success',
                              hasIcon: true
                          });
                      }
                    } catch (e) {
                        loadingComponent.close();
                        console.log(e);
                        if (e['message'].includes('400')) {
                            this.$buefy.notification.open({
                                duration: 2500,
                                message: `Kiểm tra lại, dữ liệu bạn nhập trong file <b>${file.name}</b> đang có vấn đề!`,
                                position: 'is-bottom-right',
                                type: 'is-danger',
                                hasIcon: true
                            })
                        }
                        else if (e['message'].includes('401')) {
                            this.$buefy.notification.open({
                                duration: 2500,
                                message: 'Không được quyền sử dụng!',
                                position: 'is-bottom-right',
                                type: 'is-danger',
                                hasIcon: true
                            })
                        }
                        else if (e['message'].includes('403')) {
                            this.$buefy.notification.open({
                                duration: 2500,
                                message: `File <b>${file.name}</b> có MSSV chưa tồn tại trong hệ thống!<br> <b>Chú ý</b>: Đối với nhập danh sách tình trạng môn thi của sinh viên, hãy đảm bảo là tài khoản của sinh viên đó đã tồn tại sẵn!`,
                                position: 'is-bottom-right',
                                type: 'is-warning',
                                hasIcon: true
                            })
                        }
                        else {
                            this.$buefy.notification.open({
                                duration: 2500,
                                message: 'Lỗi không thể tải file lên hệ thống!',
                                position: 'is-bottom-right',
                                type: 'is-danger',
                                hasIcon: true
                            })
                        }
                    } finally {
                        formData.delete('student_list_excel');
                        eventBus.$emit('up-to-date', '')
                    }
                }
            }
        }
    }
</script>
<style scoped>
  #button-list {
    float: right;
  }
  @media screen and (max-width: 650px) {
    #button-list {
      float: none;
    }
    #on-upload-btn, #unable-upload-btn {
      width: 100%;
      display: block;
      margin: auto;
    }
  }
</style>
