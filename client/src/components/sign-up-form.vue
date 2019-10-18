<template>
        <div id="sign-up-form">
            <h3>Sign Up</h3>
            <form method="POST" action="/create-account" enctype="multipart/form-data">
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
</template>

<script>
export default {
  name: 'sign_up_form',
};
</script>
