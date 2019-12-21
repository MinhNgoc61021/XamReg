<template>
  <form @submit.prevent="createSubject()">
    <div class="modal-card" style="width: 450px;">
        <header class="modal-card-head">
            <p class="modal-card-title">Form tạo môn học</p>
        </header>

      <section class="modal-card-body">
        <b-field label="Mã môn học">
          <b-input
            type="text"
            v-model="newSubjectID"
            :value="newSubjectID"
            maxlength="7"
            validation-message="Nhập đúng mã môn học"
            pattern="(^(([A-Z]|[a-z]){3})([1-9][(0-9)]{3}))"
            placeholder="Nhập mã môn học"
            required
          >
          </b-input>
        </b-field>
        <b-field label="Tên môn học">
          <b-input
            type="text"
            v-model="newSubjectTitle"
            :value="newSubjectTitle"
            pattern="^[a-zA-Z1-9_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀẾỂưăạảấầẩẫậắằẳẵặẹẻẽềếểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\-\s() ]+$"
            maxlength="100"
            validation-message="Nhập đúng tên môn học"
            placeholder="Nhập tên môn học"
            required
          >
          </b-input>
        </b-field>

      </section>
    </div>
    <footer class="modal-card-foot">
          <button class="button" type="button" @click="$parent.close()">Bỏ qua</button>
          <button class="button is-primary" type="submit">Tạo</button>
      </footer>
  </form>
</template>

<script>
    import axios from "axios";
    import {authHeader} from "../../../api/jwt_handling";

    export default {
        name: "subject_create",
        data() {
          return {
            newSubjectID: '',
            newSubjectTitle: ''
          }
        },
        methods: {
          async createSubject() {
            try {
              console.log( this.newSubjectID);
              console.log(this.newSubjectTitle);
              const update = await axios({
                method: 'post',
                url: '/subject/create-subject',
                headers: {
                  'Authorization': authHeader(),
                },
                data: {
                  SubjectID: this.newSubjectID,
                  SubjectTitle: this.newSubjectTitle,
                },
              });
              if (update.status === 200) {
                this.$emit('loadSubjects', 200);
                this.$parent.close();
              }
              else {
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

<style scoped>
</style>
