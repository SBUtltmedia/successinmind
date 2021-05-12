var white = 'rgb(255, 255, 255)'


var player1_name = prompt('Player 1\nEnter your name')
if (player1_name === null) {player1_name = "Player 1"};

var player2_name = prompt('Player 2\nEnter your name')
if (player2_name === null) {player2_name = "Player 2"};


var turn = true // True means player 1; False means player 2

var $status = $('#status');

$("#col1").hover(show_hidden, hide_hidden);
$("#col1").click(find_lowest_empty);

$("#col2").hover(show_hidden, hide_hidden);
$("#col2").click(find_lowest_empty);

$("#col3").hover(show_hidden, hide_hidden);
$("#col3").click(find_lowest_empty);

$("#col4").hover(show_hidden, hide_hidden);
$("#col4").click(find_lowest_empty);

$("#col5").hover(show_hidden, hide_hidden);
$("#col5").click(find_lowest_empty);

$("#col6").hover(show_hidden, hide_hidden);
$("#col6").click(find_lowest_empty);

$("#col7").hover(show_hidden, hide_hidden);
$("#col7").click(find_lowest_empty);


function win() {
	if (turn) {
		alert(player2_name + " has won.");
	} else {
		alert(player1_name + " has won.");
	}
}


function get_player_color() {
	if (turn) {
		var color = 'blue'
	} else {
		var color = 'red'
	}
	return color
}

function show_hidden() {
	$(this).find('.hover').css('background-color', get_player_color())
	$(this).find('.hover').css('border-color', 'black')
}

function hide_hidden() {
	$(this).find('.hover').css('background-color', 'white')
	$(this).find('.hover').css('border-color', 'white')
}



function display_player() {
	var text = ": It is your turn. Pick a column."
	if (turn) {
		$status.text(player1_name + text)
	} else {
		$status.text(player2_name + text)
	}
}


function find_lowest_empty() {
	var dots = $(this).find(".dot:not(.hover)");
	for (var i = dots.length - 1; i >= 0; i--) {
		var color = $(dots[i]).css('background-color');
		if (color === white) {
			$(dots[i]).css('background-color', get_player_color());
			turn = !turn
			display_player()
			$(this).find('.hover').css('background-color', get_player_color())
			if (check_win()) {
				win()
			}
			break
		}
	}
}


/*
2 - Down
4 - Left
3 - Diag-Up-Right
9 - Diag-Down-Right
*/

function crawl(direction, color, index, count) {
	var dots = $(".dot:not(.hover)")
	if (direction == 2) {
		var change = 1;
	} else if (direction == 4) {
		var change = -5
	} else if (direction == 3) {
		if ([0, 1, 2, 5, 6, 10, 34, 33, 32, 29, 28, 24].includes(index)) {return false};
		var change = 4
	} else if (direction == 9) {
		if ([2, 3, 4, 8, 9, 14, 20, 25, 26, 30, 31, 32].includes(index)) {return false};
		var change = 6
	} 

	if (change+index < 0 || change+index > dots.length) {
		return false;
	} else {
		var dot_color = $(dots[change+index]).css('background-color')
		if (dot_color === color) {
			count += 1
			if (count >= 4) {
				console.log(direction, color, change+index, count)
				return true
			} else {
				return crawl(direction, color, change+index, count)
			}
		} else {
			return false
		}
	}
}


function check_win() {
	var dots = $(".dot:not(.hover)")
	for (var i = 0; i < dots.length; i++) {
		var color = $(dots[i]).css('background-color')
		if (color != white) {
			for (direction of [2, 4, 3, 9]) {
				if (crawl(direction, color, i, 1)) {
					return true
				}
			}
		}
	}
	return false
}



display_player()