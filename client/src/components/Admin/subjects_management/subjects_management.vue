<template>
  <div>
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li>Quản lý môn thi </li>
      </ul>
    </nav>

    <section>
      <b-field grouped group-multiline>
            <b-button
              class="button"
              @click="getSubjectsInfo"
            >
              <b-icon
                size="is-small"
                icon="sync"/>
              <span>Làm mới</span>
            </b-button>

            <b-select >
              <option value="5">5 dòng/trang</option>
              <option value="10">10 dòng/trang</option>
              <option value="15">15 dòng/trang</option>
              <option value="20">20 dòng/trang</option>
            </b-select>

            <b-autocomplete
                placeholder="Tìm kiếm bằng mã môn học"
                icon="search"
                field="ID"
                expanded>
            </b-autocomplete>
        </b-field>
        <b-table
          :data="subject_info.subject_record"
          :loading="subject_info.loading"
          paginated
          backend-pagination
          detailed
          :total="subject_info.total"
          :per-page="subject_info.per_page"
          aria-next-label="Next page"
          aria-previous-label="Previous page"
          aria-page-label="Page"
          aria-current-label="Current page"
          backend-sorting
          hoverable
          detail-key="ID"
          :default-sort-direction="subject_info.defaultSortOrder"
          :default-sort="[subject_info.sortField, subject_info.sortOrder]"
          @sort="onStatusSort"
        >
          <template slot-scope="props">
            <b-table-column field="SubjectID" label="Mã môn học" sortable>
              {{props.row.SubjectID}}
            </b-table-column>
            <b-table-column field="SubjectName" label="Tên môn học" sortable>
              {{props.row.SubjectTitle}}
            </b-table-column>
          </template>
        </b-table>

    </section>
  </div>
</template>

<script>
    import axios from 'axios'
    import { authHeader} from "../../api/jwt_handling";

    export default {
        name: "subjects_management",
        data() {
          return {
            subject_info: {
              subject_record: [],
              total: 0,
              loading: false,
              sortField: 'SubjectID',
              sortOrder: 'desc',
              defaultSortOrder: 'desc',
              page: 1,
              per_page: 5,
            },
            search: {
              searchResults: [],
              searchLoading: false,
            }
          }
        },
        methods: {
          async getSubjectsInfo() {
            this.subject_info.loading = true;
            try {
              const response = await axios({
                url:'/subject-info/subject-records',
                method:'get',
                params: {
                  page_index: this.subject_info.page,
                  per_page: this.subject_info.per_page,
                  sort_field: this.subject_info.sortField,
                  sort_order: this.subject_info.sortOrder
                },
                headers: {
                  'Authorization': authHeader()
                },
              });
              if (response.status == 200) {
                this.subject_info.subject_record = [];
                this.subject_info.total = response.data.total_results;
                response.data.records.forEach((item) => {
                  this.subject_info.subject_record.push(item);
                  console.log(item);
                });
                this.subject_info.loading = false;
              }
            } catch (error) {
              this.subject_info.subject_record = [];
              this.subject_info.total = 0;
              this.subject_info.loading = false;
              this.$buefy.notification.open({
                duration: 2000,
                message: 'Chịu, đ lấy đc',
                position: 'is-bottom-right',
                type: 'is-danger',
              });
              throw error;
            }
          },
          onStatusSort(field, order) {
                this.subject_info.sortField = field;
                this.subject_info.sortOrder = order;
                this.getSubjectsInfo();
            },
        },
      mounted() {
          this.getSubjectsInfo();
      }
    }
</script>

<style scoped>

</style>
