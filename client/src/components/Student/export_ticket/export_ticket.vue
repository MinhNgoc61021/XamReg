<template>
  <div>
    <h1 class="title is-3">Quản lý phòng thi</h1>
    <h2 class="subtitle is-6">Cập nhật, quản lý thông tin của phòng thi</h2>
    <b-field grouped group-multiline>

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
      <download-excel
        class   = "btn btn-default"
        :fetch   = "exportExcel"
        :before-generate = "startDownload"
        :before-finish = "finishDownload"
      >
        <b-button class="button" icon-left="file-download" @click="exportExcel">In</b-button>
      </download-excel>
<!--      <b-select v-model="per_page">-->
<!--        <option value="5">5 dòng/trang</option>-->
<!--        <option value="10">10 dòng/trang</option>-->
<!--        <option value="15">15 dòng/trang</option>-->
<!--        <option value="20">20 dòng/trang</option>-->
<!--      </b-select>-->

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
              <div class="media-content">
                <b>Mã phòng: </b>{{ props.option.RoomID }}
                <br>
                <b>Tên phòng: </b>{{ props.option.RoomName }}
              </div>
            </div>
          </template>
      </b-autocomplete>
    </b-field>
    <b-field v-if="exam_room_list.length > 0">
      <b-table
        :data="exam_room_list"
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
            <b-table-column field="Maxcapacity" label="Số lượng chỗ" width="100" sortable>
              <span class="is-primary">
                {{ props.row.Maxcapacity }}
              </span>
            </b-table-column>
          </template>
      </b-table>
    </b-field>
    <b-field v-else>
    </b-field>
  </div>
</template>

<script>
    import axios from 'axios';
    import moment from 'moment';
    import {authHeader} from "../../../api/jwt_handling";
    import debounce from 'lodash/debounce';

    export default {
        name: 'export_ticket',
        data() {
            return {

            }
        },
        methods: {

        }
    }
</script>
