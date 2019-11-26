<template>
    <section id="create-user-form">
        <b-field label="MSSV">
            <b-input placeholder="Hãy nhập mã số sinh viên"></b-input>
        </b-field>

        <b-field label="Họ và tên">
            <b-input placeholder="Hãy nhập họ tên sinh viên"></b-input>
        </b-field>

        <b-field label="Ngày sinh">
            <b-datepicker placeholder="Hãy nhập họ tên ngày sinh"></b-datepicker>
        </b-field>

        <b-field label="Khóa học">
            <b-input placeholder="Hãy nhập mã khóa học"></b-input>
        </b-field>

        <b-field label="Giới tính">
            <b-select
                placeholder="Hãy chọn giới tính"
                expanded>
                <option value="Nam">Nam</option>
                <option value="Nữ">Nữ</option>
            </b-select>
        </b-field>
        <div class="buttons" style="float: right;">
          <b-button outlined>Thêm</b-button>
        </div>
    </section>
</template>
<script>
  export default {
        name: "input",
    }
</script>
<style scoped>
  #create-user-form {
    width: 70%;
    margin: auto;
  }
</style>
