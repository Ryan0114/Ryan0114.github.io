var account = document.forms['form']['account'];
var password = document.forms['form']['password'];

var account_error = document.getElementById('account_error');
var pass_error = document.getElementById('pass_error');

account.addEventListener('textInput', account_Verify);
password.addEventListener('textInput', password_Verify);

function validated() {
    if (account.value.length < 9) {
        account.style.border = "1px solid red";
        account_error.style.display = "block";
        account.focus();
        return false;
    }
    if (password.value.length < 6) {
        password.style.border = "1px solid red";
        pass_error.style.display = "block";
        password.focus();
        return false;
    }
}

function account_Verify() {
    if (account.value.length >= 8) {
        account.style.border = "1px solid silver";
        account_error.style.display = "none";
    }
}
function password_Verify() {
    if (password.value.length >= 5) {
        password.style.border = "1px solid silver";
        pass_error.style.display = "none";
    }
}