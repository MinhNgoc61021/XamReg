<template>
  <form @submit.prevent="updatePassword()">
      <div class="modal-card">
        <header class="modal-card-head">
            <p class="modal-card-title">Cập nhật mật khẩu mới</p>
        </header>

        <section class="modal-card-body">
          <b-field label="Mật khẩu mới">
            <b-input
              icon="lock"
              type="password"
              v-model="newPassword"
              placeholder="Mật khẩu mới"
              validation-message="Yêu cầu mật khẩu mới phải có ít nhất 5 ký tự"
              password-reveal
              required>
            </b-input>
          </b-field>
        </section>

        <section class="modal-card-body">
          <b-field label="Xác nhận mật khẩu">
            <b-input
              type="password"
              icon="lock"
              v-model="confirmPassword"
              validation-message="Nhập đúng mật khẩu xác nhận"
              placeholder="Xác nhận mật khẩu"
              password-reveal
              required>
            </b-input>
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
  import axios from 'axios';
  import { mapActions } from 'vuex';
  import { authHeader } from "../api/jwt_handling";

  export default {
      name: "update_password",
      props: ['currentUserID'],
      data() {
          return {
              UserID: this.currentUserID,
              newPassword: '',
              confirmPassword: '',
          }
      },
      methods: {
          ...mapActions([
              'SignOut',
          ]),
          async updatePassword() {
              try {
                  // console.log(moment(this.newDob).format('MM/DD/YYYY'));
                  const update = await axios({
                      method: 'put',
                      url: 'https://xamreg-uet-vnu-edu.herokuapp.com/auth/update-password',
                      headers: {
                          'Authorization': authHeader(),
                      },
                      data: {
                          UserID: this.UserID,
                          newPassword: this.newPassword,
                          confirmPassword: this.confirmPassword,
                      },
                  });
                  if (update.status === 200) {
                      this.$parent.close();
                      this.$buefy.notification.open({
                          duration: 2000,
                          message: `Đã cập nhật mật khẩu thành công.`,
                          position: 'is-bottom-right',
                          type: 'is-success',
                          hasIcon: true,
                      });
                      this.SignOut();
                  }
                  else if (update.status === 202) {
                      this.$buefy.notification.open({
                          duration: 2000,
                          message: `Mật khẩu không hợp lệ, bạn hãy nhập ít nhất 5 ký tự và bạn phải nhập đúng mât khẩu xác nhận !`,
                          position: 'is-bottom-right',
                          type: 'is-warning',
                          hasIcon: true,
                      });
                  }
              } catch (e) {
                  if (e['message'].includes('400')) {
                      this.$buefy.notification.open({
                          duration: 2000,
                          message: 'Kiểm tra lại, dữ liệu bạn nhập đang không đúng!',
                          position: 'is-bottom-right',
                          type: 'is-danger',
                          hasIcon: true,
                      });
                  }
                  else if (e['message'].includes('401')) {
                      this.$buefy.notification.open({
                          duration: 2000,
                          message: 'Không được quyền sử dụng!',
                          position: 'is-bottom-right',
                          type: 'is-danger',
                          hasIcon: true,
                      });
                  }
              }
          },
      },
    }
</script>
<style scoped>

</style>
