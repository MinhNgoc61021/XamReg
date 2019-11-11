<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
  import axios from 'axios';
  export default {
      name: 'App',
      created: function () {
          const path = '/auth/';
          axios.get(path)
              .then(function (response) {
                  if (response.data) {
                      console.log(response.data);
                  }
              })

      },
  }
</script>

<style src="./components/css/animate.css">
  @import url('https://fonts.googleapis.com/css?family=Montserrat:400,700');
  body, html {
  margin: 0;
  height: 100%;
}
#app {
}
</style>
