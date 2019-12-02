<template>
    <section>
      <br><br><br><br>
        <b-table
            :data="data"
            ref="table"
            detailed
            hoverable
            custom-detail-row
            :default-sort="['name', 'asc']"
            detail-key="name"
            @details-open="handleDetailOpen(row, index)"
            >

            <template slot-scope="props">
                <b-table-column
                    field="name"
                    :visible="columnsVisible['name'].display"
                    :label="columnsVisible['name'].title"
                    width="300"
                    sortable
                >
                  {{ props.row.name }}

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
                bgame : [{name: 'Monopoly',
                      sold: 57,
                      available: 100
                     },
                     {
                      name: 'Scrabble',
                      sold: 23,
                      available: 84
                     }],
                data: [
                    {
                        name: 'Board Games',
                        sold: 131,
                        available: 301,
                        items:[]
                    },
                    {
                        name: 'Jigsaws & Puzzles',
                        sold: 88,
                        available: 167,
                        items: []
                    }
                ],
                columnsVisible: {
                    name: { title: 'Name', display: true },
                    sold: { title: 'Stock Sold', display: true },
                    available: { title: 'Stock Available', display: true },
                    cleared: { title: 'Stock Cleared', display: true },

                },
                showDetailIcon: true
            }
        },
        methods: {
            toggle(row) {
                this.$refs.table.toggleDetails(row)
            },
            handleDetailOpen(row, index){
                row.items += this.y
            }
        }
    }
</script>
