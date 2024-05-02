let input = document.querySelector(".file-input");
let to_hide = document.querySelector(".to-hide");
input.addEventListener('change', function(event) {
  if (event.target.files.length > 0) {
    to_hide.click()
  }
});
