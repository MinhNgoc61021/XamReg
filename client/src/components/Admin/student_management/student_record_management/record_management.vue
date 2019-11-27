<template>
    <section>

        <b-table
            :data="data"
            ref="table"
            detailed
            hoverable
            custom-detail-row
            :opened-detailed="['Board Games']"
            :default-sort="['name', 'asc']"
            detail-key="name"
            @details-open="(row, index) => $buefy.toast.open(`Expanded ${row.name}`)"
            :show-detail-icon="false">

            <template slot-scope="props">
                <b-table-column
                    field="name"
                    :visible="columnsVisible['name'].display"
                    :label="columnsVisible['name'].title"
                    width="300"
                    sortable
                >
                    <template v-if="showDetailIcon">
                        {{ props.row.name }}
                    </template>
                    <template v-else>
                        <a @click="toggle(props.row)">
                            {{ props.row.name }}
                        </a>
                    </template>
                </b-table-column>

                <b-table-column
                    field="sold"
                    :visible="columnsVisible['sold'].display"
                    :label="columnsVisible['sold'].title"
                    sortable
                    centered
                >
                    {{ props.row.sold }}
                </b-table-column>

                <b-table-column
                    field="available"
                    :visible="columnsVisible['available'].display"
                    :label="columnsVisible['available'].title"
                    sortable
                    centered
                >
                    {{ props.row.available }}
                </b-table-column>

                <b-table-column
                    :visible="columnsVisible['cleared'].display"
                    :label="columnsVisible['cleared'].title"
                    centered
                >
                    <span :class="
                            [
                                'tag',
                                {'is-danger': props.row.sold / props.row.available <= 0.45},
                                {'is-success': props.row.sold / props.row.available > 0.45}
                            ]">
                        {{ Math.round((props.row.sold / props.row.available) * 100) }}%
                    </span>
                </b-table-column>
            </template>

            <template slot="detail" slot-scope="props">
                <tr v-for="item in props.row.items" :key="item.name">
                    <td v-if="showDetailIcon"></td>
                    <td v-show="columnsVisible['name'].display" >&nbsp;&nbsp;&nbsp;&nbsp;{{ item.name }}</td>
                    <td v-show="columnsVisible['sold'].display" class="has-text-centered">{{ item.sold }}</td>
                    <td v-show="columnsVisible['available'].display" class="has-text-centered">{{ item.available }}</td>
                    <td v-show="columnsVisible['cleared'].display" class="has-text-centered">
                        <span :class="
                            [
                                'tag',
                                {'is-danger': item.sold / item.available <= 0.45},
                                {'is-success': item.sold / item.available > 0.45}
                            ]">
                            {{ Math.round((item.sold / item.available) * 100) }}%
                        </span>
                    </td>
                </tr>
            </template>
        </b-table>

    </section>
</template>

<script>
    export default {
        data() {
            return {
                data: [
                    {
                        name: 'Board Games',
                        sold: 131,
                        available: 301,
                        items: [
                            {
                                name: 'Monopoly',
                                sold: 57,
                                available: 100
                            },
                            {
                                name: 'Scrabble',
                                sold: 23,
                                available: 84
                            },
                            {
                                name: 'Chess',
                                sold: 37,
                                available: 61
                            },
                            {
                                name: 'Battleships',
                                sold: 14,
                                available: 56
                            }
                        ]
                    },
                    {
                        name: 'Jigsaws & Puzzles',
                        sold: 88,
                        available: 167,
                        items: [
                            {
                                name: 'World Map',
                                sold: 31,
                                available: 38
                            },
                            {
                                name: 'London',
                                sold: 23,
                                available: 29
                            },
                            {
                                name: 'Sharks',
                                sold: 20,
                                available: 44
                            },
                            {
                                name: 'Disney',
                                sold: 14,
                                available: 56
                            }
                        ]
                    },
                    {
                        name: 'Books',
                        sold: 434,
                        available: 721,
                        items: [
                            {
                                name: 'Hamlet',
                                sold: 101,
                                available: 187
                            },
                            {
                                name: 'The Lord Of The Rings',
                                sold: 85,
                                available: 156
                            },
                            {
                                name: 'To Kill a Mockingbird',
                                sold: 78,
                                available: 131
                            },
                            {
                                name: 'Catch-22',
                                sold: 73,
                                available: 98
                            },
                            {
                                name: 'Frankenstein',
                                sold: 51,
                                available: 81
                            },
                            {
                                name: 'Alice\'s Adventures In Wonderland',
                                sold: 46,
                                available: 68
                            }
                        ]
                    }
                ],
                columnsVisible: {
                    name: { title: 'Name', display: true },
                    sold: { title: 'Stock Sold', display: true },
                    available: { title: 'Stock Available', display: true },
                    cleared: { title: 'Stock Cleared', display: true },
                },
                showDetailIcon: false
            }
        },
        methods: {
            toggle(row) {
                this.$refs.table.toggleDetails(row)
            }
        }
    }
</script>




<!--<template>-->
<!--    <section>-->
<!--        <b-table-->
<!--            :data="data"-->
<!--            :loading="loading"-->

<!--            paginated-->
<!--            backend-pagination-->
<!--            :total="total"-->
<!--            :per-page="perPage"-->
<!--            @page-change="onPageChange"-->
<!--            aria-next-label="Next page"-->
<!--            aria-previous-label="Previous page"-->
<!--            aria-page-label="Page"-->
<!--            aria-current-label="Current page"-->

<!--            backend-sorting-->
<!--            :default-sort-direction="defaultSortOrder"-->
<!--            :default-sort="[sortField, sortOrder]"-->
<!--            @sort="onSort">-->

<!--            <template slot-scope="props">-->
<!--                <b-table-column field="original_title" label="Title" sortable>-->
<!--                    {{ props.row.original_title }}-->
<!--                </b-table-column>-->

<!--                <b-table-column field="vote_average" label="Vote Average" numeric sortable>-->
<!--                    <span class="tag" :class="type(props.row.vote_average)">-->
<!--                        {{ props.row.vote_average }}-->
<!--                    </span>-->
<!--                </b-table-column>-->

<!--                <b-table-column field="vote_count" label="Vote Count" numeric sortable>-->
<!--                     {{ props.row.vote_count }}-->
<!--                </b-table-column>-->

<!--                <b-table-column field="release_date" label="Release Date" sortable centered>-->
<!--                    {{ props.row.release_date ? new Date(props.row.release_date).toLocaleDateString() : '' }}-->
<!--                </b-table-column>-->

<!--                <b-table-column label="Overview" width="500">-->
<!--                    {{ props.row.overview | truncate(80) }}-->
<!--                </b-table-column>-->
<!--            </template>-->
<!--        </b-table>-->
<!--    </section>-->
<!--</template>-->

<!--<script>-->
<!--    export default {-->
<!--        data() {-->
<!--            return {-->
<!--                data: [],-->
<!--                total: 0,-->
<!--                loading: false,-->
<!--                sortField: 'vote_count',-->
<!--                sortOrder: 'desc',-->
<!--                defaultSortOrder: 'desc',-->
<!--                page: 1,-->
<!--                perPage: 20-->
<!--            }-->
<!--        },-->
<!--        methods: {-->
<!--            /*-->
<!--        * Load async data-->
<!--        */-->
<!--            loadAsyncData() {-->
<!--                const params = [-->
<!--                    'api_key=bb6f51bef07465653c3e553d6ab161a8',-->
<!--                    'language=en-US',-->
<!--                    'include_adult=false',-->
<!--                    'include_video=false',-->
<!--                    `sort_by=${this.sortField}.${this.sortOrder}`,-->
<!--                    `page=${this.page}`-->
<!--                ].join('&')-->

<!--                this.loading = true-->
<!--                this.$http.get(`https://api.themoviedb.org/3/discover/movie?${params}`)-->
<!--                    .then(({ data }) => {-->
<!--                        // api.themoviedb.org manage max 1000 pages-->
<!--                        this.data = []-->
<!--                        let currentTotal = data.total_results-->
<!--                        if (data.total_results / this.perPage > 1000) {-->
<!--                            currentTotal = this.perPage * 1000-->
<!--                        }-->
<!--                        this.total = currentTotal-->
<!--                        data.results.forEach((item) => {-->
<!--                            item.release_date = item.release_date.replace(/-/g, '/')-->
<!--                            this.data.push(item)-->
<!--                        })-->
<!--                        this.loading = false-->
<!--                    })-->
<!--                    .catch((error) => {-->
<!--                        this.data = []-->
<!--                        this.total = 0-->
<!--                        this.loading = false-->
<!--                        throw error-->
<!--                    })-->
<!--            },-->
<!--            /*-->
<!--        * Handle page-change event-->
<!--        */-->
<!--            onPageChange(page) {-->
<!--                this.page = page-->
<!--                this.loadAsyncData()-->
<!--            },-->
<!--            /*-->
<!--        * Handle sort event-->
<!--        */-->
<!--            onSort(field, order) {-->
<!--                this.sortField = field-->
<!--                this.sortOrder = order-->
<!--                this.loadAsyncData()-->
<!--            },-->
<!--            /*-->
<!--        * Type style in relation to the value-->
<!--        */-->
<!--            type(value) {-->
<!--                const number = parseFloat(value)-->
<!--                if (number < 6) {-->
<!--                    return 'is-danger'-->
<!--                } else if (number >= 6 && number < 8) {-->
<!--                    return 'is-warning'-->
<!--                } else if (number >= 8) {-->
<!--                    return 'is-success'-->
<!--                }-->
<!--            }-->
<!--        },-->
<!--        filters: {-->
<!--            /**-->
<!--        * Filter to truncate string, accepts a length parameter-->
<!--        */-->
<!--            truncate(value, length) {-->
<!--                return value.length > length-->
<!--                    ? value.substr(0, length) + '...'-->
<!--                    : value-->
<!--            }-->
<!--        },-->
<!--        mounted() {-->
<!--            this.loadAsyncData()-->
<!--        }-->
<!--    }-->
<!--</script>-->
