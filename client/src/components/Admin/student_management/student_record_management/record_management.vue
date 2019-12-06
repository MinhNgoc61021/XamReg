<!--<template>-->
<!--    <section>-->

<!--        <b-table-->
<!--            :data="data"-->
<!--            ref="table"-->
<!--            detailed-->
<!--            hoverable-->
<!--            custom-detail-row-->
<!--            :opened-detailed="['Board Games']"-->
<!--            :default-sort="['name', 'asc']"-->
<!--            detail-key="name"-->
<!--            @details-open="(row, index) => $buefy.toast.open(`Expanded ${row.name}`)"-->
<!--            :show-detail-icon="false">-->

<!--            <template slot-scope="props">-->
<!--                <b-table-column-->
<!--                    field="name"-->
<!--                    :visible="columnsVisible['name'].display"-->
<!--                    :label="columnsVisible['name'].title"-->
<!--                    width="300"-->
<!--                    sortable-->
<!--                >-->
<!--                    <template v-if="showDetailIcon">-->
<!--                        {{ props.row.name }}-->
<!--                    </template>-->
<!--                    <template v-else>-->
<!--                        <a @click="toggle(props.row)">-->
<!--                            {{ props.row.name }}-->
<!--                        </a>-->
<!--                    </template>-->
<!--                </b-table-column>-->

<!--                <b-table-column-->
<!--                    field="sold"-->
<!--                    :visible="columnsVisible['sold'].display"-->
<!--                    :label="columnsVisible['sold'].title"-->
<!--                    sortable-->
<!--                    centered-->
<!--                >-->
<!--                    {{ props.row.sold }}-->
<!--                </b-table-column>-->

<!--                <b-table-column-->
<!--                    field="available"-->
<!--                    :visible="columnsVisible['available'].display"-->
<!--                    :label="columnsVisible['available'].title"-->
<!--                    sortable-->
<!--                    centered-->
<!--                >-->
<!--                    {{ props.row.available }}-->
<!--                </b-table-column>-->

<!--                <b-table-column-->
<!--                    :visible="columnsVisible['cleared'].display"-->
<!--                    :label="columnsVisible['cleared'].title"-->
<!--                    centered-->
<!--                >-->
<!--                    <span :class="-->
<!--                            [-->
<!--                                'tag',-->
<!--                                {'is-danger': props.row.sold / props.row.available <= 0.45},-->
<!--                                {'is-success': props.row.sold / props.row.available > 0.45}-->
<!--                            ]">-->
<!--                        {{ Math.round((props.row.sold / props.row.available) * 100) }}%-->
<!--                    </span>-->
<!--                </b-table-column>-->
<!--            </template>-->

<!--            <template slot="detail" slot-scope="props">-->
<!--                <tr v-for="item in props.row.items" :key="item.name">-->
<!--                    <td v-if="showDetailIcon"></td>-->
<!--                    <td v-show="columnsVisible['name'].display" >&nbsp;&nbsp;&nbsp;&nbsp;{{ item.name }}</td>-->
<!--                    <td v-show="columnsVisible['sold'].display" class="has-text-centered">{{ item.sold }}</td>-->
<!--                    <td v-show="columnsVisible['available'].display" class="has-text-centered">{{ item.available }}</td>-->
<!--                    <td v-show="columnsVisible['cleared'].display" class="has-text-centered">-->
<!--                        <span :class="-->
<!--                            [-->
<!--                                'tag',-->
<!--                                {'is-danger': item.sold / item.available <= 0.45},-->
<!--                                {'is-success': item.sold / item.available > 0.45}-->
<!--                            ]">-->
<!--                            {{ Math.round((item.sold / item.available) * 100) }}%-->
<!--                        </span>-->
<!--                    </td>-->
<!--                </tr>-->
<!--            </template>-->
<!--        </b-table>-->

<!--    </section>-->
<!--</template>-->

<!--<script>-->
<!--    export default {-->
<!--        data() {-->
<!--            return {-->
<!--                data: [-->
<!--                    {-->
<!--                        name: 'Board Games',-->
<!--                        sold: 131,-->
<!--                        available: 301,-->
<!--                        items: [-->
<!--                            {-->
<!--                                name: 'Monopoly',-->
<!--                                sold: 57,-->
<!--                                available: 100-->
<!--                            },-->
<!--                            {-->
<!--                                name: 'Scrabble',-->
<!--                                sold: 23,-->
<!--                                available: 84-->
<!--                            },-->
<!--                            {-->
<!--                                name: 'Chess',-->
<!--                                sold: 37,-->
<!--                                available: 61-->
<!--                            },-->
<!--                            {-->
<!--                                name: 'Battleships',-->
<!--                                sold: 14,-->
<!--                                available: 56-->
<!--                            }-->
<!--                        ]-->
<!--                    },-->
<!--                    {-->
<!--                        name: 'Jigsaws & Puzzles',-->
<!--                        sold: 88,-->
<!--                        available: 167,-->
<!--                        items: [-->
<!--                            {-->
<!--                                name: 'World Map',-->
<!--                                sold: 31,-->
<!--                                available: 38-->
<!--                            },-->
<!--                            {-->
<!--                                name: 'London',-->
<!--                                sold: 23,-->
<!--                                available: 29-->
<!--                            },-->
<!--                            {-->
<!--                                name: 'Sharks',-->
<!--                                sold: 20,-->
<!--                                available: 44-->
<!--                            },-->
<!--                            {-->
<!--                                name: 'Disney',-->
<!--                                sold: 14,-->
<!--                                available: 56-->
<!--                            }-->
<!--                        ]-->
<!--                    },-->
<!--                    {-->
<!--                        name: 'Books',-->
<!--                        sold: 434,-->
<!--                        available: 721,-->
<!--                        items: [-->
<!--                            {-->
<!--                                name: 'Hamlet',-->
<!--                                sold: 101,-->
<!--                                available: 187-->
<!--                            },-->
<!--                            {-->
<!--                                name: 'The Lord Of The Rings',-->
<!--                                sold: 85,-->
<!--                                available: 156-->
<!--                            },-->
<!--                            {-->
<!--                                name: 'To Kill a Mockingbird',-->
<!--                                sold: 78,-->
<!--                                available: 131-->
<!--                            },-->
<!--                            {-->
<!--                                name: 'Catch-22',-->
<!--                                sold: 73,-->
<!--                                available: 98-->
<!--                            },-->
<!--                            {-->
<!--                                name: 'Frankenstein',-->
<!--                                sold: 51,-->
<!--                                available: 81-->
<!--                            },-->
<!--                            {-->
<!--                                name: 'Alice\'s Adventures In Wonderland',-->
<!--                                sold: 46,-->
<!--                                available: 68-->
<!--                            }-->
<!--                        ]-->
<!--                    }-->
<!--                ],-->
<!--                columnsVisible: {-->
<!--                    name: { title: 'Name', display: true },-->
<!--                    sold: { title: 'Stock Sold', display: true },-->
<!--                    available: { title: 'Stock Available', display: true },-->
<!--                    cleared: { title: 'Stock Cleared', display: true },-->
<!--                },-->
<!--                showDetailIcon: false-->
<!--            }-->
<!--        },-->
<!--        methods: {-->
<!--            toggle(row) {-->
<!--                this.$refs.table.toggleDetails(row)-->
<!--            }-->
<!--        }-->
<!--    }-->
<!--</script>-->




<template>
    <section>
        <div class="control">
        <button
          :class="{'is-loading': loading}"
          class="button"
          @click="getRecordData"
        >
          <b-icon
            size="is-small"
            icon="sync"/>
          <span>Refresh</span>
          </button>
        </div>
        <b-table
            :data="student_record"
            :loading="loading"

            paginated
            backend-pagination
            :total="total"
            :per-page="per_page"
            @page-change="onPageChange"
            aria-next-label="Next page"
            aria-previous-label="Previous page"
            aria-page-label="Page"
            aria-current-label="Current page"
            backend-sorting
            hoverable
            :default-sort-direction="defaultSortOrder"
            :default-sort="[sortField, sortOrder]"
            @sort="onSort">

            <template slot-scope="props">
                <b-table-column field="ID" label="MSSV" sortable>
                    {{ props.row.ID }}
                </b-table-column>

                <b-table-column field="Fullname" label="Họ và tên" sortable>
                     {{ props.row.Fullname }}
                </b-table-column>

                <b-table-column field="Username" label="Tài khoản" sortable>
                    {{ props.row.Username }}
                </b-table-column>

                <b-table-column field="Dob" label="Ngày sinh" sortable>
                    <span class="tag is-success">
                     {{ props.row.Dob }}
                    </span>
                </b-table-column>

                <b-table-column field="CourseID" label="Khóa" sortable>
                     {{ props.row.CourseID }}
                </b-table-column>

                <b-table-column field="Role_Type" label="Quyền" sortable>
                     {{ props.row.Role_Type }}
                </b-table-column>

                <b-table-column field="Gender" label="Giới tính" sortable>
                     {{ props.row.Gender }}
                </b-table-column>

                <b-table-column field="Action" width="120">
                    <b-button type="is-warning" size="is-small" icon-pack="fas" icon-right="edit" outlined @click.prevent="onEdit(props.row)"></b-button>
                    <b-button type="is-danger" size="is-small" icon-pack="fas" icon-right="trash" outlined @click.prevent="onDelete(props.row.ID)"></b-button>
                </b-table-column>
            </template>
        </b-table>
    </section>
</template>

<script>
    import axios from 'axios'
    import { authHeader } from "../../../api/jwt_handling";
    import moment from 'moment/moment';
    /*
     student edit data form
    */
    const editUserForm = {
        // props in component work the same as parameters in a function
        // in here userID prop is used to find the user in the api in order to update the student record
        // editXXX props are used to update the record
        props: ['currentStudentID','currentFullname', 'currentUsername', 'currentCourseID' , 'currentDob', 'currentGender'],
        template: `
            <form @submit.prevent="updateStudentData">
                <div class="modal-card" style="width: 450px;">
                    <header class="modal-card-head">
                        <p class="modal-card-title">Form chỉnh sửa</p>
                    </header>
                    <section class="modal-card-body">
                        <b-field label="MSSV">
                            <b-input
                                type="text"
                                v-model="newStudentID"
                                :value="newStudentID"
                                placeholder="Nhập mã số sinh viên"
                                required>
                            </b-input>
                        </b-field>

                        <b-field label="Tài khoản">
                            <b-input
                                type="email"
                                v-model="newUsername"
                                :value="newUsername"
                                placeholder="Sửa tài khoản"
                                required>
                            </b-input>
                        </b-field>

                        <b-field label="Mã khóa học">
                            <b-input
                                type="text"
                                v-model="newCourseID"
                                :value="newCourseID"
                                placeholder="Sửa mã khóa học"
                                required>
                            </b-input>
                        </b-field>

                        <b-field label="Ngày sinh">
                            <b-datepicker
                                placeholder="Chọn ngày sinh"
                                v-model="newDob"
                                :value="newDob" editable required>
                            </b-datepicker>
                        </b-field>

                        <b-field label="Giới tính">
                            <b-select placeholder="Chọn giới tính" v-model="newGender" :value="newGender" required>
                                <option value="Nam">Nam</option>
                                <option value="Nữ">Nữ</option>
                            </b-select>
                        </b-field>
                    </section>

                    <footer class="modal-card-foot">
                        <button class="button" type="button" @click="$parent.close()">Bỏ qua</button>
                        <button class="button is-primary" type="submit">Cập nhật</button>
                    </footer>
                </div>
            </form>
        `,
        data() {
            return {
                newStudentID: this.currentStudentID,
                newFullname: this.currentFullname,
                newUsername: this.currentUsername,
                newCourseID: this.currentCourseID,
                newDob: this.currentDob,
                newGender: this.currentGender,
            };
        },
        methods: {
            async updateStudentData() {
                try {
                    // console.log(moment(this.newDob).format('MM/DD/YYYY'));
                    const update = await axios({
                        method: 'put',
                        url: '/record/update-record',
                        headers: {
                            'Authorization': authHeader(),
                        },
                        data: {
                            currentStudentID: this.currentStudentID,
                            StudentID: this.newStudentID,
                            Fullname: this.newFullname,
                            Username: this.newUsername,
                            CourseID: this.newCourseID,
                            Dob: moment(this.newDob).format('YYYY-MM-DD'),
                            Gender: this.newGender,
                        },
                    });
                    if (update.status === 200) {
                        this.$parent.close();
                        this.$buefy.notification.open({
                            duration: 1000,
                            message: `Đã cập nhật tài khoản ${this.newStudentID} thành công.`,
                            position: 'is-bottom-right',
                            type: 'is-success',
                        });
                    }

                } catch (e) {
                    if (e['message'].includes('400')) {
                        this.$buefy.notification.open({
                            duration: 1000,
                            message: 'HTTP Status 400: Kiểm tra lại, dữ liệu bạn nhập đang có vấn đề!',
                            position: 'is-bottom-right',
                            type: 'is-danger',
                        })
                    }
                    else if (e['message'].includes('401')) {
                        this.$buefy.notification.open({
                            duration: 1000,
                            message: 'HTTP Status 401: Không được quyền sử dụng!',
                            position: 'is-bottom-right',
                            type: 'is-danger',
                        })
                    }
                }
            },
        },
    };
    export default {
        components: {
            editUserForm,
        },
        data() {
            return {
                student_record: [],
                total: 0,
                loading: false,
                sortField: 'ID',
                sortOrder: 'desc',
                defaultSortOrder: 'desc',
                page: 1,
                per_page: 5,
            }
        },
        methods: {
            /*
             * Load async record data
            */
            getRecordData() {
                this.loading = true;
                axios.get('/record/student-records', {
                    params: {
                        page_index: this.page,
                        per_page: this.per_page,
                        sort_field: this.sortField,
                        sort_order: this.sortOrder
                    },
                    headers: {
                        'Authorization': authHeader(),
                    }
                }).then((response) => {
                        this.student_record = [];
                        this.total = response.data.total_results;
                        response.data.records.forEach((item) => {
                            this.student_record.push(item);
                        });
                        // console.log(this.data);
                        this.loading = false
                    })
                    .catch((error) => {
                        this.student_record = [];
                        this.total = 0;
                        this.loading = false;
                        throw error
                    })
            },
            /*
              * Handle page-change event
            */
            onPageChange(page) {
                this.page = page;
                this.getRecordData();
            },
            /*
              * Handle sort event
            */
            onSort(field, order) {
                this.sortField = field;
                this.sortOrder = order;
                this.getRecordData();
            },
            /*
              * Handle delete record event
            */
            async onDelete(recordID) {
                this.$buefy.dialog.confirm({
                    title: 'Xóa tài khoản',
                    message: `Bạn có chắc chắn là muốn <b>xóa</b> tài khoản ${recordID}? Đã làm thì tự chịu đấy.`,
                    confirmText: 'Xóa!',
                    cancelText: 'Bỏ qua',
                    type: 'is-danger',
                    hasIcon: true,
                    onConfirm: async () => {
                        try {
                            const removeData = await axios({
                                url: '/record/remove-record',
                                method: 'delete',
                                headers: {
                                    'Authorization': authHeader(),
                                },
                                data: {
                                    StudentID: recordID,
                                },
                            });
                            if (removeData.status === 200) {
                                this.$buefy.notification.open({
                                  duration: 1000,
                                  message: `Đã xóa tài khoản ${recordID} thành công.`,
                                  position: 'is-bottom-right',
                                  type: 'is-success',
                                });
                            }
                            this.getRecordData();
                        } catch (e) {
                            if (e['message'].includes('401')) {
                                this.$buefy.notification.open({
                                  duration: 1500,
                                  message: 'HTTP Status 401: Không được quyền sử dụng!',
                                  position: 'is-bottom-right',
                                  type: 'is-danger',
                                })
                            }
                        }
                    },
                });
            },
            onEdit(record) {
                // console.log(record.Dob);
                // console.log(new Date(moment(record.Dob).format('MM/DD/YYYY')));
                this.$buefy.modal.open({
                    parent: this,
                    component: editUserForm,
                    props: {
                        currentStudentID: record.ID,
                        currentFullname: record.Fullname,
                        currentUsername: record.Username,
                        currentCourseID: record.CourseID,
                        currentDob: new Date(moment(record.Dob).format('MM/DD/YYYY')),
                        currentGender: record.Gender,
                    },
                    hasModalCard: true,
                    customClass: 'custom-class custom-class-2',
                });
            },
            /*
              * Type style in relation to the value
            */
            type(value) {
                const number = parseFloat(value);
                if (number < 6) {
                    return 'is-danger'
                } else if (number >= 6 && number < 8) {
                    return 'is-warning'
                } else if (number >= 8) {
                    return 'is-success'
                }
            }
        },
        filters: {
            /**
        * Filter to truncate string, accepts a length parameter
        */
            truncate(value, length) {
                return value.length > length
                    ? value.substr(0, length) + '...'
                    : value
            }
        },
        mounted() {
            this.getRecordData();
        }
    }
</script>
