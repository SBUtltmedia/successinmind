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
			$(dots[i]).animate({backgroundColor: '#990000'}, 'fast');
		} else {
			$(dots[i]).animate({backgroundColor: 'white'}, 'fast');
		}
	}
}

change_dots()



function check_inputs (display=true) {
	var rows = $(inner_forms[inner_index]).find('tr')
	for (i = 0; i < rows.length; i += 2) {
		var inputs = $(rows[i]).find('input')
		var checked = false
		for (j = 0; j < inputs.length; j++) {
			if($(inputs[j]).is(':checked')) {
				checked = true
				break
			}
		}
		if (!(checked)) {
			if (display) {
				$('#error_block p').text('Please provide an input for each question!')
			}
			return false
		}
	}
	return true
}


function check_all_inputs () {
	if (inner_index != (inner_forms.length - 1)) {return}
	var rows = $('.inner_form tr')
	for (i = 0; i < rows.length; i += 2) {
		var inputs = $(rows[i]).find('input')
		var checked = false
		for (j = 0; j < inputs.length; j++) {
			if(($(inputs[j]).is(':checked'))) {
				checked = true
				break
			}
		} 
		if (!(checked)) {
			return false
		}
	}
	var selects = $('select')
	for (i = 0; i < selects.length; i++) {
		if (selects[i].value == '') {
			return false
		}
	}
	$('#submit').css('visibility','visible')
	return true
}



$('#back').css('visibility','hidden')
$('#submit').hide()

$('#back').click(function () {
	if (inner_index == 5) {$('#forward').show()}
	inner_index -= 1
	$('#error_block p').text('')
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
	if (check_inputs()) {
		$('#error_block p').text('')
		inner_index += 1
		if (inner_index >= 5) {
			$('#forward').hide()
			if (!(check_all_inputs())) {
				$('#submit').css('visibility','hidden')
				$('#submit').show()
			} else {
				$('#submit').show()
				$('#submit').css('visibility','visible')
			}
		} else {
			$('#back').css('visibility','visible')
		}
		change_inner_form()
		change_dots()
	}
})


$('.inner_form select').change(check_all_inputs)
