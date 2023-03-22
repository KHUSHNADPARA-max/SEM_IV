const menu = document.getElementById("menu");
menu.addEventListener("click", function (event) {
  // Check if the clicked element is a menu header
  if (event.target.classList.contains("menu-header")) {
    // Collapse all the other menu items
    const menuItems = menu.getElementsByClassName("menu-item");
    for (const menuItem of menuItems) {
      if (menuItem !== event.target.parentNode) {
        menuItem.classList.remove("expanded");
      }
    }
    // Expand the clicked menu item
    event.target.parentNode.classList.toggle("expanded");
  }
});
