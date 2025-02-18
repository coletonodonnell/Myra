document.addEventListener('DOMContentLoaded', function () {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
    }
});

document.querySelector(".settings-exit").addEventListener("click", function() {
    window.location.href = "index.html"; // Redirect to index page
});

