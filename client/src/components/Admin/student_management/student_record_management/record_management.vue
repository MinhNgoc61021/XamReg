<!--<template>-->
<!--  <a-table-->
<!--    :columns="columns"-->
<!--    :rowKey="record => record.login.uuid"-->
<!--    :dataSource="data"-->
<!--    :pagination="pagination"-->
<!--    :loading="loading"-->
<!--    @change="handleTableChange">-->
<!--    <template slot="name" slot-scope="name">-->
<!--      {{name.first}} {{name.last}}-->
<!--    </template>-->
<!--  </a-table>-->
<!--</template>-->
<!--<script>-->
<!--  import axios from 'axios';-->
<!--  const columns = [-->
<!--    {-->
<!--      title: 'Tên',-->
<!--      dataIndex: 'ID',-->
<!--      sorter: true,-->
<!--      width: '20%',-->
<!--      scopedSlots: { customRender: 'name' },-->
<!--    },-->
<!--    {-->
<!--      title: 'Giới tính',-->
<!--      dataIndex: 'gender',-->
<!--      filters: [{ text: 'Nam', value: 'male' }, { text: 'Nữ', value: 'female' }],-->
<!--      width: '20%',-->
<!--    },-->
<!--    {-->
<!--      title: 'Email',-->
<!--      dataIndex: 'email',-->
<!--    },-->

<!--  ];-->

<!--  export default {-->
<!--    mounted() {-->
<!--      this.fetch();-->
<!--    },-->
<!--    data() {-->
<!--      return {-->
<!--        data: [],-->
<!--        pagination: {},-->
<!--        loading: false,-->
<!--        columns,-->
<!--      };-->
<!--    },-->
<!--    methods: {-->
<!--      handleTableChange(pagination, filters, sorter) {-->
<!--        console.log(pagination);-->
<!--        const pager = { ...this.pagination };-->
<!--        pager.current = pagination.current;-->
<!--        this.pagination = pager;-->
<!--        this.fetch({-->
<!--          results: pagination.pageSize,-->
<!--          page: pagination.current,-->
<!--          sortField: sorter.field,-->
<!--          sortOrder: sorter.order,-->
<!--          ...filters,-->
<!--        });-->
<!--      },-->
<!--      fetch(params = {}) {-->
<!--        console.log('params:', params);-->
<!--        this.loading = true;-->
<!--        axios({-->
<!--          url: 'https://randomuser.me/api',-->
<!--          method: 'get',-->
<!--          data: {-->
<!--            results: 10,-->
<!--            ...params,-->
<!--          },-->
<!--          type: 'json',-->
<!--        }).then(data => {-->
<!--          const pagination = { ...this.pagination };-->
<!--          // Read total count from server-->
<!--          // pagination.total = data.totalCount;-->
<!--          pagination.total = 200;-->
<!--          this.loading = false;-->
<!--          this.data = data.results;-->
<!--          this.pagination = pagination;-->
<!--        });-->
<!--      },-->
<!--    },-->
<!--  };-->
<!--</script>-->


<template>

</template>
<script>

</script>
<style>

</style>
