<template>
  <a-list size="small" bordered :dataSource="rooms">
      <div slot="header">Danh sách ca thi</div>
      <a-list-item slot="renderItem" slot-scope="room, index">
        <div>
          <a-select defaultValue="Chọn phòng thi" style="width: 200px" @change="handleChange">
            <a-select-option v-for="room in rooms" value="room">{{room.name}}</a-select-option>
          </a-select>
          <a-date-picker style="margin-left: 5px; width: 200px" @change="onChange" />
          <span>Thông tin ca thi:</span>
        </div>
      </a-list-item>
    </a-list>
</template>

<script>
export default {
  name: "Shift_detail",
  data() {
    return {
      rooms: [
          {
            name: "Phòng 408-G2",
          },
          {
            name: "Phòng 320-GĐ3",
          },
          {
            name: "Phòng 237-Overlook Hotel",
          }
      ]
    }
  },
}
</script>

<style scoped>

</style>
