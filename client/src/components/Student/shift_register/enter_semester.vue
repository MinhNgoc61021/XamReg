<template>
    <div class="modal-card" style="height: 300px">
        <header class="modal-card-head">
            <p class="modal-card-title">Chọn kỳ thi</p>
        </header>

        <section class="modal-card-body">
          <b-autocomplete
            :data="search.searchResults"
            placeholder="Tìm kiếm và chọn tiêu đề kỳ thi"
            icon="search"
            field="SemTitle"
            :loading="search.searchLoading"
            @typing="onSemesterSearch"
            @select="option => { semester.semester_record = [option]; submitSemesterData() }"
            expanded required>
            <template slot-scope="props">
              <div class="media">
                <div class="media-content">
                  <b>Tiêu đề kỳ thi: </b>{{ props.option.SemTitle }}
                </div>
              </div>
            </template>
          </b-autocomplete>
        </section>

        <footer class="modal-card-foot">
            <button v-if="semester.currentSemesterID === ''" class="button" type="button" @click="go_home()">Về trang chủ</button>
            <button v-else class="button" type="button" @click="$parent.close()">Bỏ qua</button>
        </footer>
    </div>
</template>

<script>
import axios from "axios";
import {authHeader} from "../../api/jwt_handling";
import debounce from 'lodash/debounce';
import { mapState } from 'vuex';

export default {
  props: ['semesterID'],
  name: "enter_semester",
  data() {
    return {
      semester: {
          semester_record: [],
          currentSemesterID: this.semesterID,
      },
      search: {
        searchResults: [],
        searchLoading: false,
      }
    }
  },
  computed: {
      ...mapState([
          'ID',
      ]),
  },
  methods: {
    go_home() {
      this.$parent.close();
      this.$router.push({ name: 'student-info'})
    },
    async submitSemesterData() {
        // console.log(this.semester.semester_record[0]);
        this.$emit('loadSemesterShifts', this.semester.semester_record[0]);
        this.$parent.close();
    },
    onSemesterSearch: debounce(function (SemTitle) {
      this.search.searchLoading = true;
      if (SemTitle.length === 0) {
        this.search.searchResults = [];
        this.search.searchLoading = false;
      }
      else {
        this.search.searchResults = [];
        axios({
          url: '/shift-register/search-semester',
          method: 'get',
          headers: {
            'Authorization': authHeader(),
          },
          params: {
            searchID: SemTitle,
          },
        }).then((response) => {
          if (response.status === 200) {
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

<style scoped>
</style>
