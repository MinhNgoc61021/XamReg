/*Root component, which is the starting point from which all other components will be rendered*/
<template>
  <div id="app">
    <router-view/>
  </div>
</template>
<script>
    // import register_form from './components/register-form';
    // import sign_up_form from './components/sign-up-form';
    import Test from "./components/Test";

    export default {
        name: 'app',
        components: {
            Test
        }
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
