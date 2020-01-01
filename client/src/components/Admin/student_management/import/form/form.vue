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
                     pattern="^[a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀẾỂưăạảấầẩẫậắằẳẵặẹẻẽềếểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\\s ]+$"
                     required>
            </b-input>
        </b-field>

        <b-field label="Ngày sinh">
            <b-datepicker v-model="newStudent.Dob"
                          validation-message="Chọn đúng ngày sinh"
                          placeholder="Hãy nhập họ tên ngày sinh" required></b-datepicker>
        </b-field>

        <b-field label="Khóa học">
            <b-input v-model="newStudent.CourseID" placeholder="Hãy nhập mã khóa học"
                     validation-message="Nhập đúng khóa học"
                     pattern="(^[K|k][1-9][0-9][A-Za-z]+[1-9]*)"
                     required>
            </b-input>
        </b-field>

        <b-field label="Giới tính">
            <b-select v-model="newStudent.Gender"
                      placeholder="Hãy chọn giới tính"
                      validation-message="Chọn đúng giới tính"
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
  import lodash from 'lodash.debounce';
  import moment from 'moment/moment';
  import { eventBus } from "../../../../../main";

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
                     url: '/student/create-student-record',
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
                  if (response.data.status === 'success') {
                      this.newStudent.StudentID = '';
                      this.newStudent.Fullname = '';
                      this.newStudent.Gender = '';
                      this.newStudent.Dob = null;
                      this.newStudent.CourseID = '';
                      this.$buefy.notification.open({
                          duration: 2000,
                          message: `Dữ liệu sinh viên có MSSV: ${this.newStudent.StudentID} đã được tạo thành công!`,
                          position: 'is-bottom-right',
                          type: 'is-success',
                          hasIcon: true
                      });
                      eventBus.$emit('up-to-date', '');
                  }
                  else {
                      this.$buefy.notification.open({
                          duration: 2000,
                          message: `Dữ liệu sinh viên có MSSV: <b>${this.newStudent.StudentID}</b> đã tồn tại trước đó!`,
                          position: 'is-bottom-right',
                          type: 'is-warning',
                          hasIcon: true
                      });
                  }
              } catch (e) {
                  if (e['message'].includes('400')) {
                      this.$buefy.notification.open({
                          duration: 2000,
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


