<template>
  <div>
    <b-table
      :data="exam_room_list"
      :bordered="true"
      :loading="loading"
      backend-pagination
      :total="total"
      :per-page="per_page"
      @page-change="onPageChange()"
      aria-next-label="Next page"
      aria-previous-label="Previous page"
      aria-page-label="Page"
      aria-current-label="Current page"
      backend-sorting
      :default-sort-direction="defaultSortOrder"
      :default-sort="[sortField, sortOrder]">

        <template slot-scope="props">
          <b-table-column field="room_id" label="Phòng thi số" width="100">
            {{ props.row.RoomID }}
          </b-table-column>
          <b-table-column field="room_name" label="Tên phòng thi" width="100">
            {{ props.row.RoomName }}
          </b-table-column>
          <b-table-column field="room_name" label="Số lượng chỗ" width="100">
            {{ props.row.Computer_Number }}
          </b-table-column>
        </template>
        <template slot="bottom-left">
          <b-button type="is-white"
                    size="is-small"
                    icon-pack="fas" icon-right="plush-square" outlined
                    @click.prevent="onaddRoom()"></b-button>
          <b-button type="is-white"
                    size="is-small"
                    icon-pack="fas" icon-right="minus-square" outlined
                    @click.prevent="ondeleteRoom()"></b-button>
        </template>
    </b-table>
  </div>
</template>

<script>
  import axios from 'axios'
  import { authHeader } from "../../api/jwt_handling";
  import moment from 'moment/moment';
    export default {
        name: "exam_room_management",
        data(){
          return{
            exam_room_list: [],
            total: 0,
            loading: false,
            sortField: 'RoomcacheID',
            sortOrder: 'desc',
            defaultSortOrder: 'desc',
            page: 1,
            per_page: 5,
          }
        },
        methods: {
          async getRoomRecord() {
              this.loading = true;
              try {
                  const response = await axios({
                    url: '/room/room-cache-records',
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
                    message: 'Houston, we are in deep shit! (unable to load data)',
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

        },
      mounted(){
          this.getRoomRecord()
      }
    }
</script>

<style scoped>

</style>
