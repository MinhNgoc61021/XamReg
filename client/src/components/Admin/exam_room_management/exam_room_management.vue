<template>
  <div>
    <h1 class="title is-3">Quản lý phòng thi</h1>
    <h2 class="subtitle is-6">Cập nhật, quản lý tài khoản và thông tin của sinh viên</h2>
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
      :default-sort="[sortField, sortOrder]">

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

      <button></button>
    </b-table>
  </div>
</template>

<script>
  import axios from 'axios'
  import { authHeader } from "../../api/jwt_handling";
  import editRoomModal from "./helpers/editModal";
    export default {
        name: "exam_room_management",
        components:{
          editRoomModal
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
        },

      mounted(){
          this.getRoomRecord()
      }
    }
</script>

<style scoped>

</style>
