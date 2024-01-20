function showProfileDropDown() {
    var dropdown = document.getElementById("profile-dropdown-content");
    if (dropdown.style.opacity == 0) {
      dropdown.style.transform = "scale(1)";
      dropdown.style.opacity = 1;
      
      document.getElementById("profile-dropbutton").classList.add("dropbtn-active")
    } else {
      dropdown.style.transform = "scale(0)";
      dropdown.style.opacity = 0;
      
      document.getElementById("profile-dropbutton").classList.remove("dropbtn-active")
    }
  }