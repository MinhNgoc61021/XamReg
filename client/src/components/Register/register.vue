<template>
  <div id="container">
    <div id="sign-in-form">
      <a-form layout="horizontal" :form="form" @submit="handleSubmit">
        <h3 id="title">Đăng Nhập</h3>
        <strong>Hãy đăng nhập bằng tài khoãn mà bạn đã được cấp</strong>
        <a-form-item :validate-status="userNameError() ? 'error' : ''" :help="userNameError() || ''">
          <a-input
            v-decorator="[
              'username',
              { rules: [{ required: true, message: 'Hãy nhập tên người dùng!' }] },
            ]"
            placeholder="Username">
            <a-icon slot="prefix" type="user" style="color:rgba(0,0,0,.25)" />
          </a-input>
        </a-form-item>
        <a-form-item :validate-status="passwordError() ? 'error' : ''" :help="passwordError() || ''">
          <a-input
            v-decorator="[
              'password',
              { rules: [{ required: true, message: 'Hãy nhập mật khẩu!' }] },
            ]"
            type="password"
            placeholder="Password"
          >
            <a-icon slot="prefix" type="lock" style="color:rgba(0,0,0,.25)" />
          </a-input>
        </a-form-item>
        <a-form-item>
          <a-button type="primary" html-type="submit" :disabled="hasErrors(form.getFieldsError())">
            Đăng nhập
          </a-button>
        </a-form-item>
      </a-form>
    </div>
  </div>
</template>

<script>
import { mapMutations , mapActions } from 'vuex';

function hasErrors(fieldsError) {
  return Object.keys(fieldsError).some(field => fieldsError[field]);
}
export default {
    name: 'Register_Form',
  data() {
    return {
      hasErrors,
      form: this.$form.createForm(this, { name: 'horizontal_login' }),
    };
  },
  mounted() {
    this.$nextTick(() => {
      // To disabled submit button at the beginning.
      this.form.validateFields();
    });
  },
  methods: {
      ...mapActions([
          "SignIn"
      ]),
      // Only show error after a field is touched.
      userNameError() {
        const { getFieldError, isFieldTouched } = this.form;
        return isFieldTouched('userName') && getFieldError('userName');
      },
      // Only show error after a field is touched.
      passwordError() {
        const { getFieldError, isFieldTouched } = this.form;
        return isFieldTouched('password') && getFieldError('password');
      },
      handleSubmit(e) {
        e.preventDefault();
        this.form.validateFields((err, formInput) => {
          if (!err) {
            this.SignIn(formInput);
          }
        });
      },
    },
};
</script>
<style src="../css/login_style.css">

</style>
