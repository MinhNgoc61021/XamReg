<template>
  <form @submit.prevent="createRoom()">
      <div class="modal-card" style="width: 450px;">
        <header class="modal-card-head">
            <p class="modal-card-title">Form tạo phòng thi</p>
        </header>
        <section class="modal-card-body">
          <b-field label="Mã số phòng thi">
            <b-input
              type="number"
              v-model="newRoomID"
              :value="newRoomID"
              placeholder="Nhập mã số phòng thi"
              required>
            </b-input>
          </b-field>
          <b-field label="Tên phòng thi">
            <b-input
              v-model="newRoomName"
              :value="newRoomName"
              maxlength="19"
              placeholder="Nhập tên phòng thi"
              required>
            </b-input>
          </b-field>
          <b-field label="Số lượng chỗ thi">
            <b-input
              type="number"
              v-model="newMaxcapacity"
              :value="newMaxcapacity"
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
        name: "addRoomModal",
        data() {
          return {
              newRoomID: "",
              newRoomName: "",
              newMaxcapacity: ""
          }
      },
      methods: {
          async createRoom() {
              try {
                const update = await axios({
                      method: 'post',
                      url: '/room/create-room-records',
                      headers: {
                          'Authorization': authHeader(),
                      },
                      data: {
                          newRoomID: this.newRoomID,
                          newRoomName: this.newRoomName,
                          newMaxcapacity: this.newMaxcapacity,
                      },
                  });
                  if (update.status === 200) {
                      this.$emit('loadRoomData', 200);
                      this.$parent.close();
                  }
              } catch (e) {
                  if (e['message'].includes('400')) {
                      this.$emit('loadRoomData', 400);
                  }
                  else if (e['message'].includes('401')) {
                      this.$emit('loadRoomData', 401);
                  }
              } finally {
              }
          },
      },
    }
</script>
