<template>
  <section>
    <b-field>
      <b-button
        :class="{}"
        class="button"
        @click=""
      >
        <b-icon
          size="is-small"
          icon="sync"/>
        <span>Làm mới</span>
      </b-button>
      <b-autocomplete
                :data="search.searchResults"
                placeholder="Tìm kiếm bằng mã kỳ thi"
                icon="search"
                field="ID"
                :loading="search.searchLoading"
                @typing=""
                @select=""
                expanded>
      </b-autocomplete>
      <b-table
            paginated
            backend-pagination
            detailed
            @page-change=""
            aria-next-label="Next page"
            aria-previous-label="Previous page"
            aria-page-label="Page"
            aria-current-label="Current page"
            backend-sorting
            hoverable
            detail-key="ID"
            :opened-detailed="student_status.ID_Index"
            :default-sort-direction="student.defaultSortOrder"
            :default-sort="[student.sortField, student.sortOrder]"
            @sort="onStudentSort"
            @details-open="(row, index) => { student_status.currentStudentID = row.ID ; getStudent_Subject(); closeOtherDetails(row, index) }"
            @details-close="(row, index) => { student_status.student_subject_record = [] }"
            :show-detail-icon="true">
        <template slot-scope="props">
          <b-table-column field="SemesterID" sortable>
            102312093812
          </b-table-column>
          <b-table-column field="SemesterName" sortable>
            Cuối kì 2019
          </b-table-column>
          <b-table-column field="Action" width="90">
                    <b-button type="is-warning" size="is-small" icon-pack="fas" icon-right="edit" outlined @click.prevent="onStudentEdit(props.row)"></b-button>
                    <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onStudentDelete(props.row.ID)"></b-button>
          </b-table-column>
        </template>
        <template slot="detail" slot-scope="props">
          <b-field grouped group-multiline>
            <b-button
              :class="{'is-loading': student_status.loading}"
              class="button"
              @click="getStudent_Subject(props.row)"
            >
              <b-icon
                size="is-small"
                icon="sync"/>
            </b-button>
          </b-field>
          <b-field v-if="" grouped group-multiline>
            <b-table
              paginated
              backend-pagination
              @page-change=""
              aria-next-label="Next page"
              aria-previous-label="Previous page"
              aria-page-label="Page"
              aria-current-label="Current page"
              backend-sorting
              bordered
              narrowed
              hoverable
              detail-key="ID"
              :default-sort-direction="student_status.defaultSortOrder"
              :default-sort="[student_status.sortField, student_status.sortOrder]"
              @sort="onStatusSort">
                <template slot-scope="props">
                  <b-table-column field="SubjectID" label="Mã môn" sortable>
                    {{}}
                  </b-table-column>
                  <b-table-column field="SubjectTitle" label="Tên môn" sortable>
                    {{}}
                  </b-table-column>
                  <b-table-column field="Action">
                    <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent=""></b-button>
                  </b-table-column>
                </template>
            </b-table>
          </b-field>
        </template>
      </b-table>
    </b-field>
  </section>
</template>

<script>
    export default {
        name: "semester_management",
    }
</script>

<style scoped>

</style>
