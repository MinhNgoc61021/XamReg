<template>
  <form @submit.prevent="createShift()">
    <div class="modal-card" style="width: 450px;">
        <header class="modal-card-head">
            <p class="modal-card-title">Form tạo ca thi</p>
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
              placeholder="Tìm kiếm để nhập môn thi"
              field="SubjectID"
              :loading="search.searchLoading"
              @typing="onSubjectSearch"
              @select="option =>  optionedSubject = [option]"
              expanded>
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
                  placeholder="Hãy nhập giờ bắt đầu"
                  icon="clock" required>
              </b-timepicker>
          </b-field>

          <b-field label="Giờ kết thúc thi">
              <b-timepicker
                  v-model="End_At"
                  placeholder="Hãy nhập giờ kết thúc"
                  icon="clock" required>
              </b-timepicker>
          </b-field>

        </section>
        <footer class="modal-card-foot">
            <button class="button" type="button" @click="$parent.close()">Bỏ qua</button>
            <button class="button is-primary" type="submit">Tạo</button>
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
        name: "shift_create",
        props: ['currentSemesterID'],
        data() {
          return {
              optionedSubject: '',
              Date_Start: null,
              Start_At: null,
              End_At: null,
              search: {
                    searchResults: [],
                    searchLoading: false,
              },
          }
        },
        methods: {
            async createShift() {
                try {
                    console.log(this.optionedSubject[0]);
                  const response = await axios({
                    method: 'post',
                    url: '/schedule/create-shift',
                    headers: {
                      'Authorization': authHeader(),
                    },
                    data: {
                        semID: this.currentSemesterID,
                        subjectID: this.optionedSubject[0].SubjectID,
                        date_start: moment(this.Date_Start).format('YYYY-MM-DD'),
                        start_at: moment(this.Start_At).format("HH:mm:ss"),
                        end_at: moment(this.End_At).format("HH:mm:ss"),
                    },
                  });
                    if (response.data.status === 'success') {
                        this.$parent.close();
                        this.$emit('loadShifts', 200);
                    }
                    else {
                        this.$emit('loadShifts', 208);
                    }
                } catch (e) {
                  if (e['message'].includes('400')) {
                    this.$emit('loadShifts', 400);
                  } else if (e['message'].includes('401')) {
                    this.$emit('loadShifts', 401);
                  }
                }
            },
            onSubjectSearch: debounce(function (SubjectID) {
                this.search.searchLoading = true;
                if (SubjectID.length > 7 || SubjectID.length === 0) {
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
