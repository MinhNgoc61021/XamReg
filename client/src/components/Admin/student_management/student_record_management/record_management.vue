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
                :data="search.searchResults"
                placeholder="Tìm kiếm bằng MSSV"
                icon="search"
                field="ID"
                :loading="search.searchLoading"
                @typing="onStudentSearch"
                @select="option => student.student_record = [option]"
                expanded>
              <template slot-scope="props">
                    <div class="media">
                        <div class="media-left">
                          <b-icon icon-pack="fas" icon="user-circle"></b-icon>
                        </div>
                        <div class="media-content">
                            <b>MSSV: </b>{{ props.option.ID }}
                            <br>
                            <b>Họ và tên: </b>{{ props.option.Fullname }}
                            <br>
                            <small>
                                Ngày sinh: {{ formatDate(props.option.Dob) }},
                                Khóa: <b>{{ props.option.CourseID }}</b>
                            </small>
                        </div>
                    </div>
                </template>
            </b-autocomplete>
        </b-field>
        <b-field v-if="student.student_record.length > 0">
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
            @details-open="(row, index) => { student_status.currentStudentID = row.ID ; getStudent_Subject(); closeOtherDetails(row, index) }"
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

                <b-table-column field="Role_Type" label="Chức vụ" sortable>
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
                <h4 class="title is-4">Danh sách môn học</h4>
                <b-field grouped group-multiline>
                  <b-button
                    :class="{'is-loading': student_status.loading}"
                    class="button"
                    @click="getStudent_Subject(props.row)"
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
                      <b-table-column field="SubjectID" label="Mã môn" sortable>
                        {{ props.row.SubjectID }}
                      </b-table-column>
                      <b-table-column field="SubjectTitle" label="Tên môn" sortable>
                        {{ props.row.SubjectTitle }}
                      </b-table-column>

                      <b-table-column field="Action">
                        <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onStatusDelete(props.row.SubjectID)"></b-button>
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
        </b-field>
        <b-field v-else>
          <b-message type="is-danger" has-icon>
            Hiện tại chưa có dự liệu sinh viên, bạn hãy nhập vào sinh viên!
          </b-message>
        </b-field>
    </section>
</template>

<script>
    import axios from 'axios'
    import { authHeader } from "../../../api/jwt_handling";
    import moment from 'moment/moment';
    import edit_student_form from "./edit/student_edit";
    import debounce from 'lodash/debounce';
    import { eventBus } from "../../../../main";

    /*
     student edit data form
    */
    export default {
        components: {
            edit_student_form,
        },
        data() {
            return {
                student: { // This is used to for student info
                    student_record: [],
                    total: 0,
                    loading: false,
                    sortField: 'ID',
                    sortOrder: 'desc',
                    defaultSortOrder: 'desc',
                    page: 1,
                    per_page: 5,
                },
                student_status: { // This is used to for student subject status
                    student_subject_record: [],
                    currentStudentID: '',
                    total: 0,
                    loading: false,
                    sortField: 'SubjectID',
                    sortOrder: 'desc',
                    defaultSortOrder: 'desc',
                    page: 1,
                    per_page: 5,
                    status_type: 'Qualified',
                    ID_Index: [], // ID_Index is used for expand event
                },
                search: {
                    searchResults: [],
                    searchLoading: false,
                },
            }
        },
        methods: {
            /*
             * Change formatDate
            */
            formatDate(date) {
                return moment(date).format('L');
            },
            /*
             * Load async student info record
            */
            async getStudentRecordData() {
                this.student.loading = true;
                try {
                    const response = await axios({
                        url: '/student/student-records',
                        method: 'get',
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
                    this.student.loading = false;
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: 'Không thể lấy được dữ liệu sinh viên!',
                        position: 'is-bottom-right',
                        type: 'is-danger',
                        hasIcon: true
                    });
                    throw error;

                }
            },
            /*
              * Handle student info record page-change event
            */
            onStudentPageChange(page) {
                this.student.page = page;
                this.getStudentRecordData();
            },
            /*
              * Handle student info record sort event
            */
            onStudentSort(field, order) {
                this.student.sortField = field;
                this.student.sortOrder = order;
                this.getStudentRecordData();
            },
            /*
              * Handle delete student info record event
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
                                url: '/student/remove-student-record',
                                method: 'delete',
                                headers: {
                                    'Authorization': authHeader(),
                                },
                                data: {
                                    delStudentID: recordID,
                                },
                            });
                            if (removeData.status === 200) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: `Đã xóa tài khoản có MSSV <b>${recordID}</b> thành công.`,
                                    position: 'is-bottom-right',
                                    type: 'is-success',
                                    hasIcon: true
                                });
                            }
                            this.getStudentRecordData();
                        } catch (e) {
                            if (e['message'].includes('401')) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: 'Không được quyền sử dụng!',
                                    position: 'is-bottom-right',
                                    type: 'is-danger',
                                    hasIcon: true
                                })
                            }
                        }
                    },
                });
            },
            /*
              * Handle edit student info record event
            */
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
                    canCancel: false,
                    events: {
                        'editStatus': (http_status) => {
                            if (http_status === 200) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: `Đã cập nhật tài khoản của sinh viên thành công!`,
                                    position: 'is-bottom-right',
                                    type: 'is-success',
                                    hasIcon: true
                                });
                                this.getStudentRecordData();
                            }
                            else if(http_status === 400) {
                                 this.$buefy.notification.open({
                                    duration: 2000,
                                    message: 'Kiểm tra lại, dữ liệu bạn nhập đang không đúng!',
                                    position: 'is-bottom-right',
                                    type: 'is-danger',
                                    hasIcon: true
                                 });
                            }
                            else if (http_status === 401) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: 'Không được quyền sử dụng!',
                                    position: 'is-bottom-right',
                                    type: 'is-danger',
                                    hasIcon: true
                                });
                            }
                        }
                    }
                });
            },
            onStudentSearch: debounce(function (ID) {
                this.search.searchLoading = true;
                if (ID.length > 8  || ID.length === 0) {
                    this.search.searchResults = [];
                    this.search.searchLoading = false;
                }
                else {
                    this.search.searchResults = [];
                    axios({
                        url: '/student/search-student-record',
                        method: 'get',
                        headers: {
                            'Authorization': authHeader(),
                        },
                        params: {
                            searchID: ID,
                        },
                    }).then((response) => {
                        if (response.status === 200) {
                            // console.log(response.data.search_results);
                            response.data.search_results.forEach((item) => {
                                this.search.searchResults.push(item);
                            });
                            this.search.searchLoading = false;
                        }

                    }).catch((error) => {
                        this.search.searchResults = [];
                        this.search.searchLoading = false;
                        this.$buefy.notification.open({
                            duration: 2000,
                            message: 'Không thể tìm được dữ liệu!',
                            position: 'is-bottom-right',
                            type: 'is-danger',
                            hasIcon: true
                        });
                        throw error;
                    });
                }

            }, 500),
            /*
              * Handle student status record page-change event
            */
            onStatusPageChange(page) {
                this.student_status.page = page;
                this.getStudent_Subject();
            },
            /*
              * Handle sort student status record event
            */
            onStatusSort(field, order) {
                this.student_status.sortField = field;
                this.student_status.sortOrder = order;
                this.getStudent_Subject();
            },
            /*
              * Handle delete student status record event
            */
            async onStatusDelete(SubjectID) {
              this.$buefy.dialog.confirm({
                    title: 'Xóa môn',
                    message: `Bạn có chắc chắn là muốn <b>xóa</b> môn học ${SubjectID} của sinh viên có MSSV ${this.student_status.currentStudentID} này không? Đã làm thì tự chịu đấy.`,
                    confirmText: 'Xóa!',
                    cancelText: 'Bỏ qua',
                    type: 'is-danger',
                    hasIcon: true,
                    onConfirm: async () => {
                        try {
                            const removeData = await axios({
                                url: '/student/remove-student-status-record',
                                method: 'delete',
                                headers: {
                                    'Authorization': authHeader(),
                                },
                                data: {
                                    delStudentID: this.student_status.currentStudentID,
                                    delSubjectID: SubjectID,
                                },
                            });
                            if (removeData.status === 200) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: `Đã xóa thành công môn học ${SubjectID} của sinh viên có MSSV <b>${this.student_status.currentStudentID}</b>!`,
                                    position: 'is-bottom-right',
                                    type: 'is-success',
                                    hasIcon: true
                                });
                            }
                        } catch (e) {
                            if (e['message'].includes('401')) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: 'Không được quyền sử dụng!',
                                    position: 'is-bottom-right',
                                    type: 'is-danger',
                                    hasIcon: true
                                })
                            }
                        } finally {
                            this.getStudent_Subject();
                        }
                    },
                });
            },
            async getStudent_Subject() {
                this.student_status.loading = true;
                try {
                    const response = await axios({
                        url: '/student/student-status-records',
                        method: 'get',
                        params: {
                            StudentID: this.student_status.currentStudentID,
                            type: this.student_status.status_type,
                            page_index: this.student_status.page,
                            per_page: this.student_status.per_page,
                            sort_field: this.student_status.sortField,
                            sort_order: this.student_status.sortOrder,
                        },
                        headers: {
                            'Authorization': authHeader(),
                        }
                    });
                    if (response.status === 200) {
                        // console.log(response);
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
                        message: `Không thể lấy được dữ liệu môn học của sinh viên có MSSV ${this.student_status.currentStudentID} này!`,
                        position: 'is-bottom-right',
                        type: 'is-danger',
                        hasIcon: true
                    });
                    throw error
                }
            },
            /*
              * Handle expand event for student status
            */
            closeOtherDetails(row) {
                this.student_status.ID_Index = [row.ID];
                // console.log(this.student_status.ID_Index);
            },
        },
        mounted() {
            this.getStudentRecordData();
        },
        created() {
            eventBus.$on('up-to-date', () => {
                this.getStudentRecordData();
                this.$buefy.notification.open({
                    duration: 2000,
                    message: `Đã cập nhật danh sách sinh viên thành công!`,
                    position: 'is-bottom-right',
                    type: 'is-success',
                    hasIcon: true
                });
            })
        }
    }
</script>
