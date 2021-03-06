<template>
  <div>
    <h1 class="title is-3">Quản lý phòng thi</h1>
    <h2 class="subtitle is-6">Cập nhật, quản lý thông tin của phòng thi</h2>
    <hr>
    <b-field grouped group-multiline>
      <b-button icon-pack="fas" icon-left="plus-square" outlined @click.prevent="onRoomAdd">
        Tạo phòng thi
      </b-button>

      <b-button
        class="button"
        @click="getRoomRecord"
        :class="{'is-loading': loading}"
      >
        <b-icon
          size="is-small"
          icon="sync"/>
        <span>Làm mới</span>
      </b-button>
      <b-select v-model="per_page">
        <option value="5">5 dòng/trang</option>
        <option value="10">10 dòng/trang</option>
        <option value="15">15 dòng/trang</option>
        <option value="20">20 dòng/trang</option>
      </b-select>

      <b-autocomplete
        :data="search.searchResults"
        placeholder="Tìm kiếm bằng tên phòng"
        icon="search"
        field="RoomName"
        :loading="search.searchLoading"
        @typing="onRoomSearch"
        @select="option => { exam_room_list = [option]; total = 1; }"
        expanded>
          <template slot-scope="props">
            <div class="media">
              <div class="media-content">
                <b>Tên phòng: </b>{{ props.option.RoomName }}
                <br>
                <b>Mã phòng: </b>{{ props.option.RoomID }}
                <br>
                <b>Số lượng máy tính: </b><p style="display: inline-block;">{{ props.option.Maxcapacity }}</p> <b-icon icon-pack="fas" size="is-small" icon="laptop"></b-icon>
              </div>
            </div>
          </template>
      </b-autocomplete>
    </b-field>
    <b-field>
      <b-table
        :data="isRoomEmpty ? [] : exam_room_list"
        :loading="loading"
        paginated
        backend-pagination
        :total="total"
        :per-page="per_page"
        @page-change="onPageChange"
        aria-next-label="Next page"
        aria-previous-label="Previous page"
        aria-page-label="Page"
        aria-current-label="Current page"
        backend-sorting
        hoverable
        :default-sort-direction="defaultSortOrder"
        :default-sort="[sortField, sortOrder]"
        @sort="onRoomSort">

          <template slot-scope="props">
            <b-table-column field="RoomID" label="Phòng thi số" width="100" sortable>
              {{ props.row.RoomID }}
            </b-table-column>
            <b-table-column field="RoomName" label="Tên phòng thi" width="100" sortable>
              {{ props.row.RoomName }}
            </b-table-column>
            <b-table-column field="Maxcapacity" label="Số lượng máy tính" width="100" sortable>
              <p style="width: 25px; display: inline-block; text-align: center;">{{ props.row.Maxcapacity }}</p> <b-icon icon-pack="fas" size="is-small" icon="laptop"></b-icon>
            </b-table-column>
             <b-table-column field="Action" width="90">
              <b-button type="is-warning" size="is-small" icon-pack="fas" icon-right="edit" outlined @click.prevent="onRoomEdit(props.row)"></b-button>
              <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onRoomDelete(props.row)"></b-button>
            </b-table-column>
          </template>
          <template slot="empty">
                <section class="section">
                    <b-message type="is-danger" has-icon>
                      Hiện tại chưa có thông tin về phòng thi, bạn hãy nhập vào phòng thi!
                    </b-message>
                </section>
          </template>
      </b-table>
    </b-field>
  </div>
</template>

<script>
  import axios from 'axios'
  import { authHeader } from "../../api/jwt_handling";
  import editRoomModal from "./helpers/exam_room_edit";
  import addRoomModal from "./helpers/exam_room_create";
  import debounce from 'lodash/debounce';

    export default {
        name: "exam_room_management",
        components:{
          editRoomModal,
          addRoomModal
        },
        data(){
          return{
              isRoomEmpty: false,
              exam_room_list: [],
              total: 0,
              loading: false,
              sortField: 'RoomID',
              sortOrder: 'desc',
              defaultSortOrder: 'asc',
              page: 1,
              per_page: 5,
              search: {
                    searchResults: [],
                    searchLoading: false,
              },
          }
        },
        methods: {
          async getRoomRecord() {
              this.loading = true;
              try {
                  const response = await axios({
                    url: '/room/room-records',
                    method: 'get',
                    params:{
                        page_index: this.page,
                        per_page: this.per_page,
                        sort_field: this.sortField,
                        sort_order: this.sortOrder
                    },
                    headers:{
                        'Authorization': authHeader(), //Authorization: Bearer <token> là form header của jwt
                    }
                  });
                  if (response.status === 200) {
                    this.exam_room_list = [];
                    this.total = response.data.total_results;
                    response.data.records.forEach((item) => {
                      this.exam_room_list.push(item);
                    });
                    console.log(this.exam_room_list);
                    this.loading = false
                  }
              } catch(error) {
                  this.exam_room_list = [];
                  this.total = 0;
                  this.loading = false;
                  this.$buefy.notification.open({
                    duration: 2000,
                    message: 'Không thể lấy được dữ liệu phòng thi!',
                    position: 'is-bottom-right',
                    type: 'is-danger',
                    hasIcon: true
                  });
                throw error;
              }
          },
          onPageChange(page){
            this.page = page;
            this.getRoomRecord()
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
          onRoomAdd(){
                this.$buefy.modal.open({
                    parent: this,
                    component: addRoomModal,
                    hasModalCard: true,
                    customClass: 'custom-class custom-class-2',
                    canCancel: false,
                    events: {
                        'loadRoomData': (http_status) => {
                            if (http_status === 200) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: `Đã thêm thành công!`,
                                    position: 'is-bottom-right',
                                    type: 'is-success',
                                    hasIcon: true
                                });
                                this.getRoomRecord();
                            }
                            else if(http_status === 202) {
                                 this.$buefy.notification.open({
                                    duration: 2000,
                                    message: 'Phòng thi này đã tồn tại từ trước!',
                                    position: 'is-bottom-right',
                                    type: 'is-warning',
                                    hasIcon: true
                                 });
                            }
                            else if(http_status === 400) {
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
                });
          },
          onRoomEdit(record) {
                // console.log(record.Dob);
                // console.log(new Date(moment(record.Dob).format('MM/DD/YYYY')));
                this.$buefy.modal.open({
                    parent: this,
                    component: editRoomModal,
                    props: {
                        currentRoomID: record.RoomID,
                        currentRoomName: record.RoomName,
                        currentMaxcapacity: record.Maxcapacity,
                    },
                    hasModalCard: true,
                    customClass: 'custom-class custom-class-2',
                    canCancel: false,
                    events: {
                        'loadEditRoomStatus': (http_status) => {
                            if (http_status === 200) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: `Đã cập nhật thành công!`,
                                    position: 'is-bottom-right',
                                    type: 'is-success',
                                    hasIcon: true
                                });
                                this.getRoomRecord();
                            }
                            else if (http_status === 202) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: `Tên phòng thi này đang bị trùng với tên phòng thi khác!`,
                                    position: 'is-bottom-right',
                                    type: 'is-warning',
                                    hasIcon: true
                                });
                                this.getRoomRecord();
                            }
                            else if(http_status === 400) {
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
                });
            },
          async onRoomDelete(record) {
                this.$buefy.dialog.confirm({
                    title: 'Xóa tài khoản',
                    message: `Bạn có chắc chắn là muốn <b>xóa</b> phòng thi ${record.RoomName} không? Đã làm thì tự chịu đấy.`,
                    confirmText: 'Xóa!',
                    cancelText: 'Bỏ qua',
                    type: 'is-danger',
                    hasIcon: true,
                    onConfirm: async () => {
                        try {
                            const removeData = await axios({
                                url: '/room/remove-room-record',
                                method: 'delete',
                                headers: {
                                    'Authorization': authHeader(),
                                },
                                data: {
                                    delRoomName: record.RoomName,
                                    delRoomID: record.RoomID,
                                },
                            });
                            if (removeData.status === 200) {
                                this.$buefy.notification.open({
                                    duration: 2000,
                                    message: `Đã xóa phòng thi ${record.RoomName} thành công.`,
                                    position: 'is-bottom-right',
                                    type: 'is-success',
                                    hasIcon: true
                                });
                            }
                            this.getRoomRecord();
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
                            if (this.exam_room_list.length === 1) {
                                // console.log(this.student.total);
                                // console.log(this.student.per_page);
                                if (parseInt(this.total / this.per_page) > 0) {
                                    this.page--;
                                    this.getRoomRecord();
                                }
                                else {
                                    this.page = 1;
                                    this.getRoomRecord();
                                }
                            }
                            else {
                                this.getRoomRecord();
                            }
                        }
                    },
                });
            },
          onRoomSort(field, order) {
                this.sortField = field;
                this.sortOrder = order;
                this.getRoomRecord();
            },
        },
      mounted(){
          this.getRoomRecord()
      }
    }
</script>
