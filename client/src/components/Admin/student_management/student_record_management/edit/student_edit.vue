<template>
  <form @submit.prevent="updateStudentData()">
      <div class="modal-card" style="width: 450px;">
        <header class="modal-card-head">
            <p class="modal-card-title">Form chỉnh sửa</p>
        </header>
        <section class="modal-card-body">
          <b-field label="MSSV">
            <b-input
              type="text"
              v-model="newStudentID"
              :value="newStudentID"
              maxlength="8"
              validation-message="Nhập đúng MSSV"
              pattern="^\d{8}$"
              placeholder="Nhập mã số sinh viên"
              required>
            </b-input>
          </b-field>
          <b-field label="Tài khoản">
            <b-input
              type="email"
              v-model="newUsername"
              :value="newUsername"
              maxlength="19"
              pattern="^\d{8}@vnu.edu.vn$"
              validation-message="Nhập đúng tài khoản"
              placeholder="Sửa tài khoản"
              required>
            </b-input>
          </b-field>
          <b-field label="Họ và tên">
            <b-input
              type="text"
              v-model="newFullname"
              pattern="^[a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀẾỂưăạảấầẩẫậắằẳẵặẹẻẽềếểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\\s ]+$"
              validation-message="Nhập đúng họ và tên"
              :value="newFullname"
              placeholder="Sửa họ và tên"
              required>
            </b-input>
          </b-field>
          <b-field label="Mã khóa học">
            <b-input
              type="text"
              v-model="newCourseID"
              pattern="(^[K|k][1-9][0-9][A-Za-z]+[1-9]*)"
              validation-message="Nhập đúng khóa học"
              :value="newCourseID"
              placeholder="Sửa mã khóa học"
              required>
            </b-input>
          </b-field>
          <b-field label="Ngày sinh">
            <b-datepicker
              placeholder="Chọn ngày sinh"
              v-model="newDob"
              :value="newDob"
              required>
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
          <button class="button is-primary" type="submit" @submit="closeModal()">Cập nhật</button>
        </footer>
      </div>
  </form>
</template>


<script>
  import axios from 'axios';
  import { authHeader } from "../../../../api/jwt_handling";
  import moment from 'moment/moment';

  export default {
      name: "edit_student_modal_form",
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
                      url: '/student/update-student-record',
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
                      this.$emit('editStatus', 200);
                      this.$parent.close();
                  }
                  else {
                      this.$emit('editStatus', 202);
                  }
              } catch (e) {
                  if (e['message'].includes('400')) {
                      this.$emit('editStatus', 400);
                  }
                  else if (e['message'].includes('401')) {
                      this.$emit('editStatus', 401);
                  }
              } finally {

              }
          },
      },
    }
</script>
<style scoped>

</style>
