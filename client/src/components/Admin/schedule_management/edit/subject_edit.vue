<template>
  <form @submit.prevent="updateSubjectData()">
    <div class="modal-card" style="width: 450px;">
        <header class="modal-card-head">
            <p class="modal-card-title">Form chỉnh sửa</p>
        </header>

      <section class="modal-card-body">
        <b-field label="Mã môn thi">
          <b-input
            type="text"
            v-model="newSubjectID"
            :value="newSubjectID"
            maxlength="7"
            validation-message="Nhập đúng mã môn thi"
            pattern="(^(([A-Z]|[a-z]){3})([1-9][(0-9)]{3}))"
            placeholder="Nhập mã môn thi"
            required
          >
          </b-input>
        </b-field>
        <b-field label="Tên môn thi">
          <b-input
            type="text"
            v-model="newSubjectTitle"
            :value="newSubjectTitle"
            pattern="^[a-zA-Z1-9_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀẾỂưăạảấầẩẫậắằẳẵặẹẻẽềếểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\-\s() ]+$"
            maxlength="100"
            validation-message="Nhập đúng tên môn thi"
            placeholder="Nhập tên môn thi"
            required
          >
          </b-input>
        </b-field>
      </section>

      <footer class="modal-card-foot">
          <button class="button" type="button" @click="$parent.close()">Bỏ qua</button>
          <button class="button is-primary" type="submit">Cập nhật</button>
      </footer>
    </div>
  </form>
</template>

<script>
    import axios from "axios";
    import {authHeader} from "../../../api/jwt_handling";

    export default {
        name: "subject_edit",
        props: ['currentSubjectID','currentSubjectTitle'],
        data() {
          return {
            newSubjectID: this.currentSubjectID,
            newSubjectTitle: this.currentSubjectTitle
          }
        },
        methods: {
          async updateSubjectData() {
            try {
              // console.log(moment(this.newDob).format('MM/DD/YYYY'));
              const update = await axios({
                method: 'put',
                url: '/subject/edit-subject',
                headers: {
                  'Authorization': authHeader(),
                },
                data: {
                  currentSubjectID: this.currentSubjectID,
                  SubjectID: this.newSubjectID,
                  SubjectTitle: this.newSubjectTitle,
                },
              });
              if (update.status === 200) {
                this.$emit('loadSubjects', 200);
                this.$parent.close();
              }
              else if (update.status === 202) {
                this.$emit('loadSubjects', 202);
              }
            } catch (e) {
              if (e['message'].includes('400')) {
                this.$emit('loadSubjects', 400);
              } else if (e['message'].includes('401')) {
                this.$emit('loadSubjects', 401);
              }
            }
          }
        }
    }
</script>
