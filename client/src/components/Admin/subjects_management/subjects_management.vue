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
      :data="subjects_record"
      :bordered="true"
      :loading="loading"
      backend-pagination
      :total="total"
      :per-page="per_page"
      @page-change="onPageChange"
      aria-next-label="Next page"
      aria-previous-label="Previous page"
      aria-page-label="Page"
      aria-current-label="Current page"
      backend-sorting
      :default-sort-direction="defaultSortOrder"
      :default-sort="[sortField, sortOrder]">

        <template slot-scope="props">
<!--          <b-table-column field="id" label="TT" width="40" numeric>-->
<!--            {{ props.row.id }}-->
<!--          </b-table-column>-->
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
  import axios from 'axios'
  import { authHeader } from "/client/src/components/api/jwt_handling.js";
  import ModalAddForm from "../subjects_management/subjects_helper/addModal.vue"

    export default {
        name: "subjects_management",
        data(){
            return {
              subjects_record: [],
              total: 0,
              loading: false,
              sortField: 'subject_code',
              sortOrder: 'desc',
              defaultSortOrder: 'desc',
              page: 1,
              per_page: 5,
              isComponentModalActive: false
            }
        },
        components:{
            ModalAddForm
        },
        mounted(){
          this.getSubjectList()
        },
        methods:{
          getSubjectList(){
            axios.get('/record/subjects-record', {
              params: {
                page_index: this.page,
                per_page: this.per_page,
                sort_field: this.sortField,
                sort_order: this.sortOrder
              },
              headers: {
                'Authorization': authHeader(),
              }
            }).then((respone => {
                  this.subjects_record = [];
                  this.total = response.data.total_results;
                  response.data.records.forEach((item) => {
                    this.student_record.push(item);
                  });
                  // console.log(this.data);
                  this.loading = false
            }))
          },
          onPageChange(page) {
            this.page = page;
            this.getSubjectList();
          },
          onSort(field, order) {
            this.sortField = field;
            this.sortOrder = order;
            this.getRecordData();
          },
        }
    }
</script>

<style scoped>

</style>
