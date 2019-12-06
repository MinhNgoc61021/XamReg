<template>

</template>
<script>
    import axios from 'axios';
    import { authHeader } from "../../../../api/jwt_handling";

    export default {
        props: ['StudentID'],
        name: "subject_status",
        data() {
            return {
                student_subject_record: [],
                total: 0,
                loading: false,
                sortField: 'Subject',
                sortOrder: 'desc',
                defaultSortOrder: 'desc',
                page: 1,
                per_page: 5,
                ID_Search: '',
                studentID: this.StudentID,
                status_type: 'Qualified'
            }
        },
        methods: {
            onPageChange() {

            },
            onSort() {

            },
            onDelete() {

            },
            onEdit() {

            },
            async getSubject() {
                this.loading = true;
                try {
                    const response = await axios({
                        url: '/record/student-subject-records',
                        params: {
                            page_index: this.page,
                            per_page: this.per_page,
                            sort_field: this.sortField,
                            sort_order: this.sortOrder,
                            currentStudentID: this.studentID,
                            type: this.status_type,
                        },
                        headers: {
                            'Authorization': authHeader(),
                        }
                    });
                    if (response.status === 200) {
                        console.log(response.data);
                    }
                } catch (error) {
                    this.student_subject_record = [];
                    this.total = 0;
                    this.loading = false;
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: `Không thể lấy được dữ liệu môn học của sinh viên có MSSV ${this.studentID} này!`,
                        position: 'is-bottom-right',
                        type: 'is-danger',
                    });
                    throw error
                }
            },
            mounted() {
                this.getSubject();
            }
        },
    }
</script>
