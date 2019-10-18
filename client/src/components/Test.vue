This component is only for studying purpose only
<template>
  <div class="container">
    <div class="holder">
<!--        <h1 v-once>{{ name }}</h1>-->
<!--        <button v-on:click="changeName" class="btn btn-dark" v-bind:aria-disabled="btnstate">Change Name</button>-->
      <form @submit.prevent="addInfo">
        <input type="text" placeholder="Type info here..." v-model="infomation" v-validate="':min5'" name="infomation">
        <p class="alert" v-if="errors.has('infomation')" >{{ errors.first('infomation') }}</p>
      </form>

      <ul>
        <li v-for="(data, index) in array" :key="index"> {{ index }}. {{ data.infomation }} </li>
      </ul>
      <p>Learning Vue JS</p>
    </div>
  </div>
</template>

<script>
    export default {
        name: "Test",
        data() {
            return {
                name: 'Minhngoc61021',
                array: [
                    { 'infomation' : 'Nguyễn Ngọc Minh' },
                    { 'infomation' : 'Minh' }
                ],
            }
        },
        methods: {
            addInfo() {
                this.array.push({infomation: this.infomation});
                this.infomation = '';
            },
        }
    }
</script>

<style scoped>
  .holder {
    background: #fff;
  }

  ul {
    margin: 0;
    padding: 0;
    list-style-type: none;
  }

  ul li {
    padding: 20px;
    font-size: 1.3em;
    background-color: #E0EDF4;
    border-left: 5px solid #3EB3F6;
    margin-bottom: 2px;
    color: #3E5252;
  }

  p {
    text-align:center;
    padding: 30px 0;
    color: gray;
  }

  .container {
    box-shadow: 0px 0px 40px lightgray;
  }

  input {
    width: calc(100% - 40px);
    border: 0;
    padding: 20px;
    font-size: 1.3em;
    background-color: #323333;
    color: #687F7F;
  }
</style>
