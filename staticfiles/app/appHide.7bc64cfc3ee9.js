function hideMessage() {
  let msg = document.querySelector(".alert");
  setTimeout(() => {
    msg.style.opacity = "0";
  }, 4300);
  setTimeout(() => {
    msg.style.display = "none";
  }, 5000);
}

function dissmis() {
    let msg = document.getElementById("dissmis");
    msg.style.display = "none";
}

function closeMe() {
  let msg = document.getElementById("errorMessage");
  msg.style.display = "none";
}
