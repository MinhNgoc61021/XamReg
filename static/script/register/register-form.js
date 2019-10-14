$(document).ready(function () {
    $('#sign-up-form').hide();
    $('#password-change-form').hide();


    $('#sign-up-call-button').click(function () {
        $('#sign-in-form').fadeOut(500);
        $('#sign-up-form').fadeIn(500);
    });

    $('#callback-main-form-button').click(function () {
        $('#sign-up-form').fadeOut(500);
        $('#sign-in-form').fadeIn(500);
    });

    $('#callback-main-form-button-2').click(function () {
        $('#password-change-form').fadeOut(500);
        $('#sign-in-form').fadeIn(500);
    });

    $('#reset-password').click(function () {
        $('#sign-in-form').fadeOut(500);
        $('#password-change-form').fadeIn(500);
    });


});