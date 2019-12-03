<template>
  <div id="container">
    <section id="sign-in-form">
<!--        <b-checkbox v-model="hasError">Show errors</b-checkbox>-->
      <h3 class="title is-3">Đăng nhập</h3>
      <p class="subtitle is-6">Hãy đăng nhập bằng tài khoản mà bạn đã được cấp</p>
      <form @submit="handleSubmit">
        <b-field label="Username"
            :type="{ 'is-danger': hasError, 'is-danger': userExistence }"
            :message="[{ 'Username chưa được đánh': hasError },
                      {'Tài khoản không tồn tại hoặc mật khẩu sai': userExistence },
                      ]">
            <b-input placeholder="Hãy nhập username" v-model="username"></b-input>
        </b-field>

        <b-field label="Password"
            :type="{ 'is-danger': hasError, 'is-danger': userExistence }"
            :message="[{ 'Mật khẩu chưa được nhập': hasError },
                      {'Tài khoản không tồn tại hoặc mật khẩu sai': userExistence },
                      ]">
            <b-input placeholder="Hãy nhập mật khẩu" v-model="password" type="password"></b-input>
        </b-field>
        <div class="buttons">
            <b-button native-type="submit">Đăng nhập</b-button>
        </div>
      </form>
    </section>

  </div>
</template>

<script>
    import {mapActions, mapState} from "vuex";

    export default {
        data() {
            return {
                hasError: false,
                username: '',
                password: '',
                isNotExist: false,
            }
        },
        computed: {
            ...mapState([
                'userExistence'
            ]),
        },
        methods: {
            ...mapActions([
                'SignIn'
            ]),
            handleSubmit(e) {
              e.preventDefault();
              if (this.username.length < 5 || this.password.length < 5) {
                  this.hasError = true;
              }
              else {
                  this.hasError = false;
                  const { username, password } = this;
                  this.SignIn( { username, password } );
              }
            },
        }
    }
</script>
<style src="../css/login_style.css"></style>
