<template>
    <div class="container">
      <h1 class="title is-3">Đăng ký thi</h1>
      <h2 class="subtitle is-6">Sinh viên đăng ký ca thi mà sinh viên đủ điều kiện dự thi và đang còn chỗ trống</h2>
      <b-field grouped group-multiline>
        <b-button
          :class="{'is-loading': shift.create_loading}"
          class="button"
          @click="getShiftRecordData"
        >
          <b-icon
            size="is-small"
            icon="sync"/>
          <span>Làm mới</span>
        </b-button>

        <b-autocomplete
          :data="search.searchResults"
          placeholder="Tìm kiếm bằng mã môn học"
          icon="search"
          field="ID"
          :loading="search.searchLoading"
          @typing="onShiftSearch"
          @select="option => shift.shift_record_data = [option]"
          expanded>
          <template slot-scope="props">
            <div class="media">
              <div class="media-left">
                <b-icon icon-pack="fas" icon="user-circle"></b-icon>
              </div>
              <div class="media-content">
                <b>Mã môn học: </b>{{ props.option.Subject.SubjectID }}
                <br>
                <b>Mã ca thi: </b>{{ props.option.ShiftID }}
              </div>
            </div>
          </template>
        </b-autocomplete>

        <b-button
          class="button"
          @click="selectSemesterModal"
        >
          <span>Chọn kỳ thi khác</span>
        </b-button>
      </b-field>

      <b-field group-multiline v-if="shift.shift_record_data.length === 0">
        <b-message type="is-danger" has-icon>
          Hiện tại bạn không chưa môn nào được cho pháp đăng ký
        </b-message>
      </b-field>

      <b-field expanded v-else>
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
          @details-open="(row, index) => { currentShiftID = row.ShiftID ; getRoomRecord(); closeOtherDetails(row, index) }"
          @details-close="(row, index) => { room.room_record_data = [] }"
          :show-detail-icon="true"
        >
          <template slot-scope="props">
            <b-table-column field="ShiftID" label="Mã ca thi" sortable>
              {{ props.row.ShiftID }}
            </b-table-column>
            <b-table-column field="SubjectID" label="Môn thi" sortable>
              <b></b>{{ props.row.Subject.SubjectID }} | {{ props.row.Subject.SubjectTitle }}
            </b-table-column>
            <b-table-column field="Date_Start" label="Ngày thi" sortable>
              {{ formatDate(props.row.Date_Start) }}
            </b-table-column>
            <b-table-column field="Start_At" label="Thời gian bắt đầu" sortable>
              {{ props.row.Start_At }}
            </b-table-column>
            <b-table-column field="End_At" label="Thời gian kết thúc" sortable>
              {{ props.row.End_At }}
            </b-table-column>
          </template>

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
              </b-field>

              <b-field v-if="room.room_record_data.length === 0 ">
                <b-message type="is-danger" has-icon>
                  Hiện tại ca thi này chưa có phòng thi
                </b-message>
              </b-field>
              <b-table v-else
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
                detail-key="RoomID"
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
                  <b-table-column width="10">
                    <b-button type="is-success" style="float: right" icon-pack="fas" icon-left="plus-square" outlined @click.prevent="registerShift(props.row.Room_ShiftID)">Đăng ký</b-button>
                  </b-table-column>
                </template>
              </b-table>
            </template>
        </b-table>
      </b-field>

      <h1 class="title is-3">Các môn đã đăng ký</h1>
      <b-field grouped group-multiline>
        <b-button
          :class="{'is-loading': registered_shift.create_loading}"
          class="button"
          @click="getRegisteredRoomShiftRecordData"
        >
          <b-icon
            size="is-small"
            icon="sync"/>
          <span>Làm mới</span>
        </b-button>
      </b-field>

      <b-field group-multiline v-if="registered_shift.registered_shift_record_data.length === 0">
        <b-message type="is-danger" has-icon>
          Bạn chưa đăng ký môn
        </b-message>
      </b-field>

      <b-field v-else>
        <b-table
          :data="registered_shift.registered_shift_record_data"
          :loading="registered_shift.shift_loading"
        >
          <template slot-scope="props">
            <b-table-column field="SubjectID" label="Môn thi" sortable>
              <b></b>{{ props.row.Subject.SubjectID }} | {{ props.row.Subject.SubjectTitle }}
            </b-table-column>
            <b-table-column field="RoomName" label="Phòng thi" sortable>
              {{ props.row.RoomName }}
            </b-table-column>
            <b-table-column field="Date_Start" label="Ngày thi" sortable>
              {{ formatDate(props.row.Date_Start) }}
            </b-table-column>
            <b-table-column field="Start_At" label="Thời gian bắt đầu" sortable>
              {{ props.row.Start_At }}
            </b-table-column>
            <b-table-column field="End_At" label="Thời gian kết thúc" sortable>
              {{ props.row.End_At }}
            </b-table-column>
          </template>

          <template slot="detail" slot-scope="props">
            <h4 class="title is-4">Danh sách phòng thi</h4>
            <b-field  expanded>
              <b-button
                :class="{'is-loading': registered_room.room_loading}"
                class="button"
                @click="getRegisteredRoomShiftRecordData"
              >
                <b-icon
                  size="is-small"
                  icon="sync"/>
              </b-button>
            </b-field>
            <b-table
              :data="registered_room.room_record_data"
              :loading="registered_room.room_loading"
              bordered
              narrowed
              hoverable
              detail-key="RoomID"
            >
              <template slot-scope="props">
                <b-table-column field="RoomID" label="Mã phòng" width="100" sortable>
                  {{ props.row.RoomID }}
                </b-table-column>
                <b-table-column field="RoomName" label="Phòng thi" width="100">
                  {{ props.row.RoomName }}
                </b-table-column>
                <b-table-column field="Maxcapacity" label="Số lượng máy tính" width="100">
                  {{ props.row.Maxcapacity }}
                </b-table-column>
              </template>
            </b-table>
          </template>
        </b-table>
      </b-field>
    </div>
</template>

<script>
    import axios from "axios";
    import {authHeader} from "../../api/jwt_handling";
    import enter_semester from "./enter_semester";
    import { mapActions, mapState } from 'vuex';
    import debounce from 'lodash/debounce';
    import moment from "moment";
    export default {
        name: 'shift-register',
        props: ['studentid'],
        data() {
            return {
                semester: {
                  semester_record: []
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
                registered_shift: {
                  registered_shift_record_data: [],
                  date_start: '',
                  start_at: '',
                  total: 0,
                  shift_loading: false,
                  create_loading: false,
                  search_loading: false,
                  ID_Index: [],
                },
                room: {
                    roomID: '',
                    room_record_data: [],
                    searchResults: [],
                    room_loading: false,
                    search_loading: false,
                },
                registered_room: {
                    roomID: '',
                    room_record_data: [],
                    searchResults: [],
                    room_loading: false,
                    search_loading: false,
                },
                search: {
                  searchResults: [],
                  searchLoading: false,
                }
            }
        },
        computed: {
            ...mapState([
                'currentSemesterID',
            ]),
        },
        methods: {
            ...mapActions([
                'SetCurrentSemesterID',
            ]),
            formatDate(date) {
                return moment(date).format('L');
            },
            async registerShift(Room_ShiftID) {
              try {
                const response = await axios({
                  url: '/shift-register/register-shift',
                  method: 'post',
                  data: {
                    studentID: this.studentid,
                    Room_ShiftID: Room_ShiftID,
                  },
                  headers: {
                    'Authorization': authHeader(),
                  }
                });
                if (response.status === 200) {
                    if (response.data.status === 'success') {
                        this.$buefy.notification.open({
                              duration: 2000,
                              message: 'Đã đăng ký thành công!',
                              position: 'is-bottom-right',
                              type: 'is-success',
                              hasIcon: true
                        });
                    }
                    else {
                        this.$buefy.notification.open({
                              duration: 2000,
                              message: 'Bạn đã đăng ký phong thi này rồi!',
                              position: 'is-bottom-right',
                              type: 'is-warning',
                              hasIcon: true
                        });
                    }
                }
              } catch (error) {
                this.$buefy.notification.open({
                  duration: 2000,
                  message: 'Không thể lấy được dữ liệu ca thi!',
                  position: 'is-bottom-right',
                  type: 'is-danger',
                  hasIcon: true
                });
                throw error;
              } finally {
                  this.getShiftRecordData();
                  this.getRegisteredRoomShiftRecordData()
              }
            },
            async getShiftRecordData() {
              this.shift.shift_loading = true;
                  try {
                      const response = await axios({
                          url: '/shift-register/shift-records',
                          method: 'get',
                          params: {
                              SemID: this.semester.semester_record.SemID,
                              StudentID: this.studentid,
                              page_index: this.shift.page,
                              per_page: this.shift.per_page,
                              sort_field: this.shift.sortField,
                              sort_order: this.shift.sortOrder
                          },
                          headers: {
                              'Authorization': authHeader(),
                          }
                      });
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
            },
            // lấy data các môn đã thi
            async getRegisteredRoomShiftRecordData() {
              this.registered_shift.shift_loading = true;
              try {
                const response = await axios({
                  url: '/shift-register/registered-room-shift-records',
                  method: 'get',
                  params: {
                    StudentID: this.studentid,
                    page_index: this.registered_shift.page,
                    per_page: this.registered_shift.per_page,
                    sort_field: this.registered_shift.sortField,
                    sort_order: this.registered_shift.sortOrder
                  },
                  headers: {
                    'Authorization': authHeader(),
                  }
                });
                console.log(response.data);
                if (response.status === 200) {
                  this.registered_shift.shift_record_data = [];
                  this.registered_shift.total = response.data.total_results;
                  response.data.shift_records.forEach((item) => {
                    this.registered_shift.shift_record_data.push(item);
                  });
                  // console.log(this.data);
                  this.registered_shift.shift_loading = false
                }
              } catch (error) {
                this.registered_shift.shift_record_data = [];
                this.registered_shift.total = 0;
                this.registered_shift.shift_loading = false;
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
            closeOtherDetails(row) {
                this.shift.ID_Index = [row.ShiftID];
                // console.log(this.student_status.ID_Index);
            },
            closeOtherRegisteredDetails(row) {
                this.registered_shift.ID_Index = [row.ShiftID];
                // console.log(this.student_status.ID_Index);
            },
            async getRoomRecord() {
                this.room.room_loading = true;
                try {
                    const response = await axios({
                        url: '/shift-register/room-records',
                        method: 'get',
                        params: {
                            shiftID: this.currentShiftID,
                        },
                        headers: {
                            'Authorization': authHeader(),
                        }
                    });
                    console.log(response.data.room_records);
                    if (response.status === 200) {
                        this.room.room_record_data = [];
                        this.room.total = response.data.total_results;
                        response.data.room_records.forEach((item) => {
                            this.room.room_record_data.push(item);
                            console.log(item);
                        });
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
            },
            onShiftSearch: debounce(function (SubjectID) {
              this.search.searchLoading = true;
              if (SubjectID.length > 7 || SubjectID.length === 0) {
                this.search.searchResults = [];
                this.search.searchLoading = false;
              }
              else {
                this.search.searchResults = [];
                axios({
                  url: '/shift-register/search-subject',
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
            onShiftPageChange(page) {
              this.shift.page = page;
              this.getShiftRecordData();
            },
            onRegisteredShiftPageChange(page) {
              this.registered_shift.page = page;
              this.getRegisteredRoomShiftRecordData();
            },
            onShiftSort(field, order) {
                this.shift.sortField = field;
                this.shift.sortOrder = order;
                this.getShiftRecordData();
            },
            onRegisteredShiftSort(field, order) {
                this.registered_shift.sortField = field;
                this.registered_shift.sortOrder = order;
                this.getRegisteredRoomShiftRecordData();
            },
            selectSemesterModal() {
                this.$buefy.modal.open({
                    parent: this,
                    component: enter_semester,
                    props: { semesterID: this.semesterID },
                    hasModalCard: true,
                    customClass: 'custom-class custom-class-2',
                    canCancel: false,
                    events: {
                      'loadSemesterShifts': (semester_record) => {
                        if (semester_record.SemTitle !== '') {
                          this.semester.semester_record = semester_record;
                          this.SetCurrentSemesterID(semester_record.SemID);
                          this.getShiftRecordData();
                          this.$buefy.notification.open({
                            duration: 2000,
                            message: `Đã lấy ca thi thành công!`,
                            position: 'is-bottom-right',
                            type: 'is-success',
                            hasIcon: true
                          });
                        } else if (semester_record.SemTitle === '') {
                          this.$buefy.notification.open({
                            duration: 2000,
                            message: 'Không lấy được dữ liệu!',
                            position: 'is-bottom-right',
                            type: 'is-danger',
                            hasIcon: true
                          });
                        }
                        // } else if (http_status === 401) {
                        //   this.$buefy.notification.open({
                        //     duration: 2000,
                        //     message: 'Không được quyền sử dụng!',
                        //     position: 'is-bottom-right',
                        //     type: 'is-danger',
                        //     hasIcon: true
                        //   });
                        // }
                      }
                    }
                  })
            },
            onRoomPageChange(page) {
                this.room.page = page;
                this.getRoomRecord();
            },
            onRoomSort(field, order) {
                this.room.sortField = field;
                this.room.sortOrder = order;
                this.getRoomRecord();
            },
        },
        mounted() {
            if (this.currentSemesterID === '') {
                this.selectSemesterModal();
            }
            else {
                this.semester.semester_record.SemID = this.currentSemesterID;
                this.getShiftRecordData();
            }
        },
    }
</script>
