<template>
    <section>
        <b-field grouped group-multiline>
            <b-button
              :class="{'is-loading': student.loading}"
              class="button"
              @click="getStudentRecordData"
            >
              <b-icon
                size="is-small"
                icon="sync"/>
              <span>Làm mới</span>
            </b-button>
            <b-select v-model="student.per_page">
              <option value="5">5 dòng/trang</option>
              <option value="10">10 dòng/trang</option>
              <option value="15">15 dòng/trang</option>
              <option value="20">20 dòng/trang</option>
            </b-select>
            <b-autocomplete
                v-model="student.ID_Search"
                placeholder="Tìm kiếm theo MSSV"
                icon="search"
                expanded>
            </b-autocomplete>
        </b-field>
        <b-table
            :data="student.student_record"
            :loading="student.loading"
            paginated
            backend-pagination
            detailed
            :total="student.total"
            :per-page="student.per_page"
            @page-change="onStudentPageChange"
            aria-next-label="Next page"
            aria-previous-label="Previous page"
            aria-page-label="Page"
            aria-current-label="Current page"
            backend-sorting
            hoverable
            detail-key="ID"
            :opened-detailed="student_status.ID_Index"
            :default-sort-direction="student.defaultSortOrder"
            :default-sort="[student.sortField, student.sortOrder]"
            @sort="onStudentSort"
            @details-open="(row, index) => { getSubject(row); closeOtherDetails(row, index) }"
            @details-close="(row, index) => { student_status.student_subject_record = [] }"
            :show-detail-icon="true">

            <template slot-scope="props">
                <b-table-column field="ID" label="MSSV" sortable>
                    {{ props.row.ID }}
                </b-table-column>

                <b-table-column field="Fullname" label="Họ và tên" sortable>
                     {{ props.row.Fullname }}
                </b-table-column>

                <b-table-column field="Username" label="Tài khoản" sortable>
                    {{ props.row.Username }}
                </b-table-column>

                <b-table-column field="Dob" label="Ngày sinh" sortable>
                    <span class="tag is-success">
                     {{ formatDate(props.row.Dob) }}
                    </span>
                </b-table-column>

                <b-table-column field="CourseID" label="Khóa" sortable>
                     {{ props.row.CourseID }}
                </b-table-column>

                <b-table-column field="Role_Type" label="Quyền" sortable>
                     {{ props.row.Role_Type }}
                </b-table-column>

                <b-table-column field="Gender" label="Giới tính" sortable>
                     <span>
                        <b-icon pack="fas"
                            :icon="props.row.Gender === 'Nam' ? 'mars' : 'venus'">
                        </b-icon>
                        {{ props.row.Gender }}
                    </span>
                </b-table-column>

                <b-table-column field="Action" width="90">
                    <b-button type="is-warning" size="is-small" icon-pack="fas" icon-right="edit" outlined @click.prevent="onStudentEdit(props.row)"></b-button>
                    <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onStudentDelete(props.row.ID)"></b-button>
                </b-table-column>
            </template>

                <template slot="detail" slot-scope="props">
                  <b-field grouped group-multiline>
                      <b-button
                      :class="{'is-loading': student_status.loading}"
                      class="button"
                      @click="getSubject(props.row)"
                    >
                      <b-icon
                        size="is-small"
                        icon="sync"/>
                    </b-button>
                    <b-select v-model="student_status.status_type">
                      <option value="Qualified" >Đủ điều kiện thi</option>
                      <option value="Unqualified">Không đủ điều kiện thi</option>
                    </b-select>
                  </b-field>
                <b-field v-if="student_status.student_subject_record.length > 0" grouped group-multiline>
                    <b-table
                        :data="student_status.student_subject_record"
                        :loading="student_status.loading"
                        paginated
                        backend-pagination
                        :total="student_status.total"
                        :per-page="student_status.per_page"
                        @page-change="onStatusPageChange"
                        aria-next-label="Next page"
                        aria-previous-label="Previous page"
                        aria-page-label="Page"
                        aria-current-label="Current page"
                        backend-sorting
                        bordered
                        narrowed
                        hoverable
                        detail-key="ID"
                        :default-sort-direction="student_status.defaultSortOrder"
                        :default-sort="[student_status.sortField, student_status.sortOrder]"
                        @sort="onStatusSort">

                        <template slot-scope="props">
                            <b-table-column field="ID" label="Mã môn" sortable>
                                {{ props.row.SubjectID }}
                            </b-table-column>

                            <b-table-column field="Fullname" label="Tên môn" sortable>
                                 {{ props.row.SubjectTitle }}
                            </b-table-column>

                            <b-table-column field="Action">
                                <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onStatusDelete(props.row.StudentID, props.row.SubjectID)"></b-button>
                            </b-table-column>
                        </template>
                    </b-table>
                </b-field>
                <b-field v-else>
                  <b-message type="is-danger" has-icon>
                    Hiện tại sinh viên này chưa có thông tin về danh sách này, bạn hãy tải lên file <b-icon icon="file-excel"></b-icon> Excel định dạng <b>.xlsx</b> ở phần <b>Nhập (Import)</b>!
                  </b-message>
                </b-field>
            </template>
        </b-table>
    </section>
</template>

<script>
    import axios from 'axios'
    import { authHeader } from "../../../api/jwt_handling";
    import moment from 'moment/moment';
    import edit_student_form from "./edit/editStudent_modal_form";
    /*
     student edit data form
    */
    export default {
        components: {
            edit_student_form,
        },
        data() {
            return {
                student: {
                    student_record: [],
                    total: 0,
                    loading: false,
                    sortField: 'ID',
                    sortOrder: 'desc',
                    defaultSortOrder: 'desc',
                    page: 1,
                    per_page: 5,
                    ID_Search: '',
                },
                student_status: {
                    student_subject_record: [],
                    total: 0,
                    loading: false,
                    sortField: 'SubjectID',
                    sortOrder: 'desc',
                    defaultSortOrder: 'desc',
                    page: 1,
                    per_page: 5,
                    ID_Search: '',
                    status_type: 'Qualified',
                    ID_Index: [],
                }
            }
        },
        methods: {
            /*
             * Change formatDate
            */
            formatDate(date) {

                return moment(date).format('MM/DD/YYYY');
            },
            /*
             * Load async record data
            */
            async getStudentRecordData() {
                this.student.loading = true;
                try {
                    const response = await axios({
                        url: '/record/student-records',
                        params: {
                            page_index: this.student.page,
                            per_page: this.student.per_page,
                            sort_field: this.student.sortField,
                            sort_order: this.student.sortOrder
                        },
                        headers: {
                            'Authorization': authHeader(),
                        }
                    });
                    if (response.status === 200) {
                        this.student.student_record = [];
                        this.student.total = response.data.total_results;
                        response.data.records.forEach((item) => {
                            this.student.student_record.push(item);
                        });
                        // console.log(this.data);
                        this.student.loading = false
                    }
                } catch (error) {
                    this.student.student_record = [];
                    this.student.total = 0;
                    this.loading = false;
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: 'Không thể lấy được dữ liệu bảng!',
                        position: 'is-bottom-right',
                        type: 'is-danger',
                    });
                    throw error;

                }
            },
            /*
              * Handle page-change event
            */
            onStudentPageChange(page) {
                this.student.page = page;
                this.getStudentRecordData();
            },
            /*
              * Handle sort event
            */
            onStudentSort(field, order) {
                this.student.sortField = field;
                this.student.sortOrder = order;
                this.getStudentRecordData();
            },
            /*
              * Handle delete record event
            */
            async onStudentDelete(recordID) {
                this.$buefy.dialog.confirm({
                    title: 'Xóa tài khoản',
                    message: `Bạn có chắc chắn là muốn <b>xóa</b> tài khoản của sinh viên có MSSV ${recordID} này không? Đã làm thì tự chịu đấy.`,
                    confirmText: 'Xóa!',
                    cancelText: 'Bỏ qua',
                    type: 'is-danger',
                    hasIcon: true,
                    onConfirm: async () => {
                        try {
                            const removeData = await axios({
                                url: '/record/remove-record',
                                method: 'delete',
                                headers: {
                                    'Authorization': authHeader(),
                                },
                                data: {
                                    StudentID: recordID,
                                },
                            });
                            if (removeData.status === 200) {
                                this.$buefy.notification.open({
                                  duration: 2000,
                                  message: `Đã xóa tài khoản có MSSV <b>${recordID}</b> thành công.`,
                                  position: 'is-bottom-right',
                                  type: 'is-success',
                                });
                            }
                            this.getStudentRecordData();
                        } catch (e) {
                            if (e['message'].includes('401')) {
                                this.$buefy.notification.open({
                                  duration: 2000,
                                  message: 'HTTP Status 401: Không được quyền sử dụng!',
                                  position: 'is-bottom-right',
                                  type: 'is-danger',
                                })
                            }
                        }
                    },
                });
            },
            closeOtherDetails(row) {
                this.student_status.ID_Index = [row.ID];
                console.log(this.student_status.ID_Index);
            },
            onStudentEdit(record) {
                // console.log(record.Dob);
                // console.log(new Date(moment(record.Dob).format('MM/DD/YYYY')));
                this.$buefy.modal.open({
                    parent: this,
                    component: edit_student_form,
                    props: {
                        currentStudentID: record.ID,
                        currentFullname: record.Fullname,
                        currentUsername: record.Username,
                        currentCourseID: record.CourseID,
                        currentDob: new Date(moment(record.Dob).format('MM/DD/YYYY')),
                        currentGender: record.Gender,
                    },
                    hasModalCard: true,
                    customClass: 'custom-class custom-class-2',
                });
            },
            /*
              * Type style in relation to the value
            */
            type(value) {
                const number = parseFloat(value);
                if (number < 6) {
                    return 'is-danger'
                } else if (number >= 6 && number < 8) {
                    return 'is-warning'
                } else if (number >= 8) {
                    return 'is-success'
                }
            },
            onStatusPageChange() {

            },
            onStatusSort() {

            },
            onStatusDelete() {

            },
            onStatusEdit() {

            },
            async getSubject(row, index) {
                this.student_status.loading = true;
                console.log(this.student_status.ID_Index);
                try {
                    const response = await axios({
                        url: '/record/student-subject-records',
                        params: {
                            page_index: this.student_status.page,
                            per_page: this.student_status.per_page,
                            sort_field: this.student_status.sortField,
                            sort_order: this.student_status.sortOrder,
                            currentStudentID: row.ID,
                            type: this.student_status.status_type,
                        },
                        headers: {
                            'Authorization': authHeader(),
                        }
                    });
                    if (response.status === 200) {
                        console.log(response)
                        this.student_status.student_subject_record = [];
                        this.student_status.total = response.data.total_results;
                        response.data.records.forEach((item) => {
                            this.student_status.student_subject_record.push(item);
                        });
                        this.student_status.loading = false;
                    }
                } catch (error) {
                    this.student_status.student_subject_record = [];
                    this.student_status.total = 0;
                    this.student_status.loading = false;
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: `Không thể lấy được dữ liệu môn học của sinh viên có MSSV ${ID} này!`,
                        position: 'is-bottom-right',
                        type: 'is-danger',
                    });
                    throw error
                }
            },
        },
        mounted() {
            this.getStudentRecordData();
        }
    }
</script>
