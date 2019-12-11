<template>
  <div class="container">
    <h1 class="title is-3">Quản lý môn thi</h1>
    <h2 class="subtitle is-6">Cập nhật, quản lý thông tin của môn thi</h2>

    <section>
      <b-field grouped group-multiline >
            <b-button
              class="button"
              @click="createSubject"
              icon-pack="fas" icon-left="plus-square"
            >
              <span>Tạo môn</span>
            </b-button>

            <b-select v-model="subject_info.per_page">
              <option value="5">5 dòng/trang</option>
              <option value="10">10 dòng/trang</option>
              <option value="15">15 dòng/trang</option>
              <option value="20">20 dòng/trang</option>
            </b-select>

            <b-button
              class="button"
              @click="getSubjectsInfo"
            >
              <b-icon
                size="is-small"
                icon="sync"/>
              <span>Làm mới</span>
            </b-button>

            <b-autocomplete
                :data="search.searchResults"
                placeholder="Tìm kiếm bằng mã môn học"
                icon="search"
                field="SubjectID"
                :loading="search.searchLoading"
                @typing="onSubjectSearch"
                @select="option => subject_info.subject_record = [option]"
                expanded>
              <template slot-scope="props">
                    <div class="media">
                        <div class="media-left">
                          <b-icon icon-pack="fas" icon="file-search"></b-icon>
                        </div>
                        <div class="media-content">
                            <b>Mã môn học: </b>{{ props.option.SubjectID }}
                            <br>
                            <b>Tên môn học: </b>{{ props.option.SubjectTitle }}
                        </div>
                    </div>
                </template>
            </b-autocomplete>
        </b-field>
        <b-table
          :data="subject_info.subject_record"
          :loading="subject_info.loading"
          paginated
          backend-pagination
          :total="subject_info.total"
          :per-page="subject_info.per_page"
          @page-change="onSubjectPageChange"
          aria-next-label="Next page"
          aria-previous-label="Previous page"
          aria-page-label="Page"
          aria-current-label="Current page"
          backend-sorting
          hoverable
          :default-sort-direction="subject_info.defaultSortOrder"
          :default-sort="[subject_info.sortField, subject_info.sortOrder]"
          @sort="onStatusSort"
        >
          <template slot-scope="props" style="width: 500px">
            <b-table-column field="SubjectID" label="Mã môn học" sortable>
              {{props.row.SubjectID}}
            </b-table-column>
            <b-table-column field="SubjectTitle" label="Tên môn học" sortable>
              {{props.row.SubjectTitle}}
            </b-table-column>
            <b-table-column field="Action">
              <b-button type="is-warning" size="is-small" icon-pack="fas" icon-right="edit" outlined @click.prevent="onStatusEdit(props.row)"></b-button>
              <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onStatusDelete(props.row)"></b-button>
            </b-table-column>
          </template>
        </b-table>


    </section>
  </div>
</template>

<script>
    import axios from 'axios'
    import { authHeader} from "../../api/jwt_handling";
    import subject_edit from "./subject_create";
    import subject_create from "./subject_create";
    import debounce from 'lodash/debounce';
    export default {
        name: "subjects_management",
        component: {
          subject_edit,
        },
        data() {
          return {
            subject_info: {
              subject_record: [],
              total: 0,
              loading: false,
              sortField: 'SubjectID',
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
        methods: {
          async getSubjectsInfo() {
            this.subject_info.loading = true;
            try {
              const response = await axios({
                url:'/subject/subject-records',
                method:'get',
                params: {
                  page_index: this.subject_info.page,
                  per_page: this.subject_info.per_page,
                  sort_field: this.subject_info.sortField,
                  sort_order: this.subject_info.sortOrder
                },
                headers: {
                  'Authorization': authHeader()
                },
              });
              if (response.status === 200) {
                this.subject_info.subject_record = [];
                this.subject_info.total = response.data.total_results;
                response.data.records.forEach((item) => {
                  this.subject_info.subject_record.push(item);
                });
                this.subject_info.loading = false;
              }
            } catch (error) {
              this.subject_info.subject_record = [];
              this.subject_info.total = 0;
              this.subject_info.loading = false;
              this.$buefy.notification.open({
                duration: 2000,
                message: 'Chịu, đ lấy đc',
                position: 'is-bottom-right',
                type: 'is-danger',
              });
              throw error;
            }
          },
          onSubjectPageChange(page) {
            this.subject_info.page = page;
            this.getSubjectsInfo();
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
          onStatusSort(field, order) {
                this.subject_info.sortField = field;
                this.subject_info.sortOrder = order;
                this.getSubjectsInfo();
          },
          createSubject() {
            this.$buefy.modal.open({
              parent: this,
              component: subject_create,
              hasModalCard: true,
              customClass: 'custom-class custom-class-2',
              canCancel: false,
              events: {
                 'loadSubjects': (http_status) => {
                   if (http_status === 200) {
                     this.$buefy.notification.open({
                       duration: 2000,
                       message: `Đã tạo môn học thành công!`,
                       position: 'is-bottom-right',
                       type: 'is-success',
                       hasIcon: true
                     });
                     this.getSubjectsInfo();
                   }
                   else if (http_status === 400) {
                     this.$buefy.notification.open({
                       duration: 2000,
                       message: 'Các bạn nộp rác cho t àk ?!',
                       position: 'is-bottom-right',
                       type: 'is-danger',
                       hasIcon: true
                     });
                   }
                   else if (http_status === 401) {
                     this.$buefy.notification.open({
                       duration: 2000,
                       message: 'Không được quyền sử dụng!',
                       position: 'is-bottom-right',
                       type: 'is-danger',
                       hasIcon: true
                     });
                   }
                 }
              }
            })
          },
          async onStatusDelete(row) {
            this.$buefy.dialog.confirm({
              title: 'Xóa môn học',
              message: `Bạn có chắc chắn là muốn <b>xóa</b> môn học ${row.SubjectID} này không?`,
              confirmText: 'Xóa!',
              cancelText: 'Hủy bỏ',
              type: 'is-danger',
              hasIcon: true,
              onConfirm: async () => {
                try {
                  const removeData = await axios({
                    url: '/subject/remove-subject',
                    method: 'delete',
                    headers: {
                      'Authorization': authHeader(),
                    },
                    data: {
                      delSubjectID: row.SubjectID,
                    },
                  });
                  if (removeData.status === 200) {
                    this.$buefy.notification.open({
                      duration: 2000,
                      message: `<b>Đã xóa thành công môn học</b>.`,
                      position: 'is-bottom-right',
                      type: 'is-success',
                      hasIcon: true
                    });
                  }
                } catch (e) {
                  if (e['message'].includes('401')) {
                    this.$buefy.notification.open({
                      duration: 2000,
                      message: 'HTTP Status 401: Không được quyền sử dụng!',
                      position: 'is-bottom-right',
                      type: 'is-danger',
                      hasIcon: true
                    })
                  }
                } finally {
                  this.getSubjectsInfo();
                }
              },
            });
          },
          onStatusEdit(row) {
            console.log(row);
             this.$buefy.modal.open({
               parent: this,
               component: subject_edit,
               props: {
                 currentSubjectID: row.SubjectID,
                 currentSubjectTitle: row.SubjectTitle
               },
               hasModalCard: true,
               customClass: 'custom-class custom-class-2',
               canCancel: false,
               events: {
                 'loadSubjects': (http_status) => {
                   if (http_status === 200) {
                     this.$buefy.notification.open({
                       duration: 2000,
                       message: `Đã sửa đổi thành công!`,
                       position: 'is-bottom-right',
                       type: 'is-success',
                       hasIcon: true
                     });
                     this.getSubjectsInfo();
                   }
                   else if (http_status === 400) {
                     this.$buefy.notification.open({
                       duration: 2000,
                       message: 'Các bạn nộp rác cho t àk ?!',
                       position: 'is-bottom-right',
                       type: 'is-danger',
                       hasIcon: true
                     });
                   }
                   else if (http_status === 401) {
                     this.$buefy.notification.open({
                       duration: 2000,
                       message: 'Không được quyền sử dụng!',
                       position: 'is-bottom-right',
                       type: 'is-danger',
                       hasIcon: true
                     });
                   }
                  }
               }
             })
          }
        },
      mounted() {
          this.getSubjectsInfo();
      }
    }
</script>

<style scoped>
</style>
