<template>
  <div id="container">
    <section id="sign-in-form">
<!--        <b-checkbox v-model="hasError">Show errors</b-checkbox>-->
      <h3 class="title is-3">Đăng nhập</h3>
      <p class="subtitle is-6">Hãy đăng nhập bằng tài khoản mà bạn đã được cấp</p>
      <form @submit.prevent="handleSubmit">
        <b-field label="Tài khoản"
            :type="{ 'is-warning': hasError, 'is-danger': isNotExist   }"
            :message="[{ 'Tài khoản và mật khẩu có ít nhất 5 ký tự': hasError },
                      {'Tài khoản không tồn tại hoặc mật khẩu sai': isNotExist },
                      ]">
            <b-input placeholder="Hãy nhập tài khoản" icon="user" v-model="username" ></b-input>
        </b-field>

        <b-field label="Mật khẩu"
            :type="{ 'is-warning': hasError, 'is-danger': isNotExist }"
            :message="[{ 'Tài khoản và mật khẩu có ít nhất 5 ký tự': hasError },
                      {'Tài khoản không tồn tại hoặc mật khẩu sai': isNotExist },
                      ]">
            <b-input placeholder="Hãy nhập mật khẩu" icon="lock" v-model="password" type="password"></b-input>
        </b-field>
        <div class="buttons">
            <b-button native-type="submit" id="sign-in-btn">Đăng nhập</b-button>
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
            }
        },
        computed: {
            ...mapState([
                'isNotExist'
            ]),
        },
        methods: {
            ...mapActions([
                'SignIn'
            ]),
            handleSubmit() {
              try {
                  if (this.username.length < 5 || this.password.length < 5) {
                      this.hasError = true;
                  }
                  else {
                      this.hasError = false;
                      const { username, password } = this;
                      this.SignIn( { username, password } );
                  }
              } catch (e) {
                  this.$buefy.notification.open({
                      duration: 2000,
                      message: 'Không thể kết nối đến hệ thống!',
                      position: 'is-bottom-right',
                      type: 'is-danger',
                      hasIcon: true
                    });
              }
            },
        }
    }
</script>
<style scoped>
  #container {
    height: 100vh;
    position: relative;
  }
  #sign-in-form {
    border-radius: 4px;
    border: 1px rgba(73, 80, 87, 0.41) solid;
    position: absolute;
    top: 50%;
    right: 50%;
    min-width: 450px;
    min-height: 300px;
    padding: 50px;
    transform: translate(50%,-50%);
    -moz-transform: translate(50%,-50%);
    -webkit-transform: translate(50%,-50%);
    -o-transform: translate(50%,-50%);
    /*-ms-transform: translate(50%,-50%);*/
    /*-webkit-transition: width 2s, height 2s; !* Safari prior 6.1 *!*/
    /*transition: width 2s, height 2s;*/
    /*transition-timing-function: linear;*/
  }

  label {
    display: inline;
    max-width: 150px;
    float: left;
  }

  #container input {
    margin-top: 10px;
  }

  #container button {
    margin-top: 10px;
  }

  #container a {
    outline: none;
    text-decoration: none;
  }

  @media only screen and (max-width: 550px) {
    #sign-in-form {
      margin: 0;
      min-width: 300px;
      font-size: 12px;
    }
    #sign-in-btn {
      width: 100%;
    }

  }
  @media only screen and (max-height: 700px) {
    #container {
      transform: translate(0%, 0%);
          /*-moz-transform: translate(50%,-50%);*/
          /*-webkit-transform: translate(50%,-50%);*/
          /*-o-transform: translate(50%,-50%);*/
    }
  }

</style>
