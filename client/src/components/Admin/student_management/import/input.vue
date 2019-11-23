<template>
  <section id="form-container">
  <a-form :form="form">
    <a-form-item
      :label-col="formItemLayout.labelCol"
      :wrapper-col="formItemLayout.wrapperCol"
      label="MSSV">
      <a-input
        v-decorator="[
          'ID',
          { rules: [{ required: true, message: 'Hãy nhập MSSV' }] },
        ]"
        placeholder="Hãy nhập MSSV"
      />
    </a-form-item>
    <a-form-item
      :label-col="formItemLayout.labelCol"
      :wrapper-col="formItemLayout.wrapperCol"
      label="Họ và tên"
    >
      <a-input
        v-decorator="[
          'Fullname',
          { rules: [{ required: true, message: 'Hãy nhập đầy đủ họ và tên' }] },
        ]"
        placeholder="Hãy nhập đầy đủ họ và tên"
      />
    </a-form-item>
    <a-form-item
      :label-col="formItemLayout.labelCol"
      :wrapper-col="formItemLayout.wrapperCol"
      label="Date of birth">
      <a-date-picker :format="dateFormat"
          v-decorator="[
            'dob',
            { rules: [{ required: true, message: 'Hãy nhập đầy đủ ngày tháng năm sinh' }] },
          ]"
      />
    </a-form-item>
    <a-form-item
      :label-col="formItemLayout.labelCol"
      :wrapper-col="formItemLayout.wrapperCol"
      label="Giới tính" >
      <a-select
        v-decorator="[
          'gender',
          { rules: [{ required: true, message: 'Hãy chọn giới tính' }] },
        ]"
        placeholder="Chọn giới tính"
        @change="handleSelectChange"
      >
        <a-select-option value="male">
          Nam
        </a-select-option>
        <a-select-option value="female">
          Nữ
        </a-select-option>
      </a-select>
    </a-form-item>
    <a-form-item
      :label-col="formItemLayout.labelCol"
      :wrapper-col="formItemLayout.wrapperCol"
      label="Mã khóa học">
      <a-input
        v-decorator="[
          'courseID',
          { rules: [{ required: true, message: 'Hãy nhập mã khóa học' }] },
        ]"
        placeholder="Hãy nhập mã khóa học"
      />
    </a-form-item>
    <a-form-item :label-col="formTailLayout.labelCol" :wrapper-col="formTailLayout.wrapperCol">
      <a-button type="primary" @click="check">
        Tạo tài khoản
      </a-button>
    </a-form-item>
  </a-form>
  </section>
</template>

<script>
const formItemLayout = {
  labelCol: { span: 4 },
  wrapperCol: { span: 8 },
};
const formTailLayout = {
  labelCol: { span: 4 },
  wrapperCol: { span: 8, offset: 4 },
};
export default {
  data() {
    return {
      dateFormat: 'MM/DD/YYYY',
      checkNick: false,
      formItemLayout,
      formTailLayout,
      form: this.$form.createForm(this, { name: 'dynamic_rule' }),
    };
  },
  methods: {
    check() {
      this.form.validateFields(err => {
        if (!err) {
          console.info('success');
        }
      });
    },
    handleChange(e) {
      this.checkNick = e.target.checked;
      this.$nextTick(() => {
        this.form.validateFields(['nickname'], { force: true });
      });
    },
  },
};
</script>
<style scoped>
  #form-container {
    position: absolute;
    width: 60%;
    left: 13%;
    right: 12%;
  }
</style>
