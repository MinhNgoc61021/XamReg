<template>
  <div class="container">
    <h1 class="title is-3">Thông tin chung</h1>
    <h2 class="subtitle is-6">Thông tin chung của sinh viên có MSSV <b>{{ this.student_info.ID }}</b></h2>
    <hr>
    <section>
        <b-tabs type="is-boxed">
            <b-tab-item label="Thông tin về sinh viên" icon="info-circle">
                <b-field label="Tài khoản">
                  <p>{{ student_info.Username }}</p>
                </b-field>
                <b-field label="Họ và tên">
                  <p>{{ student_info.Fullname }}</p>
                </b-field>
                <b-field label="Ngày sinh">
                  <p>{{ formatDate(student_info.Dob) }}</p>
                </b-field>
                <b-field label="Khóa học">
                  <p>{{ student_info.CourseID }}</p>
                </b-field>
                <b-field label="Giới tính">
                  <p>{{ student_info.Gender }}</p>
                </b-field>
                <b-loading :is-full-page="false" :active.sync="loading" :can-cancel="false"></b-loading>
            </b-tab-item>
        </b-tabs>
    </section>
  </div>
</template>

<script>
  import axios from 'axios';
  import moment from 'moment';
  import {authHeader} from "../api/jwt_handling";

    export default {
        name: "student-info",
        data() {
            return {
                student_info: {
                    ID: '',
                    Fullname: '',
                    Username: '',
                    Dob: '',
                    Gender: '',
                    CourseID: '',
                },
                loading: false,
            }
        },
        methods: {
            formatDate(date) {
                return date !== '' ? moment(date).format('L') : '';
            },
            async getStudentInfo() {
                this.loading = true;
                try {
                    const response = await axios({
                        url: '/shift-register/get-info',
                        headers: { 'Authorization': authHeader() },
                    });
                    // console.log(response);
                    let info_data = response.data.info;
                    this.student_info.ID = info_data.ID;
                    this.student_info.Username = info_data.Username;
                    this.student_info.Fullname = info_data.Fullname;
                    this.student_info.Gender = info_data.Gender;
                    this.student_info.Dob = info_data.Dob;
                    this.student_info.CourseID = info_data.CourseID;
                } catch (e) {
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: 'Không thể tìm được dữ liệu!',
                        position: 'is-bottom-right',
                        type: 'is-danger',
                        hasIcon: true
                    });
                } finally {
                    this.loading = false;
                }

            }
        },
        mounted() {
            this.getStudentInfo();
        }
    }
</script>

<style scoped>
</style>
