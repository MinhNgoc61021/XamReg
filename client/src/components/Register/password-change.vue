<template>
    <div id="password-change-form">
            <h3>Change Password</h3>
            <form method="POST" action="http://localhost:5000/change-password" enctype="multipart/form-data">
                    <label for="username-input">Username</label>
                        <input type="text" id="username-input" class="form-control" name="username" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
                    <br>
                    <label for="password-input">Password</label>
                        <input type="password" id="password-input" class="form-control" name="new-password" placeholder="Password" aria-label="Password" aria-describedby="basic-addon1">
                        <br>
                    <label for="confirm-new-password-input">Retype Password</label>
                        <input type="password" id="confirm-new-password-input" class="form-control" name="confirm-password" placeholder="Retype Password" aria-label="Retype Password" aria-describedby="basic-addon1">
                    <br>
                    <button type="submit" style="display: inline-block" class="save btn btn-outline-success">Change Password</button>
                    <button type="button" id="callback-main-form-button-2" style="float: right;" class="save btn btn-outline-dark">Back</button>
                    <br>
            </form>
        </div>
</template>

<script>
    export default {
        name: "password-change"
    }
</script>

<style src="../css/login_style.css">


</style>
