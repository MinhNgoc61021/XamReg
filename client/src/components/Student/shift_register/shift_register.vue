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
            icon="edit"/>
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
                <b>Mã ca thi: </b>{{ props.option.ShiftID }}
                <br>
                <b>Mã môn học: </b>{{ props.option.SubjectID }}
              </div>
            </div>
          </template>
        </b-autocomplete>
      </b-field>

      <b-table
            :data="shift.shift_record_data"
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
            hoverable
            :default-sort-direction="shift.defaultSortOrder"
            :default-sort="[shift.sortField, shift.sortOrder]"
            @sort="onStatusSort"
      >
        <template slot-scope="props">
          <b-table-column field="ShiftID" label="Mã ca thi" sortable>
            {{ props.row.ShiftID }}
          </b-table-column>

          <b-table-column field="SubjectID" label="Môn thi" sortable>
            <b></b>{{ props.row.Subject.SubjectID }} | {{ props.row.Subject.SubjectTitle }}
          </b-table-column>

          <b-table-column field="Date_Start" label="Ngày thi" sortable>
            {{ props.row.Date_Start }}
          </b-table-column>

          <b-table-column field="Start_At" label="Giờ bắt đầu" sortable>
            {{ props.row.Start_At }}
          </b-table-column>

          <b-table-column field="End_At" label="Giờ kết thúc" sortable>
            {{ props.row.End_At }}
          </b-table-column>
        </template>
      </b-table>

      <b-table
          :data="shift.registered_shift"
          :loading="shift.loading"
          backend-sorting
          hoverable
          :default-sort-direction="shift.defaultSortOrder"
          :default-sort="[shift.sortField, shift.sortOrder]"
          @sort="onStatusSort"
        >
          <template slot-scope="props">
          <b-table-column field="ShiftID" label="Mã ca thi" sortable>
            {{ props.row.ShiftID }}
          </b-table-column>

          <b-table-column field="SubjectID" label="Môn thi">
            <b>{{ props.row.Subject.SubjectID }} | {{ props.row.Subject.SubjectTitle }}</b>
          </b-table-column>

          <b-table-column field="Date_Start" label="Ngày thi" sortable>
            {{ props.row.Date_Start }}
          </b-table-column>

          <b-table-column field="Start_At" label="Giờ bắt đầu" sortable>
            {{ props.row.Start_At }}
          </b-table-column>

          <b-table-column field="End_At" label="Giờ kết thúc" sortable>
            {{ props.row.End_At }}
          </b-table-column>
        </template>
        </b-table>
    </div>
</template>

<script>
    import axios from "axios";
    import {authHeader} from "../../api/jwt_handling";
    import enter_semester from "./enter_semester";
    import { mapActions, mapState } from 'vuex';
    export default {
        name: 'shift-register',
        data() {
            return {
                semester: {
                  semester_record: []
                },
                shift: {
                    shift_record_data: [],
                    registered_shift: [],
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
            async getShiftRecordData() {
              this.shift.shift_loading = true;
                  try {
                      const response = await axios({
                          url: '/shift-register/shift-records',
                          method: 'get',
                          params: {
                              SemID: this.semester.semester_record.SemID,
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
                          console.log(response.data.shift_records);
                          response.data.shift_records.forEach((item) => {
                              this.shift.shift_record_data.push(item);
                              console.log('ca thi ở đây:', item);
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
            onShiftSearch() {
            },
            onShiftPageChange(page) {
              this.shift.page = page;
              this.getShiftRecordData();
            },
            onStatusSort(field, order) {
              this.shift.sortField = field;
              this.shift.sortOrder = order;
            },
        },
        mounted() {
            if (this.currentSemesterID === '') {
                this.$buefy.modal.open({
                  parent: this,
                  component: enter_semester,
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
                          message: `Đã nhập thành công!`,
                          position: 'is-bottom-right',
                          type: 'is-success',
                          hasIcon: true
                        });
                      } else if (semester_record.SemTitle === '') {
                        this.$buefy.notification.open({
                          duration: 2000,
                          message: 'Sửa đổi không thành công!',
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
            }
            else {
                this.semester.semester_record.SemID = this.currentSemesterID;
                this.getShiftRecordData();
            }
        },
    }
</script>
