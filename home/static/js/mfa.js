var inner_index = 0
var inner_forms = $('.inner_form')
var dots = $('.dot')

function change_inner_form () {
	for (i = 0; i < inner_forms.length; i++) {
		if (i == inner_index) {
			$(inner_forms[i]).fadeIn();
			$(inner_forms[i]).show();
		} else {
			$(inner_forms[i]).fadeOut();
			$(inner_forms[i]).hide();
		}
	}
}
change_inner_form()


function change_dots () {
	for (i = 0; i < dots.length; i++) {
		if (i <= inner_index) {
			$(dots[i]).animate({backgroundColor: 'blue'}, 'fast');
		} else {
			$(dots[i]).animate({backgroundColor: 'white'}, 'fast');
		}
	}
}

change_dots()


$('#back').css('visibility','hidden')
$('#submit').hide()

$('#back').click(function () {
	if (inner_index == 4) {$('#forward').show()}
	inner_index -= 1
	if (inner_index < 1) {
		$('#back').css('visibility','hidden')
	} else if (inner_index == 0) {
		return
	}
	$('#submit').hide()
	change_inner_form()
	change_dots()
})

$('#forward').click(function () {
	inner_index += 1
	if (inner_index >= 4) {
		$('#forward').hide()
		$('#submit').show()
	} else {
		$('#back').css('visibility','visible')
	}
	change_inner_form()
	change_dots()
})

