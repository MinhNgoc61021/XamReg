<template>
  <div>
    <h1 class="title is-3">Quản lý phòng thi</h1>
    <h2 class="subtitle is-6">Cập nhật, quản lý tài khoản và thông tin của phòng thi</h2><br>
    <b-button icon-pack="fas" icon-left="plus-square" outlined @click.prevent="onRoomAdd">
                Thêm phòng thi
    </b-button>
    <b-autocomplete
      :data="search.searchResults"
      placeholder="Tìm kiếm bằng tên phòng"
      icon="search"
      field="RoomName"
      :loading="search.searchLoading"
      @typing="onRoomSearch"
      @select="option => exam_room_list = [option]"
      expanded>
        <template slot-scope="props">
          <div class="media">
            <div class="media-left">
              <b-icon icon-pack="fas" icon="user-circle"></b-icon>
            </div>
            <div class="media-content">
              <b>RoomName: </b>{{ props.option.RoomName }}<br>
            </div>
          </div>
        </template>
    </b-autocomplete>
    <b-table
      :data="exam_room_list"
      :bordered="true"
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
      :default-sort-direction="defaultSortOrder"
      :default-sort="[sortField, sortOrder]"
      @sort="onRoomSort">

        <template slot-scope="props">
          <b-table-column field="RoomID" label="Phòng thi số" width="100">
            {{ props.row.RoomID }}
          </b-table-column>
          <b-table-column field="RoomName" label="Tên phòng thi" width="100">
            {{ props.row.RoomName }}
          </b-table-column>
          <b-table-column field="Maxcapacity" label="Số lượng chỗ" width="100">
            {{ props.row.Maxcapacity }}
          </b-table-column>
           <b-table-column field="Action" width="90">
            <b-button type="is-warning" size="is-small" icon-pack="fas" icon-right="edit" outlined @click.prevent="onRoomEdit(props.row)"></b-button>
            <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onRoomDelete(props.row)"></b-button>
          </b-table-column>
        </template>
    </b-table>
  </div>
</template>

<script>
  import axios from 'axios'
  import { authHeader } from "../../api/jwt_handling";
  import editRoomModal from "./helpers/editModal";
  import addRoomModal from "./helpers/addModal";
  import debounce from 'lodash/debounce';

    export default {
        name: "exam_room_management",
        components:{
          editRoomModal,
          addRoomModal
        },
        data(){
          return{
              exam_room_list: [],
              total: 0,
              loading: false,
              sortField: 'RoomID',
              sortOrder: 'desc',
              defaultSortOrder: 'asc',
              page: 1,
              per_page: 2,
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
                    message: 'Không thể load được dữ liệu phòng thi, xin hãy đăng nhập lại dưới quyền admin',
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
                        'loadRoomData': (http_status) => {
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
                    message: `Bạn có chắc chắn là muốn <b>xóa</b> phòng thi ${record.RoomName} không?'`,
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
                                    message: 'HTTP Status 401: Không được quyền sử dụng!',
                                    position: 'is-bottom-right',
                                    type: 'is-danger',
                                    hasIcon: true
                                })
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

<style scoped>

</style>
