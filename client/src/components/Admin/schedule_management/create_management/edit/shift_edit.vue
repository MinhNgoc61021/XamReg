<template>
  <form @submit.prevent="createShift()">
    <div class="modal-card" style="width: 450px;">
        <header class="modal-card-head">
            <p class="modal-card-title">Form chỉnh sửa</p>
        </header>
        <section class="modal-card-body">
          <b-field label="Phòng thi">
            <b-autocomplete
              :data="search.searchResults"
              placeholder="Hãy nhập phòng thi"
              field="RoomName"
              :loading="search.searchLoading"
              @typing="onRoomSearch"
              @select="option => newRoomID = option.RoomID"
              expanded>
                <template slot-scope="props">
                  <div class="media">
                    <div class="media-content">
                      <b>Mã phòng: </b>{{ props.option.RoomID }}
                      <br>
                      <b>Tên phòng: </b>{{ props.option.RoomName }}
                    </div>
                  </div>
                </template>
            </b-autocomplete>
          </b-field>

          <b-field label="Ngày thi">
              <b-datepicker v-model="Date_Start" placeholder="Hãy nhập ngày thi" required></b-datepicker>
          </b-field>

          <b-field label="Giờ bắt đầu thi">
              <b-timepicker
                  v-model="Start_At"
                  placeholder="Hãy nhập giờ thi"
                  icon="clock" required>
              </b-timepicker>
          </b-field>


        </section>
    </div>
    <footer class="modal-card-foot">
          <button class="button" type="button" @click="$parent.close()">Bỏ qua</button>
          <button class="button is-primary" type="submit">Tạo</button>
      </footer>
  </form>
</template>

<script>
    import axios from "axios";
    import debounce from 'lodash.debounce';
    import moment from 'moment/moment';
    import {authHeader} from "../../../../api/jwt_handling";

    export default {
        name: "shift_edit",
        props: ['currentSubjectID'],
        data() {
          return {
              SubjectID: this.currentSubjectID,
              newRoomID: '',
              Date_Start: null,
              Start_At: null,
              search: {
                    searchResults: [],
                    searchLoading: false,
              },
          }
        },
        methods: {
            async updateShift() {
                try {
                  const update = await axios({
                    method: 'post',
                    url: '/schedule/edit-shift',
                    headers: {
                      'Authorization': authHeader(),
                    },
                    data: {
                        RoomID: this.newRoomID,
                        SubjectID: this.SubjectID,
                        Date_Start: moment(this.Date_Start).format('YYYY-MM-DD'),
                        Start_At: moment(this.Start_At).format("YYYY-MM-DD HH:mm:ss"),
                    },
                  });
                  if (update.status === 200) {
                    this.$emit('loadShifts', 200);
                    this.$parent.close();
                    if (update.data.status === 'success') {
                      this.$buefy.notification.open({
                        duration: 2500,
                        message: `Ca thi đã được tạo thành công!`,
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                      });
                    }
                  }
                } catch (e) {
                  if (e['message'].includes('400')) {
                    this.$emit('loadShifts', 400);
                  } else if (e['message'].includes('401')) {
                    this.$emit('loadShifts', 401);
                  }
                }
            },
            onRoomSearch: debounce(function (roomName) {
                this.search.searchLoading = true;
                if (roomName.length === 0) {
                    this.search.searchResults = [];
                    this.search.searchLoading = false;
                }
                else {
                    this.search.searchResults = [];
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
        }
    }
</script>
