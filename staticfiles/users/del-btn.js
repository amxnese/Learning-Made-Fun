document.getElementById("deleteButton").addEventListener("click", function () {
  document.getElementById("modal").style.display = "block";
});

document.getElementById("confirm").addEventListener("click", function () {
  window.location.href = "delete/";
});

document.getElementById("cancel").addEventListener("click", function () {
  let msg = document.getElementById("modal");
  msg.style.display = "none";
});
