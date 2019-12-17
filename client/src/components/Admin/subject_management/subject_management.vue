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

            <b-button
              class="button"
              @click="getSubjectInfo"
              :class="{'is-loading': subject_info.loading}"
            >
              <b-icon
                size="is-small"
                icon="sync"/>
              <span>Làm mới</span>
            </b-button>

            <b-select v-model="subject_info.per_page">
              <option value="5">5 dòng/trang</option>
              <option value="10">10 dòng/trang</option>
              <option value="15">15 dòng/trang</option>
              <option value="20">20 dòng/trang</option>
            </b-select>

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
        <b-field v-if="subject_info.subject_record.length > 0">
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
              <b-table-column field="SubjectID" label="Mã môn học" sortable width="200px">
                {{props.row.SubjectID}}
              </b-table-column>
              <b-table-column field="SubjectTitle" label="Tên môn học" sortable  width="200px">
                {{props.row.SubjectTitle}}
              </b-table-column>
              <b-table-column field="Action"  width="90px">
                <b-button type="is-warning" size="is-small" icon-pack="fas" icon-right="edit" outlined @click.prevent="onStatusEdit(props.row)"></b-button>
                <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onStatusDelete(props.row)"></b-button>
              </b-table-column>
            </template>
          </b-table>
        </b-field>
        <b-field v-else>
        </b-field>
    </section>
  </div>
</template>

<script>
    import axios from 'axios'
    import { authHeader} from "../../api/jwt_handling";
    import subject_edit from "./edit/subject_edit";
    import subject_create from "./create/subject_create";
    import debounce from 'lodash/debounce';
    export default {
        name: "subject_management",
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
          async getSubjectInfo() {
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
                  message: 'Không thể lấy được dữ liệu về môn thi!',
                  position: 'is-bottom-right',
                  type: 'is-danger',
                  hasIcon: true,
              });
              throw error;
            }
          },
          onSubjectPageChange(page) {
            this.subject_info.page = page;
            this.getSubjectInfo();
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
          onStatusSort(field, order) {
                this.subject_info.sortField = field;
                this.subject_info.sortOrder = order;
                this.getSubjectInfo();
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
                         message: `Đã tạo môn thi thành công!`,
                         position: 'is-bottom-right',
                         type: 'is-success',
                         hasIcon: true
                       });
                       this.getSubjectInfo();
                     }
                     else if (http_status === 202) {
                       this.$buefy.notification.open({
                         duration: 2000,
                         message: `Môn thi này đã tồn tại từ trước!`,
                         position: 'is-bottom-right',
                         type: 'is-warning',
                         hasIcon: true
                       });
                       this.getSubjectInfo();
                     }
                     else if (http_status === 400) {
                       this.$buefy.notification.open({
                         duration: 2000,
                         message: 'Kiểm tra lại, dữ liệu bạn nhập đang không đúng!',
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
              message: `Bạn có chắc chắn là muốn <b>xóa</b> môn học ${row.SubjectID} này không? Đã làm là tự chịu đấy.`,
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
                      message: `Đã xóa thành công môn học.`,
                      position: 'is-bottom-right',
                      type: 'is-success',
                      hasIcon: true
                    });
                  }
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
                } finally {
                  this.getSubjectInfo();
                }
              },
            });
          },
          onStatusEdit(row) {
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
                     this.getSubjectInfo();
                   }
                   else if (http_status === 202) {
                     this.$buefy.notification.open({
                       duration: 2000,
                       message: `Tên hoặc mã môn của môn học này đang bị trùng với của môn khác!`,
                       position: 'is-bottom-right',
                       type: 'is-warning',
                       hasIcon: true
                     });
                   }
                   else if (http_status === 400) {
                     this.$buefy.notification.open({
                       duration: 2000,
                       message: 'Kiểm tra lại, dữ liệu bạn nhập đang không đúng!',
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
          this.getSubjectInfo();
      }
    }
</script>

<style scoped>
</style>
