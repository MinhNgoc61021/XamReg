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
            :data="data"
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
                <b-table-column field="ID" label="ID" sortable>
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
    import {authHeader} from "../../../api/jwt_handling";

    export default {
        data() {
            return {
                data: [],
                total: 0,
                loading: false,
                sortField: 'ID',
                sortOrder: 'desc',
                defaultSortOrder: 'desc',
                page: 1,
                per_page: 5
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
                        // api.themoviedb.org manage max 1000 pages
                        // console.log(response);
                        this.data = [];
                        // let currentTotal = response.data.total_results;
                        // if (data.total_results / this.perPage > 1000) {
                        //     currentTotal = this.perPage * 1000
                        // }
                        this.total = response.data.total_results;
                        // console.log(response.data.records);
                        response.data.records.forEach((item) => {
                            this.data.push(item);
                        });
                        // console.log(this.data);
                        this.loading = false
                    })
                    .catch((error) => {
                        this.data = [];
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
                this.getRecordData()
            },
            async onDelete(recordID) {
                console.log(recordID);
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
                                    studentID: recordID,
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
                            console.log(e);
                        }
                    },
                });
            },
            async onEdit(record) {
                console.log(record.ID)
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

<!--<template>-->
<!--    <section>-->
<!--        <button class="button is-primary is-medium"-->
<!--            @click="isComponentModalActive = true">-->
<!--            Launch component modal-->
<!--        </button>-->

<!--        <b-modal :active.sync="isComponentModalActive"-->
<!--            has-modal-card full-screen :can-cancel="false">-->
<!--            <modal-form v-bind="formProps"></modal-form>-->
<!--        </b-modal>-->
<!--    </section>-->
<!--</template>-->

<!--<script>-->
<!--    const ModalForm = {-->
<!--        props: ['email', 'password'],-->
<!--        template: `-->
<!--            <div class="modal-card" style="width: auto">-->
<!--                <header class="modal-card-head">-->
<!--                    <p class="modal-card-title">Login</p>-->
<!--                </header>-->
<!--                <section class="modal-card-body">-->
<!--                    <b-field label="Email">-->
<!--                        <b-input-->
<!--                            type="email"-->
<!--                            :value="email"-->
<!--                            placeholder="Your email"-->
<!--                            required>-->
<!--                        </b-input>-->
<!--                    </b-field>-->

<!--                    <b-field label="Password">-->
<!--                        <b-input-->
<!--                            type="password"-->
<!--                            :value="password"-->
<!--                            password-reveal-->
<!--                            placeholder="Your password"-->
<!--                            required>-->
<!--                        </b-input>-->
<!--                    </b-field>-->

<!--                    <b-checkbox>Remember me</b-checkbox>-->
<!--                </section>-->
<!--                <footer class="modal-card-foot">-->
<!--                    <button class="button" type="button" @click="$parent.close()">Close</button>-->
<!--                    <button class="button is-primary">Login</button>-->
<!--                </footer>-->
<!--            </div>-->
<!--        `-->
<!--    }-->

<!--    export default {-->
<!--        components: {-->
<!--            ModalForm-->
<!--        },-->
<!--        data() {-->
<!--            return {-->
<!--                isComponentModalActive: false,-->
<!--                formProps: {-->
<!--                    email: 'evan@you.com',-->
<!--                    password: 'testing'-->
<!--                }-->
<!--            }-->
<!--        }-->
<!--    }-->
<!--</script>-->
