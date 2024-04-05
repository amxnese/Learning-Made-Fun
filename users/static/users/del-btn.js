document.getElementById("deleteButton").addEventListener("click", function () {
  document.getElementById("confirmationModal").style.display = "block";
});

document.getElementById("closeButton").addEventListener("click", function () {
  document.getElementById("confirmationModal").style.display = "none";
});

document.getElementById("confirmDelete").addEventListener("click", function () {
  window.location.href = "delete/";
});
