<!--<template>-->
<!--  <a-layout-content style="padding: 0 50px;">-->
<!--      <a-breadcrumb style="margin: 16px 0">-->
<!--        <a-breadcrumb-item>Home</a-breadcrumb-item>-->
<!--      </a-breadcrumb>-->
<!--      <a-layout id="main-content" style="padding: 24px 0; background: #fff">-->

<!--        &lt;!&ndash;sider&ndash;&gt;-->
<!--        <a-layout-sider width="200" style="background: #fff">-->
<!--          <a-menu-->
<!--            mode="inline"-->
<!--            :defaultSelectedKeys="['1']"-->
<!--            :defaultOpenKeys="['sub1']"-->
<!--            style="height: 100%">-->
<!--            <a-sub-menu key="sub1">-->
<!--              <span slot="title" title="Nhập"><a-icon type="upload" :size="32" title="Nhập"/>Nhập (Import)</span>-->
<!--              <a-menu-item v-on:click="component='upload_student_list'" key="1"><a-icon type="file-add" />Nhập file</a-menu-item>-->
<!--              <a-menu-item v-on:click="component='input_student'"><a-icon type="form" />Nhập tay</a-menu-item>-->
<!--            </a-sub-menu>-->
<!--            <a-sub-menu>-->
<!--              <span slot="title" title="Xem & Cập nhật danh sách sinh viên"><a-icon type="edit" />Xem & Cập nhật danh sách sinh viên</span>-->
<!--              <a-menu-item v-on:click="component='record_management'"><a-icon type="ordered-list" />Danh sách</a-menu-item>-->
<!--            </a-sub-menu>-->
<!--          </a-menu>-->

<!--        </a-layout-sider>-->
<!--        &lt;!&ndash;sider&ndash;&gt;-->

<!--        &lt;!&ndash;content&ndash;&gt;-->
<!--        <a-layout-content :style="{ padding: '0 24px', minHeight: '280px' , position: 'relative', margin: 'auto' }" >-->
<!--            <keep-alive>-->
<!--              <component v-bind:is="component" />-->
<!--            </keep-alive>-->
<!--        </a-layout-content>-->
<!--        &lt;!&ndash;content&ndash;&gt;-->

<!--      </a-layout>-->
<!--    </a-layout-content>-->
<!--</template>-->
<!--<script>-->
<!--  import upload_student_list from './import/upload.vue';-->
<!--  import input_student from './import/input.vue';-->
<!--  import record_management from "./student_record_management/record_management";-->

<!--  export default {-->
<!--      name: 'student_management',-->
<!--      components: {-->
<!--          upload_student_list, input_student, record_management-->
<!--      },-->
<!--      data() {-->
<!--          return {-->
<!--              component: upload_student_list,-->
<!--          }-->
<!--      },-->
<!--  }-->
<!--</script>-->
<!--<style>-->
<!--  @media screen and (max-width: 400px) {-->
<!--    #main-content {-->
<!--      overflow-x: scroll;-->
<!--    }-->
<!--  }-->
<!--  #main-content {-->

<!--  }-->
<!--</style>-->

<template>
  <div>
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li>Quản lý sinh viên </li>
      </ul>
    </nav>
    <section id="tab-action">
        <b-tabs type="is-boxed">
            <b-tab-item label="Nhập (Import)">
              <component v-bind:is="import_insert"/>
<!--              <section>-->
<!--                <b-field label="Name">-->
<!--                    <b-input></b-input>-->
<!--                </b-field>-->

<!--                <b-field label="Email"-->
<!--                    type="is-danger"-->
<!--                    message="This email is invalid">-->
<!--                    <b-input type="email"-->
<!--                        value="john@"-->
<!--                        maxlength="30">-->
<!--                    </b-input>-->
<!--                </b-field>-->

<!--                <b-field label="Username"-->
<!--                    type="is-success"-->
<!--                    message="This username is available">-->
<!--                    <b-input value="johnsilver" maxlength="30"></b-input>-->
<!--                </b-field>-->

<!--                <b-field label="Password">-->
<!--                    <b-input type="password"-->
<!--                        value="iwantmytreasure"-->
<!--                        password-reveal>-->
<!--                    </b-input>-->
<!--                </b-field>-->

<!--                <b-field label="Message">-->
<!--                    <b-input maxlength="200" type="textarea"></b-input>-->
<!--                </b-field>-->
<!--            </section>-->
            </b-tab-item>
            <b-tab-item label="Xem & Cập nhật danh sách sinh viên">
              <component v-bind:is="record_management"/>
            </b-tab-item>
        </b-tabs>
    </section>
    <section>
    </section>
  </div>
</template>
<script>
  import record_management from "./student_record_management/record_management";
  import import_insert from './import/import_input';

  export default {
      name: 'student_management',
      components: {
          import_insert, record_management
      },
      data() {
          return {
              record_management,
              import_insert,
          }
      },
  }
</script>

