$(document).ready(function() {
	$("#radio-button-container input:radio").click(function() {
		$("input:radio:checked").prop('checked', false);
		$(this).prop('checked', true);
	})
})