
// left: 37, up: 38, right: 39, down: 40,
// spacebar: 32, pageup: 33, pagedown: 34, end: 35, home: 36
var keys = { 37: 1, 38: 1, 39: 1, 40: 1 };

function preventDefault(e) {
	e.preventDefault();
}

function preventDefaultForScrollKeys(e) {
	if (keys[e.keyCode]) {
		preventDefault(e);
		return false;
	}
}

// modern Chrome requires { passive: false } when adding event
var supportsPassive = false;
try {
	window.addEventListener("test", null, Object.defineProperty({}, 'passive', {
		get: function () { supportsPassive = true; }
	}));
} catch (e) { }

var wheelOpt = supportsPassive ? { passive: false } : false;
var wheelEvent = 'onwheel' in document.createElement('div') ? 'wheel' : 'mousewheel';


function disableScroll() {
	window.addEventListener('DOMMouseScroll', preventDefault, false); // older FF
	window.addEventListener(wheelEvent, preventDefault, wheelOpt); // modern desktop
	window.addEventListener('touchmove', preventDefault, wheelOpt); // mobile
	window.addEventListener('keydown', preventDefaultForScrollKeys, false);
}


function enableScroll() {
	window.removeEventListener('DOMMouseScroll', preventDefault, false);
	window.removeEventListener(wheelEvent, preventDefault, wheelOpt);
	window.removeEventListener('touchmove', preventDefault, wheelOpt);
	window.removeEventListener('keydown', preventDefaultForScrollKeys, false);
}


$('#create_team').click(function () {
	disableScroll()
	$('#team_creator').css('visibility', 'visible')
})

$('#close_team').click(function() {
	enableScroll()
	$('#team_creator').css('visibility','hidden')
})

var url = window.location.origin + "/api/mfa_team/"

function getCode() {
	$.get(url, function(data) {$('#team_token').val(data.code)})
}

getCode()

$('#refresh_button').click(getCode)


$('#copy').hover(function () {
		$(this).css('color', 'red')
	}, function () {
		$(this).css('color', 'black')
	}
)

$('#copy').click(function () {
	var copyText = document.getElementById('team_token')
	copyText.select();
	copyText.setSelectionRange(0, 99999)
	document.execCommand("copy");

	var status_message = document.getElementById('status_message')
	status_message.innerHTML = 'Code copied to clipboard'
	status_message.style.color = "green";
})


$('#submit').click( function () {
	if (document.getElementById('team_name').value != '') {
		document.getElementById("team_form").submit();
	} else {
		var status_message = document.getElementById('status_message')
		status_message.innerHTML = 'Please give the Team a name'
		status_message.style.color = "red";
	}
})