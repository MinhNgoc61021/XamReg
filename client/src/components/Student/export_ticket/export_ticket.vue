<template>
  <div>
    <h1 class="title is-3">In phiếu báo dự thi</h1>
    <h2 class="subtitle is-6">Xem, hủy và in phiếu báo dự thi</h2>
    <hr>
    <b-field group-multiline>

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
      <b-button icon-left="file-pdf" v-if="register_result.length > 0" @click="print">
        In phiếu báo dự thi
      </b-button>
      <b-button icon-left="file-pdf" v-else disabled @click="print">
        In phiếu báo dự thi
      </b-button>
    </b-field>
    <div id = "printTickets">
       <div class="row" v-if="register_result.length > 0" >
          <div class="column" v-for="item in register_result">
            <div class="card">
              <div style="padding: 10px; margin: 10px;">
                <p><b>MSSV: </b> {{ studentid }}</p>
                <p><b>Mã ca thi: </b>{{ item.Shift.ShiftID }}</p>
                <p><b>Môn thi: </b>{{ item.Shift.Subject.SubjectID }} | {{ item.Shift.Subject.SubjectTitle }}</p>
                <p><b>Phòng thi:</b> {{ item.Exam_Room.RoomName}}</p>
                <p><b>Ngày thi:</b> {{ formatDate(item.Shift.Date_Start) }}</p>
                <p><b>{{ item.Shift.Start_At }} - {{ item.Shift.End_At }}</b></p>
              </div>
              <div id="deleteRegister">
                <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onDelete(item)"></b-button>
              </div>
            </div>
          </div>
         </div>
        <b-field v-else>
          <b-message type="is-danger" has-icon>
            Hiện tại chưa có dữ liệu ca thi đã đăng kí, yêu cầu sinh viên hãy đăng kí thêm!
          </b-message>
        </b-field>
    </div>

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
                  // console.log(response.data);
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
            async onDelete(item) {
              this.$buefy.dialog.confirm({
                  title: 'Hủy ca thi',
                  message: `Bạn có chắc chắn là muốn <b>hủy</b> ca thi số ${item.Shift.ShiftID} này không? Đã làm thì tự chịu đấy.`,
                  confirmText: 'Hủy!',
                  cancelText: 'Bỏ qua',
                  type: 'is-danger',
                  hasIcon: true,
                  onConfirm: async () => {
                      try {
                          const removeData = await axios({
                              url: '/shift-register/remove-export-records',
                              method: 'delete',
                              headers: {
                                'Authorization': authHeader(),
                              },
                              data: {
                                delRegisterID: item['Student_Shift'][0]['RegisterID'],
                              },
                          });
                          if (removeData.status === 200) {
                              this.$buefy.notification.open({
                                duration: 2000,
                                message: `Đã hủy ca thi đăng kí thành công.`,
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
                });
            },
            print(){
              this.isPrinting = true;
              printJS({
                  printable: 'printTickets',
                  // properties: [
                  //         { field: 'ID', displayName: 'Mã số sinh viên'},
                  //         { field: 'Fullname', displayName: 'Tên sinh viên'},
                  //         { field: 'Dob', displayName: 'Ngày sinh'},
                  //         { field: 'Gender', displayName: 'Giới tính'},
                  //         { field: 'CourseID', displayName: 'Mã lớp học'}
                  //       ],
                  documentTitle : "PHIẾU BÁO DỰ THI",
                  css : "../../css/ticket.css",
                  scanStyles: true,
                  ignoreElements: ['deleteRegister'],
                  targetStyles: ['*'],
                  type: 'html'
              })
            }
        },
          mounted() {
            this.getRecord()
          }
    }
</script>
<style src="../../css/ticket.css" scoped></style>
