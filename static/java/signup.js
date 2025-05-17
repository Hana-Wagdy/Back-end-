document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("signupForm");

    // Client-side validation only
    form.addEventListener("submit", function (e) {
        const password = form.querySelector('input[name="password"]').value;
        const confirmPassword = form.querySelector('input[name="confirm_password"]').value;

        if (password.length < 6) {
            alert("Password should be at least 6 characters");
            e.preventDefault();
            return;
        }
        if (password !== confirmPassword) {
            alert("Passwords do not match!");
            e.preventDefault();
            return;
        }
    });
});

function updateProfileLink(role) {
    const profileLink = document.getElementById('profile-link');
    if (role === 'admin') {
        profileLink.href = 'AdminPage.html';
    } else {
        profileLink.href = 'userprofile.html';
    }
}

function checkLogin() {
    const user = JSON.parse(localStorage.getItem('loggedInUser'));
    if (user) {
        updateProfileLink(user.role);
    }
}