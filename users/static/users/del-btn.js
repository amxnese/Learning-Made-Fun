document.getElementById("deleteButton").addEventListener("click", function () {
  document.getElementById("confirmationModal").style.display = "block";
});

document.getElementById("closeButton").addEventListener("click", function () {
  document.getElementById("confirmationModal").style.display = "none";
});

document.getElementById("confirmDelete").addEventListener("click", function () {
  window.location.href = "delete/";
});

function change_color(){
  document.getElementById("confirmDelete").style.backgroundColor = "#ff4d4f"
}
