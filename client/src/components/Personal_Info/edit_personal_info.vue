<template>
  <form @submit.prevent="updateStudentData()">
      <div class="modal-card" style="width: 450px;">
        <header class="modal-card-head">
            <p class="modal-card-title">Form chỉnh sửa</p>
        </header>
        <section class="modal-card-body">
          <b-field label="ID">
            <b-input
              type="text"
              v-model="newID"
              :value="newID"
              placeholder="Nhập ID"
              required>
            </b-input>
          </b-field>
          <b-field label="Tài khoản">
            <b-input
              type="email"
              v-model="newUsername"
              :value="newUsername"
              placeholder="Sửa tài khoản"
              required>
            </b-input>
          </b-field>
          <b-field label="Mật khẩu">
            <b-input
              type="email"
              v-model="newUsername"
              :value="newUsername"
              placeholder="Sửa tài khoản"
              required>
            </b-input>
          </b-field>
          <b-field label="Họ và tên">
            <b-input
              type="text"
              v-model="newFullname"
              :value="newFullname"
              placeholder="Sửa họ và tên"
              required>
            </b-input>
          </b-field>
          <b-field label="Mã khóa học">
            <b-input
              type="text"
              v-model="newCourseID"
              :value="newCourseID"
              placeholder="Sửa mã khóa học"
              required>
            </b-input>
          </b-field>
          <b-field label="Ngày sinh">
            <b-datepicker
              placeholder="Chọn ngày sinh"
              v-model="newDob"
              :value="newDob" required>
            </b-datepicker>
          </b-field>
          <b-field label="Giới tính">
            <b-select placeholder="Chọn giới tính" v-model="newGender" :value="newGender" required>
              <option value="Nam">Nam</option>
              <option value="Nữ">Nữ</option>
            </b-select>
          </b-field>
        </section>

        <footer class="modal-card-foot">
          <button class="button" type="button" @click="$parent.close()">Bỏ qua</button>
          <button class="button is-primary" type="submit">Cập nhật</button>
        </footer>
      </div>
  </form>
</template>


<script>
  import axios from 'axios';
  import moment from 'moment/moment';
  import {authHeader} from "../api/jwt_handling";

  export default {
      name: "edit_student_form",
      props: ['currentStudentID','currentFullname', 'currentUsername', 'currentCourseID' , 'currentDob', 'currentGender'],
      data() {
          return {
              newStudentID: this.currentStudentID,
              newFullname: this.currentFullname,
              newUsername: this.currentUsername,
              newCourseID: this.currentCourseID,
              newDob: this.currentDob,
              newGender: this.currentGender,
          }
      },
      methods: {
          async updateStudentData() {
              try {
                  // console.log(moment(this.newDob).format('MM/DD/YYYY'));
                  const update = await axios({
                      method: 'put',
                      url: '/record/update-student-record',
                      headers: {
                          'Authorization': authHeader(),
                      },
                      data: {
                          currentStudentID: this.currentStudentID,
                          StudentID: this.newStudentID,
                          Fullname: this.newFullname,
                          Username: this.newUsername,
                          CourseID: this.newCourseID,
                          Dob: moment(this.newDob).format('YYYY-MM-DD'),
                          Gender: this.newGender,
                      },
                  });
                  if (update.status === 200) {
                      this.$parent.close();
                      this.$buefy.notification.open({
                          duration: 2000,
                          message: `Đã cập nhật tài khoản của sinh viên có MSSV: <b>${this.newStudentID}</b> thành công.`,
                          position: 'is-bottom-right',
                          type: 'is-success',
                      });
                  }
              } catch (e) {
                  if (e['message'].includes('400')) {
                      this.$buefy.notification.open({
                          duration: 2000,
                          message: 'HTTP Status 400: Kiểm tra lại, dữ liệu bạn nhập đang không đúng!',
                          position: 'is-bottom-right',
                          type: 'is-danger',
                      });
                  }
                  else if (e['message'].includes('401')) {
                      this.$buefy.notification.open({
                          duration: 2000,
                          message: 'HTTP Status 401: Không được quyền sử dụng!',
                          position: 'is-bottom-right',
                          type: 'is-danger',
                      });
                  }
              }
          },
      },
    }
</script>
<style scoped>

</style>
