document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menu-toggle");
    const mobileMenu = document.getElementById("mobile-menu");

    menuToggle.addEventListener("click", function () {
        mobileMenu.classList.toggle("hidden");
    });
});
// In this code, we have a responsive navbar with navigation links aligned to the left and login/sign-up buttons aligned to the right. The mobile menu is initially hidden and is toggled when the "menu-toggle" button is clicked.

// Make sure to include Tailwind CSS by adding the CDN link in your HTML file's head section. You can further customize the styles to match your design preferences.





