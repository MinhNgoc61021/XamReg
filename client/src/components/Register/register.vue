<!--<template>-->
<!--  <div id="container">-->
<!--    <div id="sign-in-form">-->
<!--      <a-form layout="horizontal" :form="form" @submit="handleSubmit">-->
<!--        <h3 id="title">Đăng Nhập</h3>-->
<!--        <strong>Hãy đăng nhập bằng tài khoản mà bạn đã được cấp</strong>-->
<!--        <a-form-item :validate-status="userNameError() ? 'error' : ''" :help="userNameError() || ''">-->
<!--          <a-input-->
<!--            v-decorator="[-->
<!--              'username',-->
<!--              { rules: [{ required: true, message: 'Hãy nhập username của bạn!' }] },-->
<!--            ]"-->
<!--            placeholder="Hãy nhập username của bạn">-->
<!--            <a-icon slot="prefix" type="user" style="color:rgba(0,0,0,.25)" />-->
<!--          </a-input>-->
<!--        </a-form-item>-->
<!--        <a-form-item :validate-status="passwordError() ? 'error' : ''" :help="passwordError() || ''">-->
<!--          <a-input-->
<!--            v-decorator="[-->
<!--              'password',-->
<!--              { rules: [{ required: true, message: 'Hãy nhập mật khẩu của bạn!' }] },-->
<!--            ]"-->
<!--            type="password"-->
<!--            placeholder="Hãy nhập mật khẩu của bạn"-->
<!--          >-->
<!--            <a-icon slot="prefix" type="lock" style="color:rgba(0,0,0,.25)" />-->
<!--          </a-input>-->
<!--        </a-form-item>-->
<!--        <a-form-item>-->
<!--          <a-button type="primary" html-type="submit" :disabled="hasErrors(form.getFieldsError())">-->
<!--            Đăng nhập-->
<!--          </a-button>-->
<!--        </a-form-item>-->
<!--      </a-form>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import { mapMutations , mapActions } from 'vuex';-->

<!--function hasErrors(fieldsError) {-->
<!--  return Object.keys(fieldsError).some(field => fieldsError[field]);-->
<!--}-->
<!--export default {-->
<!--    name: 'Register_Form',-->
<!--  data() {-->
<!--    return {-->
<!--      hasErrors,-->
<!--      form: this.$form.createForm(this, { name: 'horizontal_login' }),-->
<!--    };-->
<!--  },-->
<!--  mounted() {-->
<!--    this.$nextTick(() => {-->
<!--      // To disabled submit button at the beginning.-->
<!--      this.form.validateFields();-->
<!--    });-->
<!--  },-->
<!--  methods: {-->
<!--      ...mapActions([-->
<!--          "SignIn"-->
<!--      ]),-->
<!--      // Only show error after a field is touched.-->
<!--      userNameError() {-->
<!--        const { getFieldError, isFieldTouched } = this.form;-->
<!--        return isFieldTouched('username') && getFieldError('username');-->
<!--      },-->
<!--      // Only show error after a field is touched.-->
<!--      passwordError() {-->
<!--        const { getFieldError, isFieldTouched } = this.form;-->
<!--        return isFieldTouched('password') && getFieldError('password');-->
<!--      },-->
<!--      handleSubmit(e) {-->
<!--        e.preventDefault();-->
<!--        this.form.validateFields((err, formInput) => {-->
<!--          if (!err) {-->
<!--            this.SignIn(formInput);-->
<!--          }-->
<!--        });-->
<!--      },-->
<!--    },-->
<!--};-->
<!--</script>-->
<!--<style src="../css/login_style.css">-->

<!--</style>-->
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
            :message="[{ 'Mật khẩu chưa được đánh': hasError },
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
