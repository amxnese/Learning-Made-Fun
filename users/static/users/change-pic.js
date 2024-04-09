let icon = document.querySelector(".icon");
icon.addEventListener("click", () => {
  document.querySelector(".file-input").click();
});
document.querySelector('.file-input').addEventListener('change', function(event) {
  if (event.target.files.length > 0) {
    document.querySelector(".to-hide").click()
  }
});
