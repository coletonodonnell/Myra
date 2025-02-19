
  function toggleMenu() {
    const menu = document.querySelector(".menu");
    const overlay = document.querySelector(".overlay");
    const menuButton = document.querySelector(".menu-icon");
    const settingsButton = document.querySelector(".settings-icon");


    if (menu.classList.contains("show")) {
        menu.classList.remove("show");
        overlay.style.display = "none";
        menuButton.style.display = "block"; 
        settingsButton.style.display = "block"; // show settings and menu buttons when menu is closed
    } else {
        menu.classList.add("show");
        overlay.style.display = "block";
        menuButton.style.display = "none"; // hide buttons when menu is open
        settingsButton.style.display = "none";

    }
}

  
  // On page load, check for the stored theme and apply it
  window.onload = function () {
    if (localStorage.getItem("theme") === "dark") {
      document.body.classList.add("dark-mode");
    }
  };
  
// search functionality
// add event listener for enter button as well?
  document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("search-btn").addEventListener("click", function () {
        let query = document.getElementById("search").value.trim();

        if (query !== "") {  // Make sure it's not empty
            console.log("Sending query:", query); 
            eel.Receive_Query_From_GUI(query);  // Send query to Python
        }
    });
});


