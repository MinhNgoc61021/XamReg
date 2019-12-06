<template>
  <form action="">
    <div class="modal-card" style="width: auto">
      <header class="modal-card-head">
        <p class="modal-card-title">Thêm môn thi</p>
      </header>
      <section class="modal-card-body">
        <b-field label="Mã môn thi">
          <b-input
            :value="data.subject_code"
            placeholder="Mã môn thi"
            required>
          </b-input>
        </b-field>

        <b-field label="Tên môn học">
          <b-input
            :value="data.subject_name"
            placeholder="Tên môn học"
            required>
          </b-input>
        </b-field>

      </section>
      <footer class="modal-card-foot">
        <button class="button" type="button" @click="$parent.close()">Cancel</button>
        <button class="button is-primary" @click="addOn()">Create</button>
      </footer>
    </div>
  </form>
</template>

<script>
    export default {
        name: "ModalAddForm",
        props:data,
        methods:{
            addOn(){

            }
        }
    }
</script>

<style scoped>

</style>
