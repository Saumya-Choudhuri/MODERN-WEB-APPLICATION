document.addEventListener("DOMContentLoaded", function () {
    const signUpButton = document.querySelector(".signup button");
    const emailInput = document.querySelector(".signup input");
    
    signUpButton.addEventListener("click", function () {
        const email = emailInput.value.trim();
        if (email === "") {
            alert("Please enter a valid email address.");
        } else {
            alert("Thank you for signing up, " + email + "!");
            emailInput.value = "";
        }
    });
});

function signup() {
    const email = document.getElementById("email").value;
    if (email) {
        alert("Signup successful for: " + email);
    } else {
        alert("Please enter a valid email.");
    }
}

function selectFeature(element, featureName) {
    document.querySelectorAll(".feature").forEach(feature => feature.classList.remove("selected"));
    element.classList.add("selected");
    alert("Feature selected: " + featureName);
}

function redirectToSignup() {
    window.location.href = "signup.html"; // Change this to match your actual signup page path
}
