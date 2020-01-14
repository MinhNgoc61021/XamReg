<template>
    <div class="container">
        <h1 class="title is-3">Quản lý lịch thi</h1>
        <h2 class="subtitle is-6">Tạo, quản lý lịch, ca thi và in danh sách sinh viên dự thi</h2>
        <hr>
        <section id="tab-action">
            <b-tabs type="is-boxed">
                <b-tab-item label="Tạo và Quản lý danh sách kỳ thi" icon-pack="fas" icon="plus-square">
                  <component v-bind:is="create_schedule_management"/>
                </b-tab-item>
                <b-tab-item label="Xem & In danh sách sinh viên dự thi" icon-pack="fas" icon="file-export">
                  <component v-bind:is="export_file"/>
                </b-tab-item>
            </b-tabs>
        </section>
    </div>
</template>

<script>
    import export_file from "./export_file/export";
    import create_schedule_management from "./create_management/create_schedule_management";
    export default {
        name: "schedule_management",
        components: {
            create_schedule_management, export_file
        },
        data() {
          return {
              create_schedule_management,
              export_file,
          }
      },
    }
</script>
