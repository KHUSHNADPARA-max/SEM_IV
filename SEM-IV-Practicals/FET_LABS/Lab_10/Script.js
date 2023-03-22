function validateForm() {
  var name = document.forms["register-form"]["name"].value;
  var email = document.forms["register-form"]["email"].value;
  var mobile = document.forms["register-form"]["mobile"].value;
  var password = document.forms["register-form"]["password"].value;
  var confirmPassword = document.forms["register-form"]["confirm-password"].value;

  if (name == "") {
    return false;
  }

  if (email == "") {
    return false;
  }

  if (mobile == "") {
    return false;
  }

  if (password == "") {
    return false;
  }

  if (confirmPassword == "") {
    return false;
  }

  if (password != confirmPassword) {
    return false;
  }

  return true;
}
