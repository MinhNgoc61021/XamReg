<template>
  <div>
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li>Quản lý sinh viên </li>
      </ul>
    </nav>
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
    <section>
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

