function hideMessage() {
  let msg = document.querySelector(".alert");
  setTimeout(() => {
    msg.style.opacity = '0';
  }, 2300);
  setTimeout(() => {
    msg.style.display = "none";
  }, 3000);
}
let closed = document.querySelector(".close-button");
closed.addEventListener("click", () => {
  let msg = document.querySelector(".alert");
  msg.style.display = "none";
});
