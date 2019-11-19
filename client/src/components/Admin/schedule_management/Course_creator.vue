<template>
    <section id="form-container">
    <a-form :form="form" @submit="handleSubmit">
    <a-form-item v-bind="formItemLayout" label="Mã kì thi: ">
      <a-input style="width:200px"
        v-decorator="[
          'Mã kì thi: ',
          {
            rules: [
              {
                required: true,
                message: 'Bạn chưa điền mã kì thi.',
              },
            ],
          },
        ]"
      />
    </a-form-item>
    <a-form-item v-bind="formItemLayout" label="Tên kì thi">
      <a-input style="width:200px"
        v-decorator="[
          'Tên kì thi',
          {
            rules: [
              {
                required: true,
                message: 'Bạn chưa điền tên kì thi',
              },
            ],
          },
        ]"
      />
    </a-form-item>
    <a-form-item v-bind="tailFormItemLayout">
      <a-button type="primary" html-type="submit">
        Tạo kì thi
      </a-button>
    </a-form-item>
  </a-form>
  </section>
</template>

<script>
import Course_detail from "./Course_detail";
export default {
  name: "Course_creator",
  components: {
    Course_detail,
  }
}
</script>

<style scoped>

</style>
