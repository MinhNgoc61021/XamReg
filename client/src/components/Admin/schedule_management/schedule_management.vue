<template>
    <div class="container">
        <h1 class="title is-3">Quản lý lịch thi</h1>
        <h2 class="subtitle is-6">Tạo, quản lý lịch, ca thi, danh sách sinh viên dự thi</h2>
        <section id="tab-action">
            <b-tabs type="is-boxed">
                <b-tab-item label="Tạo và Quản lý" icon-pack="fas" icon="plus">
                  <component v-bind:is="create_management"/>
                </b-tab-item>
                <b-tab-item label="Xem danh sách & Xuất (Export) PDF" icon-pack="fas" icon="file-export">
                  <component v-bind:is="export_pdf"/>
                </b-tab-item>
            </b-tabs>
        </section>
    </div>
</template>

<script>
    import export_pdf from "./export_pdf/export_pdf";
    import create_management from "./create_management/create_management";
    export default {
        name: "schedule_management",
        components: {
            create_management, export_pdf
        },
        data() {
          return {
              create_management,
              export_pdf,
          }
      },
    }
</script>
