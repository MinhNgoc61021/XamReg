<template>
    <div class="container">
        <h1 class="title is-3">Đăng ký thi</h1>
        <h2 class="subtitle is-6">Sinh viên đăng ký ca thi mà sinh viên đủ điều kiện dự thi và đang còn chỗ trống</h2>
      <b-field grouped group-multiline>
        <b-button
          :class="{'is-loading': student.loading}"
          class="button"
          @click="getStudentRecordData"
        >
          <b-icon
            size="is-small"
            icon="edit"/>
          <span>Làm mới</span>
        </b-button>
        <b-autocomplete
          :data="search.searchResults"
          placeholder="Tìm kiếm bằng mã môn học"
          icon="search"
          field="ID"
          :loading="search.searchLoading"
          @typing="onStudentSearch"
          @select="option => student.student_record = [option]"
          expanded>
          <template slot-scope="props">
            <div class="media">
              <div class="media-left">
                <b-icon icon-pack="fas" icon="user-circle"></b-icon>
              </div>
              <div class="media-content">
                <b>Mã môn học: </b>{{ props.option.ID }}
                <br>
                <b>Tên môn học: </b>{{ props.option.Fullname }}
              </div>
            </div>
          </template>
        </b-autocomplete>
      </b-field>

      <b-table
            :data="student.student_record"
            :loading="student.loading"
            paginated
            backend-pagination
            detailed
            :total="student.total"
            :per-page="student.per_page"
            @page-change="onStudentPageChange"
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
          <b-table-column field="ID" label="Mã môn học" sortable>
            {{ props.row.ID }}
          </b-table-column>

          <b-table-column field="Fullname" label="Tên môn học" sortable>
            {{ props.row.Fullname }}
          </b-table-column>
        </template>
        <template slot="detail" slot-scope="props">
          <h4 class="title is-4">Danh sách ca thi</h4>
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
          <b-field v-if="student_status.student_subject_record.length > 0" grouped group-multiline>
            <b-table
              :data="student_status.student_subject_record"
              :loading="student_status.loading"
              paginated
              backend-pagination
              :total="student_status.total"
              :per-page="student_status.per_page"
              @page-change="onStatusPageChange"
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
                  {{ props.row.SubjectID }}
                </b-table-column>
                <b-table-column field="SubjectTitle" label="Tên môn" sortable>
                  {{ props.row.SubjectTitle }}
                </b-table-column>
                <b-table-column field="Action">
                  <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onStatusDelete(props.row.SubjectID)"></b-button>
                </b-table-column>
              </template>
            </b-table>
          </b-field>
          <b-field v-else>
            <b-message type="is-danger" has-icon>
                    Hiện tại sinh viên này chưa có thông tin về danh sách này, bạn hãy tải lên file <b-icon icon="file-excel"></b-icon> Excel định dạng <b>.xlsx</b> ở phần <b>Nhập (Import)</b>!
            </b-message>
          </b-field>
        </template>
      </b-table>

      <b-table
          :data="subject_info.subject_record"
          :loading="subject_info.loading"
          backend-sorting
          hoverable
          :default-sort-direction="subject_info.defaultSortOrder"
          :default-sort="[subject_info.sortField, subject_info.sortOrder]"
          @sort="onStatusSort"
        >
          <template slot-scope="props" style="width: 500px">
            <b-table-column field="SubjectID" label="Mã ca thi" sortable>
              {{props.row.SubjectID}}
            </b-table-column>
            <b-table-column field="SubjectTitle" label="Tên môn thi" sortable>
              {{props.row.SubjectTitle}}
            </b-table-column>
            <b-table-column field="SubjectTitle" label="Tên phòng thi" sortable>
              {{props.row.SubjectTitle}}
            </b-table-column>
            <b-table-column field="SubjectTitle" label="Ngày thi" sortable>
              {{props.row.SubjectTitle}}
            </b-table-column>
            <b-table-column field="SubjectTitle" label="Giờ thi" sortable>
              {{props.row.SubjectTitle}}
            </b-table-column>
            <b-table-column field="Action">
              <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onStatusDelete(props.row)"></b-button>
            </b-table-column>
          </template>
        </b-table>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                isOpen: 0,
                collapses: [
                {
                    title: 'Danh sách ca thi',
                    shift_info: {
                      shift_record: [],
                      total: 0,
                      loading: false,
                      sortField: 'ShiftID',
                      sortOrder: 'desc',
                      defaultSortOrder: 'desc',
                      page: 1,
                      per_page: 5,
                    }
                },
                {
                    title: 'Danh sách ca thi đã chọn',
                    shifts: 'Text 2'
                }
                ]
            }
        }
    }
</script>
