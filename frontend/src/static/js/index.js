var exampleModal = document.getElementById("exampleModalCenter");

exampleModal.addEventListener("show.bs.modal", function (event) {
  var first_name = exampleModal.querySelector("#first_name");
  var last_name = exampleModal.querySelector("#last_name");
  var form = exampleModal.querySelector("#formId");

  var button = event.relatedTarget;
  if (button.id == "btnCreate") {
    first_name.value = "";
    last_name.value = "";
    form.action = "/add";
    return;
  }
  var elems = button.parentElement.parentElement.getElementsByTagName("td");
  first_name.value = elems[1].textContent;
  last_name.value = elems[2].textContent;
  form.action = "/update/" + elems[0].textContent;
});
