<template>
  <div>
    <div>Mã kì thi: {{course_id}}</div>
    <div>Tên kì thi: {{course_name}}</div>
    <a-list size="small" bordered :dataSource="subjects">
      <div slot="header">Danh sách môn thi</div>
      <a-list-item slot="renderItem" slot-scope="subject, index">
        <a @click="showModal">
          Mã môn học: {{subject.id}}
          <br>
          Tên môn học: {{subject.name}}
        </a>
        <a-modal
            title="Thông tin ca thi"
            :visible="visible"
            @ok="handleOk"
            :confirmLoading="confirmLoading"
            @cancel="handleCancel"
            >
            <Shift_detail/>
        </a-modal>
      </a-list-item>
    </a-list>
  </div>
</template>

<script>
import Shift_detail from "./Shift_detail"
export default {
  name: "Course_detail",
  components: {
    Shift_detail,
  },
  data() {
    return {
      visible:false,
      confirmLoading: false,
      course_id: "HK1_2019",
      course_name: "Thi cuối kì 1 2019",
      subjects: [
          {
            id: "BULLSHIT1",
            name: "Tư tưởng cc",
          },
          {
            id: "BULLSHIT2",
            name: "Tín hiệu cc",
          },
          {
            id: "BULLSHIT3",
            name: "Xác suất cc",
          }
      ]
    }
  },
  methods: {
    showModal() {
        this.visible = true;
      },
    handleOk(e) {
        this.ModalText = 'The modal will be closed after two seconds';
        this.confirmLoading = true;
        setTimeout(() => {
          this.visible = false;
          this.confirmLoading = false;
        }, 2000);
      },
    handleCancel(e) {
        console.log('Clicked cancel button');
        this.visible = false;
      },
  }
}
</script>

<style>

</style>
