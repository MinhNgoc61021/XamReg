<template>
    <section id="create-user-form">
      <form @submit.prevent="submitNewStudent">
        <b-field label="MSSV">
            <b-input v-model="newStudent.StudentID" placeholder="Hãy nhập mã số sinh viên"
                     required maxlength="8"
                     validation-message="Nhập đúng MSSV"
                     pattern="^\d{8}$">
            </b-input>
        </b-field>

        <b-field label="Họ và tên">
            <b-input v-model="newStudent.Fullname" placeholder="Hãy nhập họ và tên sinh viên"
                     validation-message="Nhập đúng họ và tên"
                     patterns="[a-zA-Z]+"
                     required>
            </b-input>
        </b-field>

        <b-field label="Ngày sinh">
            <b-datepicker v-model="newStudent.Dob" placeholder="Hãy nhập họ tên ngày sinh" required></b-datepicker>
        </b-field>

        <b-field label="Khóa học">
            <b-input v-model="newStudent.CourseID" placeholder="Hãy nhập mã khóa học"
                     validation-message="Nhập đúng khóa học"
                     patterns="(^[K|k][1-9][0-9][A-Za-z]+[1-9]*)"
                     required>
            </b-input>
        </b-field>

        <b-field label="Giới tính">
            <b-select v-model="newStudent.Gender"
                placeholder="Hãy chọn giới tính"
                expanded required>
                <option value="Nam">Nam</option>
                <option value="Nữ">Nữ</option>
            </b-select>
        </b-field>
          <div class="buttons" style="float: right;">
            <button class="button" type="submit" outlined>Tạo</button>
          </div>
      </form>
    </section>
</template>
<script>
  import axios from 'axios';
  import {authHeader} from "../../../../api/jwt_handling";
  import moment from 'moment/moment';

  export default {
      name: "form",
      data() {
          return {
              hasError: false,
              newStudent: {
                  StudentID: '',
                  Fullname: '',
                  CourseID: '',
                  Dob: null,
                  Gender: '',
              }
          }
      },
      methods: {
          async submitNewStudent() {
              try {
                  const response = await axios({
                     url: '/record/create-student-record',
                     method: 'post',
                     headers: {
                        'Authorization': authHeader(),
                     },
                     data: {
                         newStudentID: this.newStudent.StudentID,
                         newFullname: this.newStudent.Fullname,
                         newCourseID: this.newStudent.CourseID,
                         newDob: moment(this.newStudent.Dob).format('YYYY-MM-DD'),
                         newGender: this.newStudent.Gender,
                     }
                  });
                  if (response.status === 200) {
                      if (response.data.status === 'success') {
                          this.$buefy.notification.open({
                              duration: 2500,
                              message: `Dữ liệu sinh viên có MSSV: ${this.newStudent.StudentID} đã được tạo thành công!`,
                              position: 'is-bottom-right',
                              type: 'is-success',
                              hasIcon: true
                          });
                      }
                      else {
                          this.$buefy.notification.open({
                              duration: 2500,
                              message: `Dữ liệu sinh viên có MSSV: ${this.newStudent.StudentID} đã tồn tại trước đó!`,
                              position: 'is-bottom-right',
                              type: 'is-warning',
                              hasIcon: true
                          });
                      }
                  }
              } catch (e) {
                  if (e['message'].includes('400')) {
                      this.$buefy.notification.open({
                          duration: 2500,
                          message: `Kiểm tra lại, dữ liệu bạn nhập đang có vấn đề!`,
                          position: 'is-bottom-right',
                          type: 'is-danger',
                          hasIcon: true
                      })
                  }
                  else {
                      this.$buefy.notification.open({
                          duration: 2500,
                          message: `Không thể tạo được dữ liệu!`,
                          position: 'is-bottom-right',
                          type: 'is-danger',
                          hasIcon: true
                      })
                  }
              }
          },
      },
    }
</script>
<style scoped>
  #create-user-form {
    width: 70%;
    margin: auto;
  }
</style>


