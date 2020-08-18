$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#nameInput').val(),
				email : $('#dateInput').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#').text(data.error).show();
			}
			else {
				$('#').text(data.name).show();
			}

		});

		event.preventDefault();

	});

});
