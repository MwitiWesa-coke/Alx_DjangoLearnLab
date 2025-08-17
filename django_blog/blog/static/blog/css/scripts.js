// blog/static/blog/js/scripts.js

document.addEventListener("DOMContentLoaded", () => {
  console.log("Blog auth scripts loaded ✅");
  // Example: add a subtle style when any form is submitted
  const forms = document.querySelectorAll("form");
  forms.forEach(form => {
    form.addEventListener("submit", () => {
      alert("Form submitted!");
    });
  });
});
