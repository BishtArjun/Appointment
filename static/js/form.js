$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : JSON.stringify({
				name : $('#name').val(),  // this should be id of the field you want, #name refers to element with id `name`
				date : $('#date').val()
			}),
			type : 'POST',
      url : 'process',
      contentType : 'application/json'
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
