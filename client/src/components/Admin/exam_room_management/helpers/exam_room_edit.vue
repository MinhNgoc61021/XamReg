<template>
  <form @submit.prevent="updateRoom()">
      <div class="modal-card" style="width: 450px;">
        <header class="modal-card-head">
            <p class="modal-card-title">Form chỉnh sửa</p>
        </header>
        <section class="modal-card-body">
          <b-field label="Tên phòng thi">
            <b-input
              v-model="newRoomName"
              :value="newRoomName"
              maxlength="30"
              pattern="^[0-9a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀẾỂưăạảấầẩẫậắằẳẵặẹẻẽềếểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\-\s() ]+$"
              validation-message="Nhập đúng tên phòng thi"
              placeholder="Nhập tên phòng thi"
              required>
            </b-input>
          </b-field>
          <b-field label="Số lượng chỗ thi">
            <b-input
              type="number"
              v-model="newMaxcapacity"
              :value="newMaxcapacity"
              min="1"
              placeholder="Nhập số lượng chỗ thi"
              required>
            </b-input>
          </b-field>
        </section>

        <footer class="modal-card-foot">
          <button class="button" type="button" @click="$parent.close()">Bỏ qua</button>
          <button class="button is-primary" type="submit" @submit="closeModal()">Cập nhật</button>
        </footer>
      </div>
  </form>
</template>

<script>
    import axios from "axios";
    import {authHeader} from "../../../api/jwt_handling";
    export default {
        name: "editRoomModal",
        props: ['currentRoomID','currentRoomName', 'currentMaxcapacity'],
        data() {
          return {
              newRoomID: this.currentRoomID,
              newRoomName: this.currentRoomName,
              newMaxcapacity: this.currentMaxcapacity
          }
      },
      methods: {
          async updateRoom() {
              try {
                const update = await axios({
                      method: 'put',
                      url: '/room/update-room-record',
                      headers: {
                          'Authorization': authHeader(),
                      },
                      data: {
                          currentRoomID: this.currentRoomID,
                          RoomName: this.newRoomName,
                          Maxcapacity: this.newMaxcapacity,
                      },
                  });
                  if (update.status === 200) {
                      this.$emit('loadEditRoomStatus', 200);
                      this.$parent.close();
                  }
                  else if (update.status === 202) {
                      this.$emit('loadEditRoomStatus', 202);
                  }
              } catch (e) {
                  if (e['message'].includes('400')) {
                      this.$emit('loadEditRoomStatus', 400);
                  }
                  else if (e['message'].includes('401')) {
                      this.$emit('loadEditRoomStatus', 401);
                  }
              } finally {
              }
          },
      },
    }
</script>

<style scoped>
</style>
