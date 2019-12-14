<template>
    <button @click.prevent="exportPDF()"></button>
</template>

<script>
    export default {
        name: "export_pdf",
        data(){
          return{
              list: [],
              one_object:{
                "shift": "",
                "student_name": "",
                "student_dob": "",
                "student_gender": "",
              },
              text:{
                "header": "", //ten ca thi
                "room_name": "",
                "subject": "",
                "date": ""
              }
          }
        },
        methods:{
            async getData(){

            },
            exportPDF(){

            }
        }
    }
</script>

<style scoped>

</style>
