<template>
  <form @submit.prevent="updateSemester()">
    <div class="modal-card" style="width: 450px;">
        <header class="modal-card-head">
            <p class="modal-card-title">Form chỉnh sửa</p>
        </header>
        <section class="modal-card-body">
          <b-field label="Tiêu đề">
            <b-input
              type="text"
              v-model="newSemTitle"
              :value="newSemTitle"
              pattern="^[0-9a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀẾỂưăạảấầẩẫậắằẳẵặẹẻẽềếểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\-\s() ]+$"
              validation-message="Nhập đúng tiêu đề kỳ thi"
              placeholder="Sửa tiêu đề kỳ thi"
              required>
            </b-input>
          </b-field>
          <b-field label="Tình trạng">
            <b-switch v-model="newStatus"
                      :value="newStatus">
              <b-tag v-if="newStatus === false">Chưa mở đăng ký</b-tag>
              <b-tag v-else type="is-primary">Mở đăng ký</b-tag>
            </b-switch>
          </b-field>

        </section>
      <footer class="modal-card-foot">
          <button class="button" type="button" @click="$parent.close()">Bỏ qua</button>
          <button class="button is-primary" type="submit">Cập nhật</button>
      </footer>
    </div>
  </form>
</template>

<script>
    import axios from "axios";
    import debounce from 'lodash.debounce';
    import moment from 'moment/moment';
    import {authHeader} from "../../../../api/jwt_handling";

    export default {
        name: "semester_edit",
        props: ['currentSemID', 'currentSemTitle', 'currentStatus'],
        data() {
          return {
              SemID: this.currentSemID,
              newSemTitle: this.currentSemTitle,
              newStatus: this.currentStatus,
          }
        },
        methods: {
            async updateSemester() {
                try {
                  const update = await axios({
                    method: 'put',
                    url: '/schedule/edit-semester',
                    headers: {
                      'Authorization': authHeader(),
                    },
                    data: {
                        semID: this.SemID,
                        newSemTitle: this.newSemTitle,
                        newStatus: this.newStatus,
                    },
                  });
                  if (update.status === 200) {
                    this.$emit('loadSemesters', 200);
                    this.$parent.close();
                  }
                  if (update.status === 202) {
                    this.$emit('loadSemesters', 202);
                  }
                } catch (e) {
                  if (e['message'].includes('400')) {
                    this.$emit('loadSemesters', 400);
                  } else if (e['message'].includes('401')) {
                    this.$emit('loadSemesters', 401);
                  }
                }
            },
        }
    }
</script>
