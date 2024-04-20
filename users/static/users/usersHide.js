function hideMessage() {
  let msg = document.querySelector(".alert");
  setTimeout(() => {
    msg.style.opacity = '0';
  }, 1700);
  setTimeout(() => {
    msg.style.display = "none";
  }, 4000);
}
