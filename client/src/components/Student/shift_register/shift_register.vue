<template>
    <div class="container">
      <h1 class="title is-3">Đăng ký thi</h1>
      <h2 class="subtitle is-6">Sinh viên đăng ký ca thi mà sinh viên đủ điều kiện dự thi và đang còn chỗ trống</h2>
      <hr>
      <b-field grouped group-multiline>
        <b-button
          :class="{'is-loading': shift.shift_loading}"
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
          placeholder="Tìm kiếm bằng mã môn thi"
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
                <b>Mã môn thi: </b>{{ props.option.Subject.SubjectID }}
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

      <b-field expanded>
        <b-table
          :data="shift.isShiftEmpty ? [] : shift.shift_record_data"
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
          @details-open="(row, index) => { currentShiftID = row.ShiftID ; room.page = 1; getRoomRecord(); closeOtherDetails(row, index) }"
          @details-close="(row, index) => { room.room_record_data = [] }"
          :show-detail-icon="true"
        >
          <template slot-scope="props">
            <b-table-column field="ShiftID" label="Mã ca thi" sortable>
              {{ props.row.ShiftID }}
            </b-table-column>
            <b-table-column field="SubjectID" label="Môn thi" sortable>
              <b>{{ props.row.Subject.SubjectID }} | {{ props.row.Subject.SubjectTitle }}</b>
            </b-table-column>
            <b-table-column field="Date_Start" label="Ngày thi" sortable>
              <span class="tag is-primary">
                {{ formatDate(props.row.Date_Start) }}
              </span>
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
              <b-table
                :data="room.isRoomEmpty ? [] : room.room_record_data"
                :loading="room.room_loading"
                paginated
                backend-pagination
                :current-page.sync="room.page"
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
                @sort="onRoomSort">

                <template slot-scope="props">
                  <b-table-column field="RoomID" label="Mã phòng" width="100">
                    {{ props.row.Exam_Room.RoomID }}
                  </b-table-column>
                  <b-table-column field="RoomName" label="Phòng thi" width="100">
                    {{ props.row.Exam_Room.RoomName }}
                  </b-table-column>
                  <b-table-column field="Maxcapacity" label="Số người dự thi / Số lượng máy tính" width="100">
                    {{ props.row.Student_Shift.length }} / {{ props.row.Exam_Room.Maxcapacity }}
                  </b-table-column>
                  <b-table-column width="10">
                    <b-button type="is-success" style="float: right" icon-pack="fas" icon-left="plus-square" outlined @click.prevent="registerShift(props.row.Room_ShiftID)">Đăng ký</b-button>
                  </b-table-column>
                </template>
                <template slot="empty">
                  <section class="section">
                    <b-message type="is-danger" has-icon>
                      Hiện tại ca thi này chưa có phòng thi!
                    </b-message>
                  </section>
                </template>
              </b-table>
            </template>
          <template slot="empty">
            <section class="section">
              <b-message type="is-danger" has-icon>
                Hiện tại chưa có ca thi (môn thi) nào được cho phép đăng ký!
              </b-message>
            </section>
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
                    isShiftEmpty: false,
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
                    isRoomEmpty: false,
                    roomID: '',
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
                if (response.data.status === 'success') {
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: 'Đã đăng ký thành công!',
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                    });
                }
                else if (response.data.status === 'already-registered') {
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: 'Bạn đã đăng ký phòng thi này rồi!',
                        position: 'is-bottom-right',
                        type: 'is-warning',
                        hasIcon: true
                    });
                }
                else if (response.data.status === 'out of capacity') {
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: 'Phòng này hiện tại đã đủ sinh viên đăng ký, bạn hãy đăng ký phòng khác!',
                        position: 'is-bottom-right',
                        type: 'is-warning',
                        hasIcon: true
                    });
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
                  this.getRoomRecord();
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
            closeOtherDetails(row) {
                this.shift.ID_Index = [row.ShiftID];
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
                            page_index: this.room.page,
                            per_page: this.room.per_page,
                            sort_field: this.room.sortField,
                            sort_order: this.room.sortOrder
                        },
                        headers: {
                            'Authorization': authHeader(),
                        }
                    });
                    // console.log(response.data.room_records);
                    if (response.status === 200) {
                        this.room.room_record_data = [];
                        this.room.total = response.data.total_results;
                        response.data.room_records.forEach((item) => {
                            this.room.room_record_data.push(item);
                            // console.log(item);
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
                      studentID: this.studentid,
                      subjectID: SubjectID,
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
            onShiftSort(field, order) {
                this.shift.sortField = field;
                this.shift.sortOrder = order;
                this.getShiftRecordData();
            },
            selectSemesterModal() {
                this.$buefy.modal.open({
                    parent: this,
                    component: enter_semester,
                    props: { semesterID: this.currentSemesterID },
                    hasModalCard: true,
                    customClass: 'custom-class custom-class-2',
                    canCancel: false,
                    events: {
                      'loadSemesterShifts': (semester_record) => {
                          this.semester.semester_record = semester_record;
                          this.SetCurrentSemesterID(semester_record.SemID);
                          if (semester_record.shift.length !== 0) {
                              this.getShiftRecordData();
                              this.$buefy.notification.open({
                                duration: 2000,
                                message: `Kỳ thi đã được truy cập và ca thi đã được lấy thành công!`,
                                position: 'is-bottom-right',
                                type: 'is-success',
                                hasIcon: true
                              });
                          }
                          else {
                              this.getShiftRecordData();
                              this.$buefy.notification.open({
                                duration: 2000,
                                message: 'Kỳ thi đã được truy cập nhưng tuy nhiên hiện tại chưa có ca thi nào được mở!',
                                position: 'is-bottom-right',
                                type: 'is-warning',
                                hasIcon: true
                              });
                          }
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
            // console.log(this.currentSemesterID);
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
