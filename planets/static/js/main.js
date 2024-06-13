function toggle(value) {
	var btnSubmit = document.getElementById("btnSearch");

	var isEmpty = value.value.trim() == ""
	btnSubmit.disabled = isEmpty;
};

function blockSearch() {
	document.getElementById("btnSearch").disabled = true;
};