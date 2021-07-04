
var url = window.location.origin + "/api/mfa_team/"
var valid_team = false

function get_name() {
	var code = document.getElementById('team_token').value
	if (code.length == 6) {
		$.get(url, {'code':code}, function(data) {
			$('#team_name').text(data.name)
			valid_team = true
		})
	} else {
		$('#team_name').text('')
		valid_team = false
	}
}

$('#team_token').on('input', get_name)


$('#submit').click(function() {
	if (valid_team) {
		document.getElementById("team_form").submit();
	} else {
		$('#status_message').text('Please enter a valid 6 character code')
	}
})