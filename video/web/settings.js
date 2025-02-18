document.addEventListener('DOMContentLoaded', function () {
    const savedTheme = localStorage.getItem('theme');
    const settingsExitIcon = document.querySelector(".settings-exit");
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        updateExitIcon();
    }
});

document.querySelector(".settings-exit").addEventListener("click", function() {
    window.location.href = "index.html"; // Redirect to index page
});

function updateExitIcon() {
    if (document.body.classList.contains("dark-mode")) {
        settingsExitIcon.src = "./Images/darkX.png";
    } else {
        settingsExitIcon.src = "./Images/lightX.png";
    }
}