<template>
  <div id="container">
        <div id="sign-in-form">
            <h3 id="title">{{ msg }}, Please sign in</h3>
            <form method="POST" action="http://localhost:5000/authenticate" enctype="multipart/form-data">
                    <label for="username-input">Username</label>
                        <input type="text" id="username-input"  class="form-control" name="username" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
                    <br>
                    <label for="password-input">Password</label>
                        <input type="password" id="password-input" class="form-control" name="password" placeholder="Password" aria-label="Password" aria-describedby="basic-addon1">
                        <a id="reset-password" style="display:block; float: right; cursor: pointer;">Forgotten Password</a>
                    <br>
                    <button type="submit" style="display: inline-block" class="save btn btn-outline-success">Sign In</button>
                    <button type="button" id="sign-up-call-button" class="save btn btn-outline-warning">Sign Up</button>
                    <br>
            </form>
        </div>
        <div id="password-change-form">
            <h3>Change Password</h3>
            <form method="POST" action="http://localhost:5000/change-password" enctype="multipart/form-data">
                    <label for="username-input">Username</label>
                        <input type="text" id="password-username-input" class="form-control" name="username" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
                    <br>
                    <label for="newpassword-input">Password</label>
                        <input type="password" id="newpassword-input" class="form-control" name="new-password" placeholder="Password" aria-label="Password" aria-describedby="basic-addon1">
                        <br>
                    <label for="confirm-new-password-input">Retype Password</label>
                        <input type="password" id="confirm-new-password-input" class="form-control" name="confirm-password" placeholder="Retype Password" aria-label="Retype Password" aria-describedby="basic-addon1">
                    <br>
                    <button type="submit" style="display: inline-block" class="save btn btn-outline-success">Change Password</button>
                    <button type="button" id="callback-main-form-button-2" style="float: right;" class="save btn btn-outline-dark">Back</button>
                    <br>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'register_form',
    data() {
      return {
        msg: 'Not Yet',
      };
    },
    methods: {
        getMessage() {
            const path = 'http://localhost:5000/register-form';
            axios.get(path)
                .then((response) => {
                    console.log(response.data);
                    this.msg = response.data;
                });
        },
    },
    created() {
      this.getMessage();
    },
};
</script>

<style src="./css/login_style.css"></style>
