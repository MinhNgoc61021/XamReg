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
            @open="() => { isOpen = index; currentSemID = collapse.SemID ;  getShiftRecordData() }"
            @close="destroySemesterData()"
            >
            <div
                slot="trigger"
                slot-scope="props"
                class="card-header"
                role="button">
                <p class="card-header-title">
                    <span>Tiêu đề: {{ collapse.SemTitle }}
                      <b-tag v-if="collapse.Status === false">Chưa mở đăng ký</b-tag>
                      <b-tag v-else type="is-primary">Mở đăng ký</b-tag>
                    </span>
                </p>
                <div style="float: right; margin: 20px;">
                    <b-button type="is-warning" size="is-small" icon-pack="fas" icon-right="edit" outlined @click.prevent="onSemesterEdit(collapse)"></b-button>
                    <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onSemesterDelete(collapse)"></b-button>
                </div>
            </div>
              <div class="card-content">
                <h4 class="title is-4">Danh sách ca thi</h4>
                <b-field>
                  <b-button
                    type="is-primary"
                    :class="{'is-loading': shift.create_loading}"
                    @click="addNewShift">
                    <span>Tạo ca thi</span>
                  </b-button>
                </b-field>
                <div>
                  <b-field group-multiline v-if="shift.shift_record_data.length === 0">
                    <b-message type="is-danger" has-icon>
                      Hiện tại chưa có thông tin về ca thi trong <b>{{ collapse.SemTitle }}</b>, bạn hãy nhập vào ca thi!
                    </b-message>
                  </b-field>
                  <b-field expanded v-else>

                    <!--Shift Record-->
                    <b-table
                        :data="shift.shift_record_data"
                        :loading="shift.shift_loading"
                        paginated
                        backend-pagination
                        detailed
                        :total="shift.total"
                        :per-page="shift.per_page"
                        @page-change="onShiftPageChange"
                        aria-next-label="Next page"
                        aria-previous-label="Previous page"
                        aria-page-label="Page"
                        aria-current-label="Current page"
                        backend-sorting
                        hoverable
                        detail-key="ShiftID"
                        :opened-detailed="shift.ID_Index"
                        :default-sort-direction="shift.defaultSortOrder"
                        :default-sort="[shift.sortField, shift.sortOrder]"
                        @sort="onShiftSort"
                        @details-open="(row, index) => { currentShiftID = row.ShiftID; getRoomRecord(); closeOtherDetails(row, index) }"
                        @details-close="(row, index) => { room.room_record_data = []; room.page = 1 }"
                        :show-detail-icon="true">
                        <template slot-scope="props">
                            <b-table-column field="ShiftID" label="Mã ca thi" width="100" sortable>
                              {{ props.row.ShiftID }}
                            </b-table-column>
                            <b-table-column field="SubjectID" label="Môn thi" width="100" sortable>
                              <b>{{ props.row.Subject.SubjectID }} | {{ props.row.Subject.SubjectTitle }}</b>
                            </b-table-column>
                            <b-table-column field="Date_Start" label="Ngày thi" width="100" sortable>
                              <span class="tag is-success">
                                {{ formatDate(props.row.Date_Start) }}
                              </span>
                            </b-table-column>
                            <b-table-column field="Start_At" label="Thời gian bắt đầu" width="100" sortable>
                              {{ props.row.Start_At }}
                            </b-table-column>
                            <b-table-column field="End_At" label="Thời gian kết thúc" width="100" sortable>
                              {{ props.row.End_At }}
                            </b-table-column>

                            <b-table-column field="Action" width="90">
                                <b-button type="is-warning" size="is-small" icon-pack="fas" icon-right="edit" outlined @click.prevent="onShiftEdit(props.row)"></b-button>
                                <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onShiftDelete(props.row.ShiftID)"></b-button>
                            </b-table-column>
                        </template>

                        <!--Room-->
                        <template slot="detail" slot-scope="props">
                            <h4 class="title is-4">Danh sách phòng thi</h4>
                            <b-field  expanded>
                              <b-button
                                :class="{'is-loading': room.room_loading}"
                                class="button"
                                @click="getRoomRecord"
                              >
                                <b-icon
                                  size="is-small"
                                  icon="sync"/>
                              </b-button>
                              <b-autocomplete clear-on-select
                                  :data="room.searchResults"
                                  placeholder="Tìm kiếm để chọn phòng thi"
                                  icon="search"
                                  field="RoomName"
                                  :loading="room.search_loading"
                                  @typing="onRoomSearch"
                                  @select="option => { room.select_search = [option]; addNewRoom() }"
                                   expanded>
                                    <template slot-scope="props">
                                      <div class="media">
                                        <div class="media-content">
                                          <b>Tên phòng: </b>{{ props.option.RoomName }}
                                        </div>
                                      </div>
                                    </template>
                                </b-autocomplete>
                            </b-field>
                            <!--shift-->
                            <b-field v-if="room.room_record_data.length > 0">
                              <b-table
                                :data="room.room_record_data"
                                :loading="room.room_loading"
                                paginated
                                backend-pagination
                                :total="room.total"
                                :per-page="room.per_page"
                                @page-change="onRoomPageChange"
                                aria-next-label="Next page"
                                aria-previous-label="Previous page"
                                aria-page-label="Page"
                                aria-current-label="Current page"
                                backend-sorting
                                bordered
                                narrowed
                                hoverable
                                :default-sort-direction="room.defaultSortOrder"
                                :default-sort="[room.sortField, room.sortOrder]"
                                @sort="onRoomSort">
                                <template slot-scope="props">

                                  <b-table-column field="RoomID" label="Mã phòng" width="100" sortable>
                                    {{ props.row.Exam_Room.RoomID }}
                                  </b-table-column>
                                  <b-table-column field="RoomName" label="Phòng thi" width="100">
                                    {{ props.row.Exam_Room.RoomName }}
                                  </b-table-column>
                                  <b-table-column field="Maxcapacity" label="Số lượng máy tính" width="100">
                                    {{ props.row.Exam_Room.Maxcapacity }}
                                  </b-table-column>

                                  <b-table-column field="Action" width="90">
                                    <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onRoomDelete(props.row.Exam_Room.RoomID)"></b-button>
                                  </b-table-column>
                                </template>
                              </b-table>
                            </b-field>
                            <b-field v-else>
                              <b-message type="is-danger" has-icon>
                                Hiện tại chưa có dự liệu phòng thi trong ca thi này, bạn hãy nhập vào môn thi!
                              </b-message>
                            </b-field>

                            <!--shift-->
                        </template>
                    </b-table>
                    <!--Shift Record-->

                  </b-field >
                </div>
            </div>
        </b-collapse>
      </div>
      <div v-else>
      </div>
    </section>
  </div>

</template>

<script>
    import axios from 'axios';
    import moment from 'moment';
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
                    semester_status: false,
                },
                shift: {
                    shift_record_data: [],
                    date_start: '',
                    start_at: '',
                    total: 0,
                    shift_loading: false,
                    create_loading: false,
                    search_loading: false,
                    sortField: 'ShiftID',
                    sortOrder: 'desc',
                    defaultSortOrder: 'desc',
                    page: 1,
                    per_page: 5,
                    ID_Index: [],
                },
                room: {
                    select_search: Object,
                    room_record_data: [],
                    total: 0,
                    searchResults: [],
                    room_loading: false,
                    search_loading: false,
                    sortField: 'RoomID',
                    sortOrder: 'desc',
                    defaultSortOrder: 'desc',
                    page: 1,
                    per_page: 5,
                },
                isOpen: null,
                collapses: [],
                currentShiftID: '', // current opening shiftID
                currentSemID: '', // current opening semesterID
                hasSemesterError: false,
                hasSubjectError: false,
                hasRoomError: false,
            }
        },
        methods: {
            formatDate(date) {
                return moment(date).format('L');
            },
            async addNewSemester() {
                if (this.semester.newSemester.length === 0) {
                    this.hasSemesterError = true;
                }
                else {
                    try {
                        this.hasSemesterError = false;
                        this.semester.create_loading = true;
                        const response = await axios({
                            url: '/schedule/create-semester',
                            method: 'post',
                            headers: {
                                'Authorization': authHeader(),
                            },
                            data: {
                                newSemester: this.semester.newSemester,
                            },
                        });
                        this.semester.create_loading = false;
                        if (response.status === 200) {
                            this.$buefy.notification.open({
                                duration: 2000,
                                message: `Đã tạo kỳ thi thành công!`,
                                position: 'is-bottom-right',
                                type: 'is-success',
                                hasIcon: true
                            });
                        }
                        else if (response.status === 202) {
                            this.$buefy.notification.open({
                                duration: 2000,
                                message: `Kỳ thi đã tồn tại từ trước!`,
                                position: 'is-bottom-right',
                                type: 'is-warning',
                                hasIcon: true
                            });
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
                                message: 'Không được quyền sử dụng!',
                                position: 'is-bottom-right',
                                type: 'is-danger',
                                hasIcon: true
                            })
                        }
                    }
                    finally {
                        this.semester.newSemester = '';
                        this.getSemesterRecordData();
                    }
                }
            }, // xong
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
                                url: '/schedule/remove-semester',
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
                                    message: 'Không được quyền sử dụng!',
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
            }, // xong
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
            }, // xong
            async onSemesterEdit(record) {
                this.$buefy.modal.open({
                   parent: this,
                   component: semester_edit,
                   props: {
                       currentSemID: record.SemID,
                       currentSemTitle: record.SemTitle,
                       currentStatus: record.Status,
                   },
                   hasModalCard: true,
                   customClass: 'custom-class custom-class-2',
                   canCancel: false,
                   events: {
                     'loadSemesters': (http_status) => {
                       if (http_status === 200) {
                         this.$buefy.notification.open({
                           duration: 2000,
                           message: `Đã sửa đổi thành công!`,
                           position: 'is-bottom-right',
                           type: 'is-success',
                           hasIcon: true
                         });
                         this.getSemesterRecordData();
                       }
                       else if (http_status === 202) {
                          this.$buefy.notification.open({
                           duration: 2000,
                           message: `Kỳ thi đã tồn tại từ trước!`,
                           position: 'is-bottom-right',
                           type: 'is-warning',
                           hasIcon: true
                         });
                         this.getSemesterRecordData();
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
            async addNewShift() {
                this.$buefy.modal.open({
                    parent: this,
                    component: new_shift,
                    props: { currentSemesterID: this.currentSemID },
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
                         else if (http_status === '202-already-exist-subject') {
                             this.$buefy.notification.open({
                               duration: 2000,
                               message: `Ca thi đang bị trùng môn thi với ca thi khác!`,
                               position: 'is-bottom-right',
                               type: 'is-warning',
                               hasIcon: true
                             });
                         }
                         else if (http_status === '202-time-false') {
                             this.$buefy.notification.open({
                               duration: 2000,
                               message: `Thời gian bắt đầu thi và kết thúc phải chênh nhau ít nhất <b>1 tiếng</b>!`,
                               position: 'is-bottom-right',
                               type: 'is-warning',
                               hasIcon: true
                             });
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
            }, // xong
            onShiftSort(field, order) {
                this.shift.sortField = field;
                this.shift.sortOrder = order;
                this.getShiftRecordData();
            }, // xong
            async getShiftRecordData() {
                this.shift.shift_loading = true;
                try {
                    const response = await axios({
                        url: '/schedule/shift-records',
                        method: 'get',
                        params: {
                            semID: this.currentSemID,
                            page_index: this.shift.page,
                            per_page: this.shift.per_page,
                            sort_field: this.shift.sortField,
                            sort_order: this.shift.sortOrder
                        },
                        headers: {
                            'Authorization': authHeader(),
                        }
                    });
                    // console.log(response.data.shift_records);
                    if (response.status === 200) {
                        this.shift.shift_record_data = [];
                        this.shift.total = response.data.total_results;
                        response.data.shift_records.forEach((item) => {
                            this.shift.shift_record_data.push(item);
                        });
                        // console.log(this.data);
                        this.shift.shift_loading = false
                    }
                } catch (error) {
                    this.shift.shift_record_data = [];
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
            }, // xong
            onShiftPageChange(page) {
                this.shift.page = page;
                this.room.page = 1;
                this.getShiftRecordData();
            }, // xong
            onShiftEdit(record) {
                this.$buefy.modal.open({
                   parent: this,
                   component: shift_edit,
                   props: {
                       currentSemID: this.currentSemID,
                       currentShiftID: record.ShiftID,
                       currentSubjectID: record.Subject.SubjectID,
                       currentDate_Start: new Date(moment(record.Date_Start).format('MM/DD/YYYY')),
                       currentStart_At: new Date(moment(record.Start_At, 'hh:mm')),
                       currentEnd_At: new Date(moment(record.End_At, 'hh:mm')),
                   },
                   hasModalCard: true,
                   customClass: 'custom-class custom-class-2',
                   canCancel: false,
                   events: {
                     'editShift': (http_status) => {
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
                       else if (http_status === '202-already-exist-subject') {
                             this.$buefy.notification.open({
                               duration: 2000,
                               message: `Ca thi đang bị trùng môn thi với ca thi khác!`,
                               position: 'is-bottom-right',
                               type: 'is-warning',
                               hasIcon: true
                             });
                         }
                         else if (http_status === '202-time-false') {
                             this.$buefy.notification.open({
                               duration: 2000,
                               message: `Thời gian bắt đầu thi và kết thúc phải chênh nhau ít nhất <b>1 tiếng</b>!`,
                               position: 'is-bottom-right',
                               type: 'is-warning',
                               hasIcon: true
                             });
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
            }, // chưa xong
            async onShiftDelete(ID) {
                this.$buefy.dialog.confirm({
                    title: 'Xóa ca thi',
                    message: `Bạn có chắc chắn là muốn <b>xóa</b> ca thi có mã ${ID} này không? Đã làm thì tự chịu đấy.`,
                    confirmText: 'Xóa!',
                    cancelText: 'Bỏ qua',
                    type: 'is-danger',
                    hasIcon: true,
                    onConfirm: async () => {
                        try {
                            const removeData = await axios({
                                url: '/schedule/remove-shift',
                                method: 'delete',
                                headers: {
                                    'Authorization': authHeader(),
                                },
                                data: {
                                    delShiftID: ID,
                                },
                            });
                            if (removeData.status === 200) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: `Đã xóa ca thi có mã <b>${ID}</b> thành công.`,
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
                            this.getShiftRecordData();
                        }
                    },
                });
            }, // xong
            async addNewRoom() {
                try {
                    this.room.room_loading = true;
                    const response = await axios({
                        url: '/schedule/create-room',
                        method: 'post',
                        headers: {
                            'Authorization': authHeader(),
                        },
                        data: {
                            roomID: this.room.select_search[0].RoomID,
                            shiftID: this.currentShiftID,
                        },
                    });
                    if (response.status === 200) {
                        this.room.room_loading = false;
                        if (response.data.status === 'success') {
                            this.$buefy.notification.open({
                                duration: 2000,
                                message: `Đã thêm phòng thi thành công.`,
                                position: 'is-bottom-right',
                                type: 'is-success',
                                hasIcon: true
                            });
                        } else {
                            this.$buefy.notification.open({
                                duration: 2000,
                                message: `Phòng thi đã tồn tại từ trước.`,
                                position: 'is-bottom-right',
                                type: 'is-warning',
                                hasIcon: true
                            });
                        }
                    }
                } catch (e) {
                    this.room.room_loading = false;
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
                            message: 'Không được quyền sử dụng!',
                            position: 'is-bottom-right',
                            type: 'is-danger',
                            hasIcon: true
                        })
                    }
                }
                finally {
                    this.getRoomRecord();
                }
            },
            async getRoomRecord() {
                this.room.room_loading = true;
                try {
                    const response = await axios({
                        url: '/schedule/room-records',
                        method: 'get',
                        params: {
                            shiftID: this.currentShiftID,
                            page_index: this.room.page,
                            per_page: this.room.per_page,
                            sort_field: this.room.sortField,
                            sort_order: this.room.sortOrder
                        },
                        headers: {
                            'Authorization': authHeader(),
                        }
                    });
                    // console.log(response.data.shift_records);
                    if (response.status === 200) {
                        this.room.room_record_data = [];
                        this.room.total = response.data.total_results;
                        response.data.room_records.forEach((item) => {
                            this.room.room_record_data.push(item);
                        });
                        // console.log(this.data);
                        this.room.room_loading = false
                    }
                } catch (error) {
                    this.room.room_record_data = [];
                    this.room.total = 0;
                    this.room.room_loading = false;
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: 'Không thể lấy được dữ liệu phòng!',
                        position: 'is-bottom-right',
                        type: 'is-danger',
                        hasIcon: true
                    });
                    throw error;
                }
            }, // xong
            onRoomPageChange(page) {
                this.room.page = page;
                this.getRoomRecord();
            }, // xong
            onRoomSort(field, order) {
                this.room.sortField = field;
                this.room.sortOrder = order;
                this.getRoomRecord();
            }, // xong
            async onRoomDelete(ID) {
                this.$buefy.dialog.confirm({
                    title: 'Xóa kỳ thi',
                    message: `Bạn có chắc chắn là muốn <b>xóa</b> phòng thi có mã ${ID} này không? Đã làm thì tự chịu đấy.`,
                    confirmText: 'Xóa!',
                    cancelText: 'Bỏ qua',
                    type: 'is-danger',
                    hasIcon: true,
                    onConfirm: async () => {
                        try {
                            const removeData = await axios({
                                url: '/schedule/remove-room',
                                method: 'delete',
                                headers: {
                                    'Authorization': authHeader(),
                                },
                                data: {
                                    currentShiftID: this.currentShiftID,
                                    delRoomID: ID,
                                },
                            });
                            if (removeData.status === 200) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: `Đã xóa phòng thi có mã ${ID}`,
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
                            this.getRoomRecord();
                        }
                    },
                });
            },
            onRoomSearch: debounce(function (roomName) {
                this.room.search_loading = true;
                if (roomName.length === 0) {
                    this.room.searchResults = [];
                    this.room.search_loading = false;
                }
                else {
                    this.room.searchResults = [];
                    axios({
                        url: '/room/search-room-record',
                        method: 'get',
                        headers: {
                            'Authorization': authHeader(),
                        },
                        params: {
                            searchName: roomName,
                        },
                    }).then((response) => {
                        if (response.status === 200) {
                            // console.log(response.data.search_results);
                            response.data.search_results.forEach((item) => {
                                this.room.searchResults.push(item);
                            });
                            this.room.search_loading = false;
                        }
                    }).catch((error) => {
                        this.room.searchResults = [];
                        this.room.search_loading = false;
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
            }, 500), // xong
            destroySemesterData() { // destroy subject data for scalability when closing accordion
                this.shift.shift_record_data = [];
            },
            closeOtherDetails(row) {
                this.shift.ID_Index = [row.ShiftID];
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
