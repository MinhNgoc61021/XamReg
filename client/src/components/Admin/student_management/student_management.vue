<template>
  <div>
    <h1 class="title is-3">Quản lý sinh viên</h1>
    <h2 class="subtitle is-6">Cập nhật, quản lý tài khoản và thông tin của sinh viên</h2>
    <section id="tab-action">
        <b-tabs type="is-boxed">
            <b-tab-item label="Nhập (Import)" icon-pack="fas" icon="file-import">
              <component v-bind:is="import_insert"/>
            </b-tab-item>
            <b-tab-item label="Xem & Chỉnh sửa danh sách sinh viên" icon-pack="fas" icon="user-edit">
              <component v-bind:is="record_management"/>
            </b-tab-item>
        </b-tabs>
    </section>
  </div>
</template>
<script>
  import record_management from "./student_record_management/record_management";
  import import_insert from './import/import_input';

  export default {
      name: 'student_management',
      components: {
          import_insert, record_management
      },
      data() {
          return {
              record_management,
              import_insert,
          }
      },
  }
</script>

