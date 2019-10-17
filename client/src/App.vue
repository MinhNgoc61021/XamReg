/*Root component, which is the starting point from which all other components will be rendered*/
<template>
  <div id="app">
<!--    <router-view/>-->
<!--    <register_form msg="Opening register form for user"></register_form>-->
<!--    <sign_up_form></sign_up_form>-->
    <Test></Test>
  </div>
</template>
<script>
    import register_form from './components/register-form';
    import sign_up_form from './components/sign-up-form';
    import Test from "./components/Test";

    export default {
        name: 'app',
        components: {
            Test
        }
    }

//     window.onload = function () {
//         document.getElementById('sign-up-call-button').onclick = function() {
//             document.getElementById('sign-in-form').style.display = 'none';
//             document.getElementById('sign-up-form').style.display = 'block';
//         };
//
//         document.getElementById('callback-main-form-button').onclick = function (e) {
//                 document.getElementById('sign-in-form').style.display = 'block';
//                 document.getElementById('sign-up-form').style.display = 'none';
//         };
//
//         document.getElementById('callback-main-form-button-2').onclick = function () {
//             document.getElementById('sign-in-form').style.display = 'block';
//             document.getElementById('password-change-form').style.display = 'none';
//         };
//
//         document.getElementById('reset-password').onclick = function () {
//             document.getElementById('sign-in-form').style.display = 'none';
//             document.getElementById('password-change-form').style.display = 'block';
//         };
// };
</script>
<style>
  @import url('https://fonts.googleapis.com/css?family=Montserrat:400,700');

body {
  background-color: #EEEEEE;
  font-family: 'Montserrat', sans-serif;
  display: grid;
  grid-template-rows: auto;
  justify-items: center;
  align-items: center;
}
body, html {
  margin: 0;
  height: 100%;
}
#app {
    width: 50%;
}
</style>
