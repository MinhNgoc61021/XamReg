<template>
  <div id="container">
        <div id="sign-in-form">
            <h3 id="title" >{{ msg }}, Please sign in</h3>
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
        <div id="sign-up-form">
            <h3>Sign Up</h3>
            <form method="POST" action="http://localhost:5000/create-account" enctype="multipart/form-data">
                    <label for="new-email-input">Email</label>
                        <input type="email" id="new-email-input" class="form-control" name="new-email-input" placeholder="Email" aria-label="Email" aria-describedby="basic-addon1">
                    <br>
                    <label for="new-username-input">Username</label>
                        <input type="text" id="new-username-input" class="form-control" name="new-username-input" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
                    <br>
                    <label for="new-fullname-input">Fullname</label>
                        <input type="text" id="new-fullname-input" class="form-control" name="new-fullname-input" placeholder="Fullname" aria-label="Fullname" aria-describedby="basic-addon1">
                    <br>
                    <label for="new-password-input">Password</label>
                        <input type="password" id="new-password-input" class="form-control" name="new-password-input" placeholder="Password" aria-label="Password" aria-describedby="basic-addon1">
                    <br>
                    <label for="confirm-password-input">Retype Password</label>
                        <input type="password" id="confirm-password-input" class="form-control" name="confirm-password-input" placeholder="Retype Password" aria-label="Retype Password" aria-describedby="basic-addon1">
                    <br>
                    <button type="submit" style="display: inline-block" id="sign-up-button" class="save btn btn-outline-success">Sign Up</button>
                    <button type="button" style="display: inline-block; float: right;" id="callback-main-form-button" class="save btn btn-outline-dark">Back</button>
                <br>
            </form>
        </div>
        <div id="password-change-form">
            <h3>Change Password</h3>
            <form method="POST" action="/change-password" enctype="multipart/form-data">
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
window.onload = function () {
    document.getElementById('sign-up-call-button').onclick = function() {
        document.getElementById('sign-in-form').style.display = 'none';
        document.getElementById('sign-up-form').style.display = 'block';
    };

    document.getElementById('callback-main-form-button').onclick = function () {
        document.getElementById('sign-in-form').style.display = 'block';
        document.getElementById('sign-up-form').style.display = 'none';
    }
};

export default {
  name: 'register_form',
  data() {
    return {
      msg: '',
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

<style scoped>
  #container {
    height: 100vh;
    position: relative;
  }
  #sign-in-form, #sign-up-form, #password-change-form {
    border-radius: 4px;
    border: 1px rgba(73, 80, 87, 0.30196078431372547) solid;
    position: absolute;
    top: 50%;
    right: 50%;
    min-width: 450px;
    min-height: 300px;
    padding: 50px;
    transform: translate(50%,-50%);
    -moz-transform: translate(50%,-50%);
    -webkit-transform: translate(50%,-50%);
    -o-transform: translate(50%,-50%);
    -ms-transform: translate(50%,-50%);
    /*-webkit-transition: width 2s, height 2s; !* Safari prior 6.1 *!*/
    /*transition: width 2s, height 2s;*/
    /*transition-timing-function: linear;*/
  }

  #sign-up-form, #password-change-form {
    display: none;
  }

  label {
    display: inline;
    max-width: 150px;
    float: left;
  }

  #container input {
      margin-top: 10px;
  }

#container button {
    margin-top: 10px;
}

  #container a {
      outline: none;
      text-decoration: none;
      color:#E45953;
  }

  #sign-up-call-button {
      display: inline-block;
      float: right;
  }

  @media only screen and (max-width: 500px) {
      #sign-in-form, #sign-up-form {
          margin: 0;
          min-width: 300px;
          font-size: 12px;
      }
  }

  @media only screen and (max-height: 700px) {
      #container {
          min-height: 700px;
      }
  }
</style>
