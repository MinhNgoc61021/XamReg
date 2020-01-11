<template>
  <div>
    <b-field group-multiline>
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
    </b-field>

    <section>
      <div v-if="semester.semester_record_data.length > 0">
        <b-collapse
            class="card"
            v-for="(collapse, index) of semester.semester_record_data"
            :key="index"
            :open="isOpen === index"
            @open="() => { isOpen = index; shift.page = 1; currentSemID = collapse.SemID ;  getShiftRecordData() }"
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
                      <b-tag v-else type="is-primary">Đang mở đăng ký</b-tag>
                    </span>
                </p>
            </div>
              <div class="card-content">
                <h4 class="title is-4">Danh sách ca thi</h4>
                <div>
                  <b-field expanded>

                    <!--Shift Record-->
                    <b-table
                        :data="shift.isShiftEmpty ? [] : shift.shift_record_data"
                        :loading="shift.shift_loading"
                        paginated
                        backend-pagination
                        detailed
                        :current-page.sync="shift.page"
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
                        @details-open="(row, index) => { currentShiftID = row.ShiftID; room.page = 1; currentSubjectName = row.Subject.SubjectTitle; getRoomRecord(); closeOtherDetails_Shift(row, index) }"
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
                              <span class="tag is-primary">
                                {{ formatDate(props.row.Date_Start) }}
                              </span>
                            </b-table-column>
                            <b-table-column field="Start_At" label="Thời gian bắt đầu" width="100" sortable>
                              {{ props.row.Start_At }}
                            </b-table-column>
                            <b-table-column field="End_At" label="Thời gian kết thúc" width="100" sortable>
                              {{ props.row.End_At }}
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

                            </b-field>
                            <!--room-->
                            <b-field group-multiline>
                              <b-table
                                :data="room.isRoomEmpty ? [] : room.room_record_data"
                                :loading="room.room_loading"
                                paginated
                                backend-pagination
                                detailed
                                :total="room.total"
                                :per-page="room.per_page"
                                @page-change="onRoomPageChange"
                                aria-next-label="Next page"
                                aria-previous-label="Previous page"
                                aria-page-label="Page"
                                aria-current-label="Current page"
                                backend-sorting
                                hoverable
                                bordered
                                detail-key="Room_ShiftID"
                                :opened-detailed="room.ID_Index"
                                :default-sort-direction="room.defaultSortOrder"
                                :default-sort="[room.sortField, room.sortOrder]"
                                @sort="onRoomSort"
                                @details-open="(row, index) => { currentRoomShiftID = row.Room_ShiftID ; currentRoomName = row.Exam_Room.RoomName;  getStudentRecord(); closeOtherDetails_Room(row, index) }"
                                @details-close="(row, index) => { student.student_record_data = [] }"
                                :show-detail-icon="true">
                                <template slot-scope="props">
                                  <b-table-column field="RoomID" label="Mã phòng" width="100" sortable>
                                    {{ props.row.Exam_Room.RoomID }}
                                  </b-table-column>
                                  <b-table-column field="RoomName" label="Phòng thi" width="100">
                                    {{ props.row.Exam_Room.RoomName }}
                                  </b-table-column>
                                  <b-table-column field="Maxcapacity" label="Số lượng máy tính" width="100">
                                    <p style="width: 25px; display: inline-block; text-align: center;">{{ props.row.Exam_Room.Maxcapacity }}</p> <b-icon icon-pack="fas" size="is-small" icon="laptop"></b-icon>
                                  </b-table-column>
                                </template>
                                <template slot="empty">
                                  <b-message type="is-danger" has-icon>
                                    Hiện tại chưa có dữ liệu phòng thi trong ca thi này, bạn hãy nhập vào phòng thi!
                                  </b-message>
                                </template>

                                <!--Student-->
                                 <template slot="detail" slot-scope="props">
                                    <h4 class="title is-4">Danh sách sinh viên</h4>
                                    <b-field expanded>
                                      <b-button
                                            :class="{'is-loading': student.student_loading}"
                                            class="button"
                                            @click="getStudentRecord">
                                        <b-icon size="is-small" icon="sync"/></b-button>
                                      <b-button v-if="student.student_record_data.length > 0" icon-left="file-pdf" @click="print">
                                        In danh sách sinh viên
                                      </b-button>
                                      <b-button v-else icon-left="file-pdf" disabled>
                                        In danh sách sinh viên
                                      </b-button>
                                    </b-field>
                                    <b-field>
                                        <b-table
                                              :data="student.isStudentEmpty ? [] : student.student_record_data"
                                              :loading="student.student_loading"
                                              backend-sorting
                                              bordered
                                              narrowed
                                              hoverable
                                              detail-key="ID"
                                              :default-sort-direction="student.defaultSortOrder"
                                              :default-sort="[student.sortField, student.sortOrder]"
                                              @sort="onStudentSort">
                                             <template slot-scope="props">
                                                <b-table-column field="ID" label="Mã số sinh viên" width="100" sortable>
                                                {{ props.row.ID }}
                                                </b-table-column>
                                                <b-table-column field="Fullname" label="Phòng thi" width="100" sortable>
                                                  {{ props.row.Fullname }}
                                                </b-table-column>
                                                <b-table-column field="Dob" label="Ngày sinh" width="100" sortable>
                                                 <span class="tag is-primary">
                                                    {{ formatDate(props.row.Dob) }}
                                                 </span>
                                                </b-table-column>
                                                <b-table-column field="CourseID" label="Lớp" width="100" sortable>
                                                  {{ props.row.CourseID }}
                                                </b-table-column>
                                                <b-table-column field="Gender" label="Giới tính" width="100" sortable >
                                                  <span>
                                                      <b-icon pack="fas"
                                                          :icon="props.row.Gender === 'Nam' ? 'mars' : 'venus'">
                                                      </b-icon>
                                                      {{ props.row.Gender }}
                                                  </span>
                                                </b-table-column>
                                              </template>
                                              <template slot="empty">
                                                <section class="section">
                                                  <b-message type="is-danger" has-icon>
                                                    Hiện tại chưa có sinh viên đăng kí phòng thi này!
                                                 </b-message>
                                                </section>
                                              </template>
                                        </b-table>
                                    </b-field>
                                  </template>
                                  <!--Student-->
                              </b-table>
                            </b-field>
                        </template>
                        <!--room-->
                        <template slot="empty">
                          <section class="section">
                            <b-message type="is-danger" has-icon>
                              Hiện tại chưa có thông tin về ca thi trong <b>{{ collapse.SemTitle }}</b>, bạn hãy nhập vào ca thi!
                            </b-message>
                          </section>
                        </template>
                    </b-table>
                    <!--Shift Record-->

                  </b-field >
                </div>
            </div>
        </b-collapse>
      </div>
      <div v-else>
        <b-field>
          <b-message type="is-danger" has-icon>
            <p>Hiện tại chưa có kỳ thi nào ở đây!</p>
            <p>Lưu ý! Ở đây chỉ hiển thị những kỳ thi đang <b>mở đăng ký!</b></p>
          </b-message>
        </b-field>
      </div>
    </section>
  </div>

</template>

<script>
    import axios from 'axios';
    import printJS from 'print-js';
    import moment from 'moment';
    import {authHeader} from "../../../api/jwt_handling";
    import debounce from 'lodash/debounce';
    import { eventBus } from "../../../../main";

    export default {
        name: 'export',
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
                select_search: Object,
                room_record_data: [],
                total: 0,
                // student_count: '',
                searchResults: [],
                room_loading: false,
                search_loading: false,
                sortField: 'RoomID',
                sortOrder: 'desc',
                defaultSortOrder: 'desc',
                page: 1,
                per_page: 5,
                ID_Index: [],
              },
              student: {
                isStudentEmpty: false,
                select_search: Object,
                student_record_data: [],
                total: 0,
                searchResults: [],
                student_loading: false,
                search_loading: false,
                sortField: 'ID',
                sortOrder: 'desc',
                defaultSortOrder: 'desc',
              },
              excel_export: {
                json_fields: {
                  "Mã sinh viên": "ID",
                  "Tên sinh viên":"Fullname",
                  "Ngày sinh": "Dob",
                  "Giới tính": "Gender",
                  "Lớp học": "CourseID"
                },
                json_data: [],
                file_name: ""
              },
              isOpen: null,
              collapses: [],
              currentShiftID: '', // current opening shiftID
              currentSemID: '', // current opening semesterID
              currentRoomShiftID: '', //current opening roomID
              currentRoomName: '', // for pdf title
              currentSubjectName: '', // for pdf title
              hasSemesterError: false,
              hasSubjectError: false,
              hasRoomError: false
            }
        },
        methods: {
            formatDate(date) {
                return moment(date).format('L');
            },
            async getSemesterRecordData() {
                this.semester.loading = true;
                try {
                    const response = await axios({
                        url: '/schedule/register-semester-records',
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
                        // console.log(this.semester.semester_record_data);
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
                        // console.log(response.data.total_results);
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
                this.getShiftRecordData();
            }, // xong
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
                        // console.log(response.data);
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
            async getStudentRecord() {
                this.student.student_loading = true;
                try {
                    const response = await axios({
                        url: '/schedule/student-records',
                        method: 'get',
                        params: {
                            currentRoomShiftID: this.currentRoomShiftID,
                            sort_field: this.student.sortField,
                            sort_order: this.student.sortOrder
                        },
                        headers: {
                            'Authorization': authHeader(),
                        }
                    });
                    // console.log(response.data.shift_records);
                    if (response.status === 200) {
                        this.student.student_record_data = [];
                        // this.room.student_count = response.data.total_results;
                        // console.log(response.data.total_results);
                        response.data.student_records.forEach((item) => {
                            this.student.student_record_data.push(item);
                        });
                        // console.log(this.room.student_count);
                        this.student.student_loading = false
                    }
                } catch (error) {
                    this.student.student_record_data = [];
                    this.student.total = 0;
                    this.student.student_loading = false;
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: 'Không thể lấy được dữ liệu sinh viên!',
                        position: 'is-bottom-right',
                        type: 'is-danger',
                        hasIcon: true
                    });
                    throw error;
                }
            }, // xong
            onStudentSort(field, order) {
                this.student.sortField = field;
                this.student.sortOrder = order;
                this.getStudentRecord();
            }, // xong
            destroySemesterData() { // destroy subject data for scalability when closing accordion
                this.shift.shift_record_data = [];
            },
            closeOtherDetails_Shift(row) {
                this.shift.ID_Index = [row.ShiftID];
                // console.log(this.student_status.ID_Index);
            },
            closeOtherDetails_Room(row) {
                this.room.ID_Index = [row.Room_ShiftID];
                // console.log(this.student_status.ID_Index);
            },
            print(){
              printJS({
                  printable: this.student.student_record_data,
                  properties: [
                          { field: 'ID', displayName: 'Mã số sinh viên'},
                          { field: 'Fullname', displayName: 'Tên sinh viên'},
                          { field: 'Dob', displayName: 'Ngày sinh'},
                          { field: 'Gender', displayName: 'Giới tính'},
                          { field: 'CourseID', displayName: 'Mã lớp học'}
                        ],
                  documentTitle: "Danh sách sinh viên tại phòng: " + this.currentRoomName + ' | Môn thi: ' + this.currentSubjectName,
                  headerStyle: 'font-weight: 300;',
                  repeatTableHeader: false,
                  type: 'json'
              })
            }
        },
        mounted() {
            this.getSemesterRecordData();
        },
        created() {
            eventBus.$on('up-to-date-semester', () => {
                this.getSemesterRecordData();
            })
        }
    }
</script>
