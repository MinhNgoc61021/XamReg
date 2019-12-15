<template>
    <div>
      <a-input-search
        placeholder="Nhập mã số sinh viên"
        @search="onSearch"
        enterButton="Tìm kiếm"
        size="large"
        style="width:300px"
      />

      <br>

      <a-form :form="form" @submit="handleSubmit">
        <a-form-item label="Tên sinh viên">
          <p>
            <a-input
              v-decorator="[
            'student_id',
            {
              rules: [{ required: true, message: 'Username is required!' }],
            },
          ]"
              v-model="student_name"
              style="width:200px"
            />
          </p>
        </a-form-item>

        <a-form-item label="Mã số sinh viên">
          <a-input
            v-decorator="[
            'student_id',
            {
              rules: [{ required: true, message: 'Username is required!' }],
            },
          ]"
            v-model="student_id"
            style="width:200px"
          />
        </a-form-item>

        <a-form-item label="Ngày sinh">
          <a-input
            v-decorator="[
            'username',
            {
              rules: [{ required: true, message: 'Username is required!' }],
            },
          ]"
            v-model="dob"
            style="width:200px"
          />
        </a-form-item>

        <a-form-item label="Khóa, ngành">
          <a-input
            v-decorator="[
            'username',
            {
              rules: [{ required: true, message: 'Username is required!' }],
            },
          ]"
            style="width:200px"
          />
        </a-form-item>

        <a-form-item>
          <a-menu
            @click="handleClick"
            :defaultSelectedKeys="['1']"
            :openKeys.sync="openKeys"
            mode="inline">
            <!--<a-sub-menu key="sub1" title="Danh sách môn thi" >-->
            <a-menu-item v-for="exam_info in exam_infos"  v-bind="exam_info.id">
              {{exam_info.name}}
              <a-select defaultValue="exam_schedul" @change="handleChange" style="width: 220px" v-model="exam_schedul">
                <a-select-option v-for="value in exam_info.sche" value="value">{{value}}</a-select-option>
              </a-select>
            </a-menu-item>
            <!--</a-sub-menu>-->
          </a-menu>
        </a-form-item>
      </a-form>

      <a-button type="primary" htmp-type="submit" style="margin-left:5px; float:right">
        Cancel
      </a-button>

      <a-button type="primary" html-type="submit" style="float:right">
        Submit
      </a-button>
    </div>
</template>

<script>
    export default {
        name:"Student_edit_info",
        data() {
            return {
                  student_name: "Lê phê đô",
                  student_id: "0129312",
                  dob: "??",
                  class: "???",
                  exam_schedul: "Phòng 100-G2 1/1/2020",
                  exam_infos: [
                      {
                          id: 1,
                          name: "Tín hiệu hệ thống",
                          sche: ["Phòng 308-G2 1/1/2020","Phòng 318-G2 1/1/2020","Phòng 338-G2 1/1/2020"]
                      },
                      {
                          id: 2,
                          name: "Quản lý dự án",
                          sche: ["Phòng 308-G2 1/1/2020","Phòng 318-G2 1/1/2020","Phòng 338-G2 1/1/2020"]
                      },
                      {
                          id: 3,
                          name: "Lập trình web",
                          sche: ["Phòng 308-G2 1/1/2020","Phòng 318-G2 1/1/2020","Phòng 338-G2 1/1/2020"]
                      },
                  ],
            }
          },
          methods: {
          },
      }
</script>

<style scoped>

</style>
