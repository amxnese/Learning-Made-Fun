function hideMessage() {
  let msg = document.querySelector(".alert");
  setTimeout(() => {
    msg.style.opacity = "0";
  }, 1700);
  setTimeout(() => {
    msg.style.display = "none";
  }, 3000);
}

function closeMe() {
  console.log("hi");
  let msg = document.getElementById("errorMessage");
  msg.style.display = "none";
}
