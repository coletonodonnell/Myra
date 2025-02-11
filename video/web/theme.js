function toggleTheme() {
    document.body.classList.toggle("dark-mode");
    const logo = document.getElementById("theme-logo");

    // Save the user's theme preference in localStorage
    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("theme", "dark");
        logo.src = "./Images/MyraDark.png";
    } else {
        localStorage.setItem("theme", "light");
        logo.src = "./Images/MyraLight.png";
    }
}

// On page load, check for the stored theme and apply it
window.onload = function () {
    const logo = document.getElementById("theme-logo");

    // Check the theme stored in localStorage
    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-mode");
        logo.src = "./Images/MyraDark.png";
    }
    else{
        logo.src = "./Images/MyraLight.png";

    }

    // Add event listener to the toggle button
    const themeToggleButton = document.getElementById("theme-toggle-btn");
    if (themeToggleButton) {
        themeToggleButton.addEventListener("click", toggleTheme);
    }
};
