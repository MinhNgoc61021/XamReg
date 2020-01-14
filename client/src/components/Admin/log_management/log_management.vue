<template>
      <div class="container">
          <h1 class="title is-3">Quản lý nhật ký</h1>
          <h2 class="subtitle is-6">Xem, quản lý hành vi và hoạt động của từng người dùng</h2>
          <hr>
          <b-field grouped group-multiline>
              <b-button
                v-if="log_data.length !== 0"
                :class="{'is-loading': loading}"
                class="button"
                @click="getLogRecordData"
              >
                <b-icon
                  size="is-small"
                  icon="sync"/>
                <span>Làm mới</span>
              </b-button>
              <b-button
                v-else
                class="button"
                disabled
              >
                <b-icon
                  size="is-small"
                  icon="sync"/>
                <span>Làm mới</span>
              </b-button>
            <b-select v-model="perPage">
              <option value="5">5 dòng/trang</option>
              <option value="10">10 dòng/trang</option>
              <option value="15">15 dòng/trang</option>
              <option value="20">20 dòng/trang</option>
            </b-select>
          </b-field>
          <b-field>
              <b-table
                  :data="isLogEmpty ? [] : log_data"
                  :loading="loading"
                  paginated
                  backend-pagination
                  :total="total"
                  :per-page="perPage"
                  @page-change="onPageChange"
                  aria-next-label="Next page"
                  aria-previous-label="Previous page"
                  aria-page-label="Page"
                  aria-current-label="Current page"
                  hoverable
                  backend-sorting
                  :default-sort-direction="defaultSortOrder"
                  :default-sort="[sortField, sortOrder]"
                  @sort="onSort">
                  <template slot-scope="props">
                    <b-table-column field="LogID" label="ID" sortable>
                        {{ props.row.LogID }}
                    </b-table-column>

                    <b-table-column field="UserID" label="Người dùng" width="120" sortable>
                         {{ props.row.User }}
                    </b-table-column>

                    <b-table-column field="Action" label="Hành động" width="700" sortable>
                        {{ props.row.Action }}
                    </b-table-column>

                    <b-table-column field="Created_At" label="Thời gian" width="120" sortable>
                        <span class="tag is-primary">
                          {{ formatDate(props.row.Created_At) }}
                        </span>
                    </b-table-column>

                  </template>
                  <template slot="empty">
                        <section class="section">
                            <b-message type="is-danger" has-icon>
                              Hiện tại chưa có thông tin về nhật ký!
                            </b-message>
                        </section>
                  </template>
              </b-table>
          </b-field>
      </div>
</template>

<script>
  import axios from 'axios';
  import moment from 'moment/moment';
  import { authHeader } from "../../api/jwt_handling";

  export default {
      name: 'log_management',
      data() {
          return {
              isLogEmpty: false,
              log_data: [],
              total: 0,
              loading: false,
              sortField: 'Created_At',
              sortOrder: 'desc',
              defaultSortOrder: 'desc',
              page: 1,
              perPage: 20
          }
      },
      methods: {
          formatDate(date) {
                return moment(date).format("L, LTS");
          },
          /*
            * Load async log info record
           */
          async getLogRecordData() {
              this.loading = true;
              try {
                  const response = await axios({
                      url: '/log/log-records',
                      method: 'get',
                      params: {
                          page_index: this.page,
                          per_page: this.perPage,
                          sort_field: this.sortField,
                          sort_order: this.sortOrder
                      },
                      headers: {
                          'Authorization': authHeader(),
                      }
                  });
                  if (response.status === 200) {
                      this.log_data = [];
                      this.total = response.data.total_results;
                      // console.log(response.data.log_records);
                      response.data.log_records.forEach((item) => {
                          this.log_data.push(item);
                      });
                      // console.log(this.data);
                      this.loading = false
                  }
              } catch (error) {
                  this.log_data = [];
                  this.total = 0;
                  this.loading = false;
                  this.$buefy.notification.open({
                      duration: 2000,
                      message: 'Không thể lấy được dữ liệu nhật ký!',
                      position: 'is-bottom-right',
                      type: 'is-danger',
                      hasIcon: true
                  });
                  throw error;
              }
          },
            /*
            * Handle page-change event
            */
            onPageChange(page) {
                this.page = page;
                this.getLogRecordData()
            },
            /*
        * Handle sort event
        */
            onSort(field, order) {
                this.sortField = field;
                this.sortOrder = order;
                this.getLogRecordData()
            },
        },

        mounted() {
            this.getLogRecordData()
        }
    }
</script>
