
var url = window.location.origin + "/api/mfa_team/"

$.get(url, {'code':team_code}, function(data) {
	$('#team_name').text(data.name)
	valid_team = true
})

