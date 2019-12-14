<template>
    <form @submit.prevent="submitSemesterData()">
    <div class="modal-card" style="width: 450px; height: 300px">
        <header class="modal-card-head">
            <p class="modal-card-title">Nhập tên kỳ thi</p>
        </header>

      <section class="modal-card-body">
        <b-autocomplete
          :data="search.searchResults"
          placeholder="Nhập tên kỳ thi"
          icon="search"
          field="SemTitle"
          :loading="search.searchLoading"
          @typing="onSemesterSearch"
          @select="option => semester.semester_record = [option]"
        expanded required>
          <template slot-scope="props">
            <div class="media">
              <div class="media-left">
                <b-icon icon-pack="fas" icon="file-search"></b-icon>
              </div>
              <div class="media-content">
                <b>Tên kỳ thi: </b>{{ props.option.SemTitle }}
              </div>
            </div>
          </template>
        </b-autocomplete>
      </section>

      <footer class="modal-card-foot">
          <button class="button" type="button" @click="go_home()">Về trang chủ</button>
          <button class="button is-primary" type="submit">Xác nhận</button>
      </footer>
    </div>
  </form>
</template>

<script>
import axios from "axios";
import {authHeader} from "../../api/jwt_handling";
import debounce from 'lodash/debounce';
export default {
  name: "enter_semester",
  data() {
    return {
      semester: {
        semester_record: []
      },
      search: {
        searchResults: [],
        searchLoading: false,
      }
    }
  },
  methods: {
    go_home() {
      this.$parent.close();
      this.$router.push({ path: '/student-home' })
    },
    async submitSemesterData() {
        if (this.semester_record !== []) {
          this.$emit('loadSemesterShifts', this.semester.semester_record[0]);
          this.$parent.close();
        }
        else {
            this.go_home();
        }
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
