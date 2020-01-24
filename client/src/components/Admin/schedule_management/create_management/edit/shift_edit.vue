<template>
  <form @submit.prevent="updateShift()">
    <div class="modal-card has-mobile-cards">
        <header class="modal-card-head">
            <p class="modal-card-title">Form chỉnh sửa</p>
        </header>
        <section class="modal-card-body">
          <b-field label="Ngày thi">
              <b-datepicker v-model="Date_Start" placeholder="Hãy nhập ngày thi" required></b-datepicker>
          </b-field>

          <b-field label="Môn thi">
            <b-autocomplete
              icon="search"
              type="text"
              :data="search.searchResults"
              placeholder="Tìm kiếm mã môn thi để nhập"
              validation-message="Nhập đúng mã môn thi"
              field="SubjectID"
              :value="SubjectID"
              v-model="SubjectID"
              :loading="search.searchLoading"
              @typing="onSubjectSearch"
              @select="option =>  optionedSubject = [option]"
              expanded required>
                <template slot-scope="props">
                    <div class="media">
                        <div class="media-left">
                          <b-icon icon-pack="fas" icon="book"></b-icon>
                        </div>
                        <div class="media-content">
                          <div><b>Mã môn học: </b>{{ props.option.SubjectID }}</div>
                          <div><b>Tên môn học: </b>{{ props.option.SubjectTitle }}</div>
                        </div>
                    </div>
                </template>
            </b-autocomplete>
          </b-field>

          <b-field label="Giờ bắt đầu thi">
              <b-timepicker
                  v-model="Start_At"
                  :value="Start_At"
                  placeholder="Hãy nhập giờ thi"
                  icon="clock" required>
              </b-timepicker>
          </b-field>

          <b-field label="Giờ kết thúc thi">
              <b-timepicker
                  v-model="End_At"
                  :value="End_At"
                  placeholder="Hãy nhập giờ thi"
                  icon="clock" required>
              </b-timepicker>
          </b-field>

        </section>
        <footer class="modal-card-foot">
            <button class="button" type="button" @click="$parent.close()">Bỏ qua</button>
            <button class="button is-primary" type="submit">Cập nhật</button>
        </footer>
    </div>
  </form>
</template>

<script>
    import axios from "axios";
    import debounce from 'lodash.debounce';
    import moment from 'moment/moment';
    import {authHeader} from "../../../../api/jwt_handling";

    export default {
        name: "shift_edit",
        props: ['currentShiftID', 'currentSemID', 'currentStart_At', 'currentEnd_At' ,'currentDate_Start', 'currentSubjectID'],
        data() {
          return {
              SemID: this.currentSemID,
              ShiftID: this.currentShiftID,
              SubjectID: this.currentSubjectID,
              Date_Start: this.currentDate_Start,
              Start_At: this.currentStart_At,
              End_At:  this.currentEnd_At,
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
                    method: 'put',
                    url: '/schedule/edit-shift',
                    headers: {
                      'Authorization': authHeader(),
                    },
                    data: {
                        SemID: this.SemID,
                        ShiftID: this.ShiftID,
                        newSubjectID: this.SubjectID,
                        newDate_Start: moment(this.Date_Start).format('YYYY-MM-DD'),
                        newStart_At: moment(this.Start_At).format("HH:mm:ss"),
                        newEnd_At: moment(this.End_At).format('HH:mm:ss'),
                    },
                  });
                  if (update.status === 200) {
                      this.$emit('editShift', 200);
                      this.$parent.close();
                  }
                  else if (update.data.status === 'time-false') {
                        this.$emit('editShift', '202-time-false');
                    }
                  else if (update.data.status === 'already-exist-subject') {
                      this.$emit('editShift', '202-already-exist-subject');
                  }
                } catch (e) {
                  if (e['message'].includes('400')) {
                    this.$emit('editShift', 400);
                  } else if (e['message'].includes('401')) {
                    this.$emit('editShift', 401);
                  }
                }
            },
            onSubjectSearch: debounce(function (SubjectID) {
                this.search.searchLoading = true;
                if (SubjectID.length > 15 || SubjectID.length === 0) {
                  this.search.searchResults = [];
                  this.search.searchLoading = false;
                }
                else {
                  this.search.searchResults = [];
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
