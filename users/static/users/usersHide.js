function hideMessage() {
  let msg = document.querySelector(".alert");
  setTimeout(() => {
    msg.style.opacity = "0";
  }, 2000);
  setTimeout(() => {
    msg.style.display = "none";
  }, 3300);
}

function closeMe() {
  let msg = document.getElementById("errorMessage");
  msg.style.display = "none";
}
