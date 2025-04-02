document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let emailError = document.getElementById("emailError");
    let passwordError = document.getElementById("passwordError");

    emailError.textContent = "";
    passwordError.textContent = "";

    if (!email) {
        emailError.textContent = "Email required!";
    } else if (!email.includes("@")) {
        emailError.textContent = "Invalid email!";
    }

    if (!password) {
        passwordError.textContent = "Password required!";
    }
});

document.getElementById("togglePassword").addEventListener("click", function() {
    let passwordField = document.getElementById("password");
    passwordField.type = passwordField.type === "password" ? "text" : "password";
});
