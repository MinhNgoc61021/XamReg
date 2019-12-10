<template>
    <section>
        <b-field grouped group-multiline>
            <b-button
              :class="{'is-loading': student_subject.loading}"
              class="button"
              @click="getStudent_Subject()"
            >
              <b-icon
                size="is-small"
                icon="sync"/>
              <span>Làm mới</span>
            </b-button>

            <b-select v-model="student_subject.per_page">
              <option value="5">5 dòng/trang</option>
              <option value="10">10 dòng/trang</option>
              <option value="15">15 dòng/trang</option>
              <option value="20">20 dòng/trang</option>
            </b-select>

            <b-autocomplete
                :data="search.searchResults"
                placeholder="Tìm kiếm bằng Mã Môn"
                icon="search"
                field="ID"
                :loading="search.searchLoading"
                @typing="onStudentSearch"
                @select="option => student_subject.student_record = [option]"
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
        <b-table
            :data="student_subject.student_record"
            :loading="student_subject.loading"
            paginated
            backend-pagination
            detailed
            :total="student_subject.total"
            :per-page="student_subject.per_page"
            @page-change="onStudentPageChange"
            aria-next-label="Next page"
            aria-previous-label="Previous page"
            aria-page-label="Page"
            aria-current-label="Current page"
            backend-sorting
            hoverable
            detail-key="ID"
            :opened-detailed="subject_shift.ID_Index"
            :default-sort-direction="student_subject.defaultSortOrder"
            :default-sort="[student_subject.sortField, student_subject.sortOrder]"
            @sort="onStudentSort"
            @details-open="(row, index) => { subject_shift.currentStudentID = row.ID ; getStudent_Subject(); closeOtherDetails(row, index) }"
            @details-close="(row, index) => { subject_shift.student_subject_record = [] }"
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
                    :class="{'is-loading': subject_shift.loading}"
                    class="button"
                    @click="getStudent_Subject(props.row)"
                  >
                    <b-icon
                      size="is-small"
                      icon="sync"/>
                  </b-button>
                  <b-select v-model="subject_shift.status_type">
                    <option value="Qualified" >Đủ điều kiện thi</option>
                    <option value="Unqualified">Không đủ điều kiện thi</option>
                  </b-select>
                </b-field>
                <b-field v-if="subject_shift.student_subject_record.length > 0" grouped group-multiline>
                  <b-table
                    :data="subject_shift.student_subject_record"
                    :loading="subject_shift.loading"
                    paginated
                    backend-pagination
                    :total="subject_shift.total"
                    :per-page="subject_shift.per_page"
                    @page-change="onStatusPageChange"
                    aria-next-label="Next page"
                    aria-previous-label="Previous page"
                    aria-page-label="Page"
                    aria-current-label="Current page"
                    backend-sorting
                    bordered
                    hoverable
                    detail-key="ID"
                    :default-sort-direction="subject_shift.defaultSortOrder"
                    :default-sort="[subject_shift.sortField, subject_shift.sortOrder]"
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
                    Hiện tại môn thi này chưa được sắp xếp lịch, bạn hãy kiểm tra lại sau!
                  </b-message>
                </b-field>
            </template>
        </b-table>
    </section>
</template>

<script>
    import axios from 'axios'
    import { authHeader } from "../../api/jwt_handling";
    import moment from 'moment/moment';
    import debounce from 'lodash/debounce';
    import edit_student_modal_form
        from "../../Admin/student_management/student_record_management/edit/edit_student_modal_form";
    /*
     student edit data form
    */
    export default {
        components: {
            edit_student_modal_form,
        },
        data() {
            return {
                student_subject: { // This is used to for student info
                    student_record: [],
                    total: 0,
                    loading: false,
                    sortField: 'ID',
                    sortOrder: 'desc',
                    defaultSortOrder: 'desc',
                    page: 1,
                    per_page: 5,

                },
                subject_shift: { // This is used to for student subject status
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
                this.student_subject.loading = true;
                try {
                    const response = await axios({
                        url: '/record/student-records',
                        method: 'get',
                        params: {
                            page_index: this.student_subject.page,
                            per_page: this.student_subject.per_page,
                            sort_field: this.student_subject.sortField,
                            sort_order: this.student_subject.sortOrder
                        },
                        headers: {
                            'Authorization': authHeader(),
                        }
                    });
                    if (response.status === 200) {
                        this.student_subject.student_record = [];
                        this.student_subject.total = response.data.total_results;
                        response.data.records.forEach((item) => {
                            this.student_subject.student_record.push(item);
                        });
                        // console.log(this.data);
                        this.student_subject.loading = false
                    }
                } catch (error) {
                    this.student_subject.student_record = [];
                    this.student_subject.total = 0;
                    this.student_subject.loading = false;
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
                this.student_subject.page = page;
                this.getStudentRecordData();
            },
            /*
              * Handle student info record sort event
            */
            onStudentSort(field, order) {
                this.student_subject.sortField = field;
                this.student_subject.sortOrder = order;
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
                                url: '/record/remove-student-record',
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
                                    message: 'HTTP Status 401: Không được quyền sử dụng!',
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
                    component: edit_student_modal_form,
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
                        'loadStudentData': (http_status) => {
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
                        url: '/record/search-student-record',
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
                this.subject_shift.page = page;
                this.getStudent_Subject();
            },
            /*
              * Handle sort student status record event
            */
            onStatusSort(field, order) {
                this.subject_shift.sortField = field;
                this.subject_shift.sortOrder = order;
                this.getStudent_Subject();
            },
            /*
              * Handle delete student status record event
            */
            async onStatusDelete(SubjectID) {
              this.$buefy.dialog.confirm({
                    title: 'Xóa môn',
                    message: `Bạn có chắc chắn là muốn <b>xóa</b> môn học ${SubjectID} của sinh viên có MSSV ${this.subject_shift.currentStudentID} này không? Đã làm thì tự chịu đấy.`,
                    confirmText: 'Xóa!',
                    cancelText: 'Bỏ qua',
                    type: 'is-danger',
                    hasIcon: true,
                    onConfirm: async () => {
                        try {
                            const removeData = await axios({
                                url: '/record/remove-student-status-record',
                                method: 'delete',
                                headers: {
                                    'Authorization': authHeader(),
                                },
                                data: {
                                    delStudentID: this.subject_shift.currentStudentID,
                                    delSubjectID: SubjectID,
                                },
                            });
                            if (removeData.status === 200) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: `Đã xóa thành công môn học ${SubjectID}của sinh viên có MSSV <b>${this.subject_shift.currentStudentID}</b>.`,
                                    position: 'is-bottom-right',
                                    type: 'is-success',
                                    hasIcon: true
                                });
                            }
                        } catch (e) {
                            if (e['message'].includes('401')) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: 'HTTP Status 401: Không được quyền sử dụng!',
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
                this.subject_shift.loading = true;
                try {
                    const response = await axios({
                        url: '/record/student-status-records',
                        method: 'get',
                        params: {
                            StudentID: this.subject_shift.currentStudentID,
                            type: this.subject_shift.status_type,
                            page_index: this.subject_shift.page,
                            per_page: this.subject_shift.per_page,
                            sort_field: this.subject_shift.sortField,
                            sort_order: this.subject_shift.sortOrder,
                        },
                        headers: {
                            'Authorization': authHeader(),
                        }
                    });
                    if (response.status === 200) {
                        // console.log(response);
                        this.subject_shift.student_subject_record = [];
                        this.subject_shift.total = response.data.total_results;
                        response.data.records.forEach((item) => {
                            this.subject_shift.student_subject_record.push(item);
                        });
                        this.subject_shift.loading = false;
                    }
                } catch (error) {
                    this.subject_shift.student_subject_record = [];
                    this.subject_shift.total = 0;
                    this.subject_shift.loading = false;
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: `Không thể lấy được dữ liệu môn học của sinh viên có MSSV ${this.subject_shift.currentStudentID} này!`,
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
                this.subject_shift.ID_Index = [row.ID];
                // console.log(this.student_status.ID_Index);
            },
        },
        mounted() {
            this.getStudentRecordData();
        }
    }
</script>
