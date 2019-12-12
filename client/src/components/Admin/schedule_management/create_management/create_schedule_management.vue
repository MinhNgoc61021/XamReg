<template>
  <div>
    <b-field grouped group-multiline>
      <b-button
        class="button"
        :class="{'is-loading': semester.loading}"
        @click="getSemesterRecordData"
      >
        <b-icon
          size="is-small"
          icon="sync"/>
        <span>Làm mới</span>
      </b-button>
      <b-field :message="[{ 'Kỳ thi chưa đánh': hasSemesterError },]" expanded>
        <b-input v-model="semester.newSemester" placeholder="Nhập tiêu đề để tạo kỳ thi" >
        </b-input>
      </b-field>
      <b-button
        :class="{'is-loading': semester.create_loading}"
        icon-pack="fas" icon-left="plus-square"
        @click="addNewSemester">
        <span>Tạo kỳ thi</span>
      </b-button>
    </b-field>
    <section>
      <div v-if="semester.semester_record_data.length > 0">
        <b-collapse
            class="card"
            v-for="(collapse, index) of semester.semester_record_data"
            :key="index"
            :open="isOpen === index"
            @open="() => { isOpen = index; currentSemID = collapse.SemID ;  getSemesterSubjectRecordData() }"
            @close="destroySemesterData()"
            >
            <div
                slot="trigger"
                slot-scope="props"
                class="card-header"
                role="button">
                <p class="card-header-title">
                    {{ collapse.SemTitle }}
                </p>
                <div style="float: right; margin: 20px;">
                    <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onSemesterDelete(collapse)"></b-button>
                </div>
            </div>
              <div class="card-content">
                <h2 class="subtitle is-6">Danh sách môn thi</h2>
                <b-field grouped group-multiline>
                    <b-autocomplete
                      :data="subject.searchResults"
                      placeholder="Nhập mã môn"
                      field="SubjectID"
                      :loading="subject.search_loading"
                      @typing="onSubjectSearch"
                      @select="option => { semester.SemesterSubjectID = option.SubjectID}"
                      expanded>
                      <template slot-scope="props">
                        <div class="media">
                            <div class="media-left">
                              <b-icon icon-pack="fas" icon="book"></b-icon>
                            </div>
                            <div class="media-content">
                                <b>Mã môn học: </b>{{ props.option.SubjectID }}
                                <br>
                                <b>Tên môn học: </b>{{ props.option.SubjectTitle }}
                            </div>
                        </div>
                      </template>
                    </b-autocomplete>
                  <b-button
                    type="is-primary"
                    :class="{'is-loading': semester.create_loading}"
                    @click="addNewSubject">
                    <span>Thêm Môn</span>
                  </b-button>
                </b-field>
                <div>
                  <div v-if="subject.semester_subject_record_data.length === 0" >
                    <b-message type="is-danger" has-icon>
                      Hiện tại chưa có thông tin về môn thi, bạn hãy nhập vào môn thi!
                    </b-message>
                  </div>
                  <div v-else>

                    <!--Semester Subject Record-->
                    <b-table
                        :data="subject.semester_subject_record_data"
                        :loading="subject.subject_loading"
                        paginated
                        backend-pagination
                        detailed
                        :total="subject.total"
                        :per-page="subject.per_page"
                        @page-change="onSemesterSubjectPageChange"
                        aria-next-label="Next page"
                        aria-previous-label="Previous page"
                        aria-page-label="Page"
                        aria-current-label="Current page"
                        backend-sorting
                        hoverable
                        detail-key="SubjectID"
                        :opened-detailed="subject.ID_Index"
                        :default-sort-direction="subject.defaultSortOrder"
                        :default-sort="[subject.sortField, subject.sortOrder]"
                        @sort="onSemesterSubjectSort"
                        @details-open="(row, index) => { subject.currentSemesterSubjectID = row.SubjectID ; getShiftRecordData(); closeOtherDetails(row, index) }"
                        @details-close="(row, index) => { shift.subject_shift_record_data = [] }"
                        :show-detail-icon="true">
                        <template slot-scope="props">
                            <b-table-column field="SubjectID" label="Mã môn" sortable width="90">
                                {{ props.row.SubjectID }}
                            </b-table-column>

                            <b-table-column field="SubjectTitle" label="Tên môn" sortable width="90">
                                 {{ props.row.SubjectTitle }}
                            </b-table-column>

                            <b-table-column field="Action" width="90">
                                <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onSemesterSubjectDelete(props.row.SubjectID)"></b-button>
                            </b-table-column>
                        </template>
                        <template slot="detail" slot-scope="props">
                            <h4 class="title is-4">Danh sách ca thi</h4>
                            <b-field grouped group-multiline>
                              <b-button
                                :class="{'is-loading': shift.shift_loading}"
                                class="button"
                                @click="getShiftRecordData(props.row)"
                              >
                                <b-icon
                                  size="is-small"
                                  icon="sync"/>
                              </b-button>
                              <b-button
                                class="button"
                                @click="addNewShift"
                                icon-pack="fas" icon-left="plus-square"
                              >
                                <span>Tạo ca thi</span>
                              </b-button>
                            </b-field>

                            <!--subject_shift-->
                            <b-field v-if="shift.subject_shift_record_data.length > 0" grouped group-multiline>
                              <b-table
                                :data="shift.subject_shift_record_data"
                                :loading="shift.loading"
                                paginated
                                backend-pagination
                                :total="shift.total"
                                :per-page="shift.per_page"
                                @page-change="onShiftPageChange"
                                aria-next-label="Next page"
                                aria-previous-label="Previous page"
                                aria-page-label="Page"
                                aria-current-label="Current page"
                                backend-sorting
                                bordered
                                narrowed
                                hoverable
                                detail-key="ID"
                                :default-sort-direction="shift.defaultSortOrder"
                                :default-sort="[shift.sortField, shift.sortOrder]"
                                @sort="onShiftSort">
                                <template slot-scope="props">

                                  <b-table-column field="ShiftID" label="Mã môn" width="100" sortable>
                                    {{ props.row.ShiftID }}
                                  </b-table-column>
                                  <b-table-column field="Date_Start" label="Ngày thi" width="100" sortable>
                                    {{ props.row.Date_Start }}
                                  </b-table-column>
                                  <b-table-column field="Start_At" label="Thời gian thi" width="100" sortable>
                                    {{ props.row.Start_At }}
                                  </b-table-column>
                                  <b-table-column field="RoomName" label="Phòng thi" width="100" sortable>
                                    {{ props.row.RoomName }}
                                  </b-table-column>
                                  <b-table-column field="Maxcapacity" label="Số lượng máy tính" width="100" sortable>
                                    {{ props.row.Maxcapacity }}
                                  </b-table-column>

                                  <b-table-column field="Action" width="90">
                                    <b-button type="is-warning" size="is-small" icon-pack="fas" icon-right="edit" outlined @click.prevent="onShiftEdit(props.row)"></b-button>
                                    <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onShiftDelete(props.row.ShiftID)"></b-button>
                                  </b-table-column>
                                </template>
                              </b-table>
                            </b-field>
                            <b-field v-else>
                              <b-message type="is-danger" has-icon>
                                Hiện tại chưa có dự liệu ca thi, bạn hãy nhập vào ca thi!
                              </b-message>
                            </b-field>

                            <!--subject_shift-->
                        </template>
                    </b-table>
                    <!--Semester Subject Record-->

                  </div>
                </div>
            </div>
        </b-collapse>
      </div>
      <div v-else>
        <b-message type="is-danger" has-icon>
          Hiện tại chưa có thông tin về kỳ thi, bạn hãy nhập vào và tạo kỳ thi mới!
        </b-message>
      </div>
    </section>
  </div>

</template>

<script>
    import axios from 'axios';
    import {authHeader} from "../../../api/jwt_handling";
    import debounce from 'lodash/debounce';
    import semester_edit from "./edit/semester_edit";
    import shift_edit from "./edit/shift_edit";
    import new_shift from "./create/shift_create";

    export default {
        name: 'create_management',
        data() {
            return {
                semester: {
                    newSemester: '', // new semester
                    semester_record_data: [], // semester info
                    loading: false, // semester loading
                    create_loading: false, // create semester loading
                    SemesterSubjectID: '', // subject for semester
                },
                subject: {
                    semester_subject_record_data: [], // subject semester data
                    total: 0,
                    subject_loading: false,
                    search_loading: false,
                    searchResults: [],
                    sortField: 'SubjectID',
                    sortOrder: 'desc',
                    defaultSortOrder: 'desc',
                    page: 1,
                    per_page: 5,
                    ID_Index: [],
                    currentSemesterSubjectID: '',
                },
                shift: {
                    subject_shift_record_data: [],
                    date_start: '',
                    start_at: '',
                    total: 0,
                    shift_loading: false,
                    search_loading: false,
                    searchResults: [],
                    sortField: 'ShiftID',
                    sortOrder: 'desc',
                    defaultSortOrder: 'desc',
                    page: 1,
                    per_page: 5,
                    ID_Index: [],
                },
                isOpen: null,
                collapses: [],
                currentSemID: '', // current opening semesterID
                hasSemesterError: false,
                hasSubjectError: false,
            }
        },
        methods: {
            async addNewSemester() {
                if (this.semester.newSemester.length === 0) {
                    this.hasSemesterError = true;
                }
                else {
                    try {
                        this.hasSemesterError = false;
                        this.semester.create_loading = true;
                        const response = await axios({
                            url: '/schedule/create-new-semester',
                            method: 'post',
                            headers: {
                                'Authorization': authHeader(),
                            },
                            data: {
                                newSemester: this.semester.newSemester,
                            },
                        });
                        if (response.status === 200) {
                            this.semester.create_loading = false;
                            if (response.data.status === 'success') {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: `Đã tạo kỳ thi thành công.`,
                                    position: 'is-bottom-right',
                                    type: 'is-success',
                                    hasIcon: true
                                });
                            } else {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: `Kỳ thi đã tồn tại từ trước.`,
                                    position: 'is-bottom-right',
                                    type: 'is-warning',
                                    hasIcon: true
                                });
                            }
                        }
                    } catch (e) {
                        this.semester.create_loading = false;
                        if (e['message'].includes('400')) {
                            this.$buefy.notification.open({
                                duration: 2000,
                                message: 'Kiểm tra lại, dữ liệu bạn nhập đang không đúng!',
                                position: 'is-bottom-right',
                                type: 'is-danger',
                                hasIcon: true
                            })
                        } else if (e['message'].includes('401')) {
                            this.$buefy.notification.open({
                                duration: 2000,
                                message: 'HTTP Status 401: Không được quyền sử dụng!',
                                position: 'is-bottom-right',
                                type: 'is-danger',
                                hasIcon: true
                            })
                        }
                    }
                    finally {
                        this.getSemesterRecordData();
                    }
                }
            },
            async onSemesterDelete(record) {
                this.$buefy.dialog.confirm({
                    title: 'Xóa kỳ thi',
                    message: `Bạn có chắc chắn là muốn <b>xóa</b> ${record.SemTitle} này không? Đã làm thì tự chịu đấy.`,
                    confirmText: 'Xóa!',
                    cancelText: 'Bỏ qua',
                    type: 'is-danger',
                    hasIcon: true,
                    onConfirm: async () => {
                        try {
                            const removeData = await axios({
                                url: '/schedule/remove-semester-record',
                                method: 'delete',
                                headers: {
                                    'Authorization': authHeader(),
                                },
                                data: {
                                    delSemID: record.SemID,
                                    delSemTitle: record.SemTitle,
                                },
                            });
                            if (removeData.status === 200) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: `Đã xóa kỳ thi <b>${record.SemTitle}</b> thành công.`,
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
                            this.getSemesterRecordData();
                        }
                    },
                });
            },
            async getSemesterRecordData() {
                this.semester.loading = true;
                try {
                    const response = await axios({
                        url: '/schedule/semester-records',
                        method: 'get',
                        headers: {
                            'Authorization': authHeader(),
                        }
                    });
                    // console.log(response.data);
                    if (response.status === 200) {
                        this.semester.semester_record_data = [];
                        this.semester.total = response.data.total_results;
                        response.data.semesterRecords.forEach((item) => {
                            this.semester.semester_record_data.push(item);
                        });
                        // console.log(this.data);
                        this.semester.loading = false
                    }
                } catch (error) {
                    this.semester.semester_record_data = [];
                    this.semester.loading = false;
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: 'Không thể lấy được dữ liệu kỳ thi!',
                        position: 'is-bottom-right',
                        type: 'is-danger',
                        hasIcon: true
                    });
                    throw error;
                }
            },
            async getSemesterSubjectRecordData() {
                this.subject.subject_loading = true;
                try {
                    const response = await axios({
                        url: '/schedule/semester-subject-records',
                        method: 'get',
                        params: {
                            SemID: this.currentSemID,
                            page_index: this.subject.page,
                            per_page: this.subject.per_page,
                            sort_field: this.subject.sortField,
                            sort_order: this.subject.sortOrder,
                        },
                        headers: {
                            'Authorization': authHeader(),
                        }
                    });
                    if (response.status === 200) {
                        // console.log(response);
                        this.subject.semester_subject_record_data = [];
                        this.subject.total = response.data.total_results;
                        response.data.semester_subject_records.forEach((item) => {
                            this.subject.semester_subject_record_data.push(item);
                        });
                        this.subject.subject_loading = false;
                    }
                } catch (error) {
                    this.subject.semester_subject_record_data = [];
                    this.subject.total = 0;
                    this.subject.loading = false;
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: `Không thể lấy được dữ liệu của kỳ thi ${this.currentSemID} này!`,
                        position: 'is-bottom-right',
                        type: 'is-danger',
                        hasIcon: true
                    });
                    throw error
                }
            },
            async onSemesterSubjectDelete(SubjectID) {
                console.log(SubjectID);
                console.log(this.currentSemID);
                this.$buefy.dialog.confirm({
                    title: 'Xóa kỳ thi',
                    message: `Bạn có chắc chắn là muốn <b>xóa</b> môn thi có mã số ${SubjectID} này không? Đã làm thì tự chịu đấy.`,
                    confirmText: 'Xóa!',
                    cancelText: 'Bỏ qua',
                    type: 'is-danger',
                    hasIcon: true,
                    onConfirm: async () => {
                        try {
                            const removeData = await axios({
                                url: '/schedule/remove-semester-subject-record',
                                method: 'delete',
                                headers: {
                                    'Authorization': authHeader(),
                                },
                                data: {
                                    semID: this.currentSemID,
                                    delSubjectID: SubjectID,
                                },
                            });
                            if (removeData.status === 200) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: `Đã xóa môn thi có mã số <b>${SubjectID}</b> thành công.`,
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
                            this.getSemesterSubjectRecordData();
                        }
                    },
                });
            },
            async getShiftRecordData() {
                this.shift.shift_loading = true;
                try {
                    const response = await axios({
                        url: '/schedule/shift-records',
                        method: 'get',
                        params: {
                            subjectID: this.subject.currentSemesterSubjectID,
                            page_index: this.shift.page,
                            per_page: this.shift.per_page,
                            sort_field: this.shift.sortField,
                            sort_order: this.shift.sortOrder
                        },
                        headers: {
                            'Authorization': authHeader(),
                        }
                    });
                    console.log(response.data.shift_records);
                    if (response.status === 200) {
                        this.shift.subject_shift_record_data = [];
                        this.shift.total = response.data.total_results;
                        response.data.shift_records.forEach((item) => {
                            this.shift.subject_shift_record_data.push(item);
                        });
                        // console.log(this.data);
                        this.shift.shift_loading = false
                    }
                } catch (error) {
                    this.shift.student_record = [];
                    this.shift.total = 0;
                    this.shift.shift_loading = false;
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: 'Không thể lấy được dữ liệu ca thi!',
                        position: 'is-bottom-right',
                        type: 'is-danger',
                        hasIcon: true
                    });
                    throw error;
                }
            },
            onSemesterSubjectSort(field, order) {
                this.subject.sortField = field;
                this.subject.sortOrder = order;
                this.getSemesterSubjectRecordData();
            },
            onSemesterSubjectPageChange(page) {
                this.subject.page = page;
                this.getSemesterSubjectRecordData();
            },
            async addNewSubject() {
                if (this.semester.SemesterSubjectID.length === 0) {
                    this.hasSubjectError = true;
                }
                else {
                   try {
                       // console.log(this.currentSemID, this.semester.SemesterSubjectID);
                       this.hasSubjectError = false;
                       this.semester.create_loading = true;
                       const response = await axios({
                           url: '/schedule/create-subject-semester',
                           method: 'post',
                           headers: {
                               'Authorization': authHeader(),
                           },
                           data: {
                               semID: this.currentSemID,
                               subjectID: this.semester.SemesterSubjectID,
                           },
                       });
                       if (response.status === 200) {
                           this.semester.create_loading = false;
                           if (response.data.status === 'success') {
                               this.$buefy.notification.open({
                                   duration: 2000,
                                   message: `Đã thêm môn thi thành công.`,
                                   position: 'is-bottom-right',
                                   type: 'is-success',
                                   hasIcon: true
                               });
                           } else {
                               this.$buefy.notification.open({
                                   duration: 2000,
                                   message: `Môn thi đã được thêm từ trước.`,
                                   position: 'is-bottom-right',
                                   type: 'is-warning',
                                   hasIcon: true
                               });
                           }
                       }
                    } catch (e) {
                       this.semester.create_loading = false;
                       if (e['message'].includes('400')) {
                            this.$buefy.notification.open({
                                duration: 2000,
                                message: 'Kiểm tra lại, dữ liệu bạn nhập đang không đúng!',
                                position: 'is-bottom-right',
                                type: 'is-danger',
                                hasIcon: true
                            })
                        } else if (e['message'].includes('401')) {
                           this.$buefy.notification.open({
                                duration: 2000,
                                message: 'HTTP Status 401: Không được quyền sử dụng!',
                                position: 'is-bottom-right',
                                type: 'is-danger',
                                hasIcon: true
                            })
                       }
                   }
                   finally {
                       this.subject.subject_loading = false;
                       this.getSemesterSubjectRecordData();
                   }
                }
            },
            onSubjectSearch: debounce(function (SubjectID) {
              this.subject.search_loading = true;
              if (SubjectID.length > 15 || SubjectID.length === 0) {
                this.subject.searchResults = [];
                this.subject.search_loading = false;
              }
              else {
                this.subject.searchResults = [];
                axios({
                  url: '/subject/search-subject',
                  method: 'get',
                  headers: {
                    'Authorization': authHeader(),
                  },
                  params: {
                    searchID: SubjectID,
                  },
                }).then((response) => {
                  if (response.status === 200) {
                    // console.log(response.data.search_results);
                    response.data.search_results.forEach((item) => {
                      this.subject.searchResults.push(item);
                    });
                    this.subject.search_loading = false;
                  }
                }).catch((error) => {
                  this.subject.searchResults = [];
                  this.subject.search_loading = false;
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
            async addNewShift() {
                this.$buefy.modal.open({
                    parent: this,
                    component: new_shift,
                    props: { currentSubjectID: this.subject.currentSemesterSubjectID},
                    hasModalCard: true,
                    customClass: 'custom-class custom-class-2',
                    canCancel: false,
                    events: {
                       'loadShifts': (http_status) => {
                         if (http_status === 200) {
                           this.$buefy.notification.open({
                             duration: 2000,
                             message: `Đã tạo ca thi thành công!`,
                             position: 'is-bottom-right',
                             type: 'is-success',
                             hasIcon: true
                           });
                           this.getShiftRecordData();
                         }
                         else if (http_status === 400) {
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
                })
            },
            onShiftSort(field, order) {
                this.shift.sortField = field;
                this.shift.sortOrder = order;
                this.getShiftRecordData();
            },
            onShiftPageChange(page) {
                this.shift.page = page;
                this.getShiftRecordData();
            },
            onShiftEdit(record) {
                this.$buefy.modal.open({
                   parent: this,
                   component: shift_edit,
                   props: {
                       currentShiftID: record.ShiftID,
                       currentStart_At: record.Start_At,
                       currentDate_Start: record.Date_Start,
                       currentRoomID: record.Date_Start,
                   },
                   hasModalCard: true,
                   customClass: 'custom-class custom-class-2',
                   canCancel: false,
                   events: {
                     'loadSubjects': (http_status) => {
                       if (http_status === 200) {
                         this.$buefy.notification.open({
                           duration: 2000,
                           message: `Đã sửa đổi thành công!`,
                           position: 'is-bottom-right',
                           type: 'is-success',
                           hasIcon: true
                         });
                         this.getShiftRecordData();
                       }
                       else if (http_status === 400) {
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
                })
            },
            onShiftDelete(ID) {

            },
            destroySemesterData() { // destroy subject data for scalability when closing accordion
                this.subject.semester_subject_record_data = [];
            },
            closeOtherDetails(row) {
                this.subject.ID_Index = [row.SubjectID];
                // console.log(this.student_status.ID_Index);
            },
        },
        mounted() {
            this.getSemesterRecordData();
        }
    }
</script>

<style scoped>

</style>
