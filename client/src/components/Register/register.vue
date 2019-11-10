<template>
  <div id="container">
    <component v-bind:is="component"></component>
        <div id="sign-in-form">
            <h3 id="title">{{ msg }}, Please sign in</h3>
            <form v-on:submit.prevent="checkAuthentication()" enctype="multipart/form-data">
                    <label for="username-input">Username</label>
                        <input type="text" id="username-input" v-on:blur="showAlert = 'bounceOutUp'" v-on:keyup="onInputChange()" v-model="username" class="form-control" name="username" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
                    <br>
                    <label for="password-input">Password</label>
                        <input type="password" id="password-input" v-on:blur="showAlert = 'bounceOutUp'" v-on:keyup="onInputChange()" v-model="password" class="form-control" name="password" placeholder="Password" aria-label="Password" aria-describedby="basic-addon1">
                    <br>
                    <button type="submit" v-on:blur="showAlert = 'bounceOutUp'" v-on:click="warn($event)" @click="count++" style="display: inline-block;" class="save btn btn-outline-success">Sign In</button>

                    <button type="button" id="sign-up-call-button" class="save btn btn-outline-warning">About</button>
                    <br>
            </form>
        </div>
        <div class="alert animated " role="alert" id="password_warning" v-html="warning" style="text-align: center;" v-bind:class="[invalidSyntax, validSyntax, animateError, animateNotError, showAlert]">
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Test from "../Test.vue";
export default {
    name: 'register_form',
    data() {
      return {
          msg: 'Please',
          username: '',
          password: '',
          warning: '',
          invalidSyntax: '',
          animateError: '',
          animateNotError: '',
          validSyntax: '',
          count: 0,
          component: '',
          showAlert: '',
      };
    },
    methods: {
        warn: function(event) {
            console.log("Warning");
            this.showAlert = 'none';
            if (this.username.trim() === '' || this.password.trim() === '') {
                this.invalidSyntax = 'alert-danger';
                this.animateError ='bounceInDown';
                this.warning = 'Invalid, please type all your username | password.'
                event.preventDefault();
                if (this.count > 0) {
                    this.animateError = 'shake';
                }
            }
            console.log(this.count);

        },

        checkAuthentication: function() {
            const path = '/auth/register';
            axios.post(path, {
                  Username: this.username,
                  Password: this.password,
                })
                .then((response) => {
                    if (response.data === 'Proceed') {
                        this.$router.push('Test');
                    }
                    else {
                        this.showAlert = '';
                        this.warning = 'Account does not exist.';
                        this.invalidSyntax = 'alert-danger';
                        this.animateError ='bounceInDown';
                    }
                });
        },
        getMessage: function() {
            const path = '/test/hello_flask';
            axios.get(path)
                .then((response) => {
                    console.log(response.data);
                    this.msg = response.data;
                });
        },
        onInputChange: function() {
            this.showAlert = 'none';
            if (this.username.trim() === '' && this.password.trim() !== '') {
                this.warning = 'Please type your username.';
                this.invalidSyntax = 'alert-warning';
                this.animateError ='bounceInDown';
            }
            else if (this.password.trim() === '' && this.username.trim() !== '') {
                this.warning = 'Please type your password.';
                this.invalidSyntax = 'alert-warning';
                this.animateError ='bounceInDown';
            }
            else if (this.password.trim() === '' && this.username.trim() === '') {
                this.warning = 'Please type your username and password.';
                this.invalidSyntax = 'alert-warning';
                this.animateError ='bounceInDown';
            }
            else {
                this.animateError ='bounceInDown';
                this.invalidSyntax = 'alert-success';
                this.warning = 'All good!';
            }
        },
    },
    //
    // created() {
    //   this.getMessage();
    // },
};
</script>

<style src="../css/login_style.css">

</style>
