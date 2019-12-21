<template>
  <div>
    <h1 class="title is-3">Danh sách ca thi đã đăng kí</h1>
    <h2 class="subtitle is-6">Xem & xóa ca thi đã đăng kí</h2>
    <b-field grouped group-multiline>

      <b-button
        class="button"
        @click="getRecord"
        :class="{'is-loading': loading}"
      >
        <b-icon
          size="is-small"
          icon="sync"/>
        <span>Làm mới</span>
      </b-button>

    </b-field>
    <b-field v-if="register_result.length > 0">
      <b-table
        :data="register_result"
        :loading="loading"
        :bordered="true">
          <template slot-scope="props">
            <b-table-column field="ShiftID" label="Ca thi số" width="100">
              {{ props.row.Shift.ShiftID }}
            </b-table-column>
            <b-table-column field="SubjectTitle" label="Môn thi">
              <b>{{ props.row.Shift.Subject.SubjectID }} | {{ props.row.Shift.Subject.SubjectTitle }}</b>
            </b-table-column>
            <b-table-column field="Date_Start" label="Ngày thi">
              <span class="tag is-success">
                {{ formatDate(props.row.Shift.Date_Start) }}
              </span>
            </b-table-column>
            <b-table-column field="Start_At" label="Ca thi bắt đầu">
              {{ props.row.Shift.Start_At }}
            </b-table-column>
            <b-table-column field="End_At" label="Ca thi kết thúc">
              {{ props.row.Shift.End_At }}
            </b-table-column>
            <b-table-column field="RoomName" label="Phòng thi">
              {{ props.row.Exam_Room.RoomName}}
            </b-table-column>
             <b-table-column field="Action" width="100">
               <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onDelete(props.row)"></b-button>
            </b-table-column>
          </template>
      </b-table>
    </b-field>
    <b-field v-else>
      <b-message type="is-danger" has-icon>
        Hiện tại chưa có dữ liệu ca thi đã đăng kí, yêu cầu sinh viên hãy đăng kí thêm!
      </b-message>
    </b-field>
  </div>
</template>

<script>
    import axios from 'axios';
    import {authHeader} from "../../api/jwt_handling";
    import moment from 'moment';

    export default {
        name: 'export-ticket',
        props: ['studentid'],
        data() {
            return {
              loading: false,
              register_result: [],
              // room_data: {'RoomID' : '',
              //             'RoomName' : '',
              //             'Maxcapacity' : ''},
              // subject_data: {'SubjectID' : '',
              //                'SubjectTitle' : ''},
              // shift_data: {'ShifID' : '',
              //              'Start_At' : '',
              //              'Date_Start' : '',
              //              'End_At' : ''}
            }
        },
        methods: {
            formatDate(date) {
                return moment(date).format('L');
            },
            async getRecord() {
              this.loading = true;
              try {
                const response = await axios({
                  url: '/shift-register/export-records',
                  method: 'get',
                  params: {
                    studentID: this.studentid,
                  },
                  headers: {
                    'Authorization': authHeader(),
                  }
                });
                if (response.status === 200) {
                  this.register_result = [];
                  // this.register_result = response.data.result_records;
                  response.data.result_records.forEach((item) => {
                        this.register_result.push(item);
                      });
                  this.loading = false;
                  console.log(response.data);
                  // const subject_data = response.data.result_records['Shift']['Subject'];
                  // this.subject_data['SubjectID'] = subject_data['SubjectID'];
                  // this.subject_data['SubjectTitle'] = subject_data['SubjectTitle'];
                  // console.log(this.subject_data);
                  // const room_data = response.data.result_records['Exam_Room'];
                  // this.room_data['RoomID'] = room_data['RoomID'];
                  // this.room_data['RoomName'] = room_data['RoomName'];
                  // this.room_data['Maxcapacity'] = room_data['Maxcapacity'];
                  // console.log(this.room_data);
                  // const shift_data = response.data.result_records['Shift'];
                  // this.shift_data['ShifID'] = shift_data['ShifID'];
                  // this.shift_data['Start_At'] = shift_data['Start_At'];
                  // this.shift_data['Date_Start'] = shift_data['Date_Start'];
                  // this.shift_data['End_At'] = shift_data['End_At'];
                  // console.log(this.shift_data);
                }
              }
              catch (error) {
                this.register_result = [];
                this.loading = false;
                this.$buefy.notification.open({
                  duration: 2000,
                  message: 'Không thể lấy được dữ liệu !',
                  position: 'is-bottom-right',
                  type: 'is-danger',
                  hasIcon: true
                });
                throw error;
              }
            },
            async onDelete(row) {
              try {
                const removeData = await axios({
                  url: '/shift-register/remove-export-records',
                  method: 'delete',
                  headers: {
                    'Authorization': authHeader(),
                  },
                  data: {
                    delRegisterID: row['Student_Shift'][0]['RegisterID'],
                  },
                });
                if (removeData.status === 200) {
                  this.$buefy.notification.open({
                    duration: 2000,
                    message: `Đã xóa ca thi đăng kí thành công.`,
                    position: 'is-bottom-right',
                    type: 'is-success',
                    hasIcon: true
                  });
                }
                this.getRecord();
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
            }
        },
          mounted() {
            this.getRecord()
          }
    }
</script>
