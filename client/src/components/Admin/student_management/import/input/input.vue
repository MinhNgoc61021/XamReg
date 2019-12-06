<template>
    <section id="create-user-form">
        <b-field label="MSSV"
            :type="{ 'is-danger': hasError }"
            :message="[
                { 'Hãy điền đầy đủ mã số sinh viên': hasError },
            ]">
            <b-input placeholder="Hãy nhập mã số sinh viên"></b-input>
        </b-field>

        <b-field label="Họ và tên"
            :type="{ 'is-danger': hasError }"
            :message="[
                { 'Hãy điền đầy đủ mật khẩu': hasError },
            ]">
            <b-input placeholder="Hãy nhập họ tên sinh viên"></b-input>
        </b-field>

        <b-field label="Ngày sinh"
            :type="{ 'is-danger': hasError }"
            :message="[
                { 'Hãy chọn ngày sinh': hasError },
            ]">
            <b-datepicker placeholder="Hãy nhập họ tên ngày sinh"></b-datepicker>
        </b-field>

        <b-field label="Khóa học"
            :type="{ 'is-danger': hasError }"
            :message="[
                { 'Hãy điền đầy đủ khóa học': hasError },
            ]">
            <b-input placeholder="Hãy nhập mã khóa học"></b-input>
        </b-field>

        <b-field label="Giới tính"
            :type="{ 'is-danger': hasError }"
            :message="[
                { 'Hãy chọn giới tính': hasError },
            ]">
            <b-select
                placeholder="Hãy chọn giới tính"
                expanded>
                <option value="Nam">Nam</option>
                <option value="Nữ">Nữ</option>
            </b-select>
        </b-field>
        <div class="buttons" style="float: right;">
          <b-button outlined>Tạo</b-button>
        </div>
    </section>
</template>
<script>
  export default {
      name: "input",
      data() {
          return {
              hasError: false
          };
      }
    }
</script>
<style scoped>
  #create-user-form {
    width: 70%;
    margin: auto;
  }
</style>


