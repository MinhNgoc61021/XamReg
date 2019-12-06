<template>
  <div>
    <section>
        <button @click="isComponentModalActive = true">Thêm</button>
        <b-modal :active.sync="isComponentModalActive"
                 has-modal-card
                 trap-focus
                 aria-role="dialog"
                 aria-modal>
            <modal-add-form v-bind="data"></modal-add-form>
        </b-modal>
    </section>
    <b-table
      :data="demo_data"
      :bordered="true"
      :loading="true">

        <template slot-scope="props">
          <b-table-column field="id" label="TT" width="40" numeric>
            {{ props.row.id }}
          </b-table-column>
          <b-table-column field="subject_code" label="Mã môn học" width="100">
            {{ props.row.code }}
          </b-table-column>
          <b-table-column field="subject_name" label="Tên môn học" width="100">
            {{ props.row.name }}
          </b-table-column>
          <b-table-column field="modify" label="Chỉnh sửa" width="40">
            <b-button @click="onModify()" type="is-text" style="color:#3342ff;">Chỉnh sửa</b-button>
          </b-table-column>
          <b-table-column field="delete" label="Xóa" width="40">
            <b-button @click="onDelete()" type="is-text" style="color:#3342ff;">Xóa</b-button>
          </b-table-column>
        </template>
    </b-table>
  </div>
</template>

<script>
  import ModalAddForm from "../subjects_management/subjects_helper/addModal.vue"
  const demo_data = []
    export default {
        name: "subjects_management",
        data(){
            return {
                data:{
                    id: "",
                    subject_code: "",
                    subject_name: "",
                },
                isComponentModalActive: false
            }
        },
        mounted(){
            demo_data.push({ 'id': 1, 'subject_code': 'INT12345', 'subject_name': 'Quan li du an'})
            demo_data.push({ 'id': 2, 'subject_code': 'INT12345', 'subject_name': 'Phan tich va thiet ke huong doi tuong'})
            demo_data.push({ 'id': 3, 'subject_code': 'INT12345', 'subject_name': 'Lap trinh huong doi tuong'})
            demo_data.push({ 'id': 4, 'subject_code': 'INT12345', 'subject_name': 'Hoc may'})
            demo_data.push({ 'id': 5, 'subject_code': 'INT12345', 'subject_name': 'Tri tue nhan tao'})
        },
        components:{
            ModalAddForm
        },
        methods:{

        }
    }
</script>

<style scoped>

</style>
