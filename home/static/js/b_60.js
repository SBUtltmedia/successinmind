
var playlist_1 = [
	'https://www.youtube.com/embed/jQzjBAsJ938',
	'https://www.youtube.com/embed/WkvKqqeV0cQ',
	'https://www.youtube.com/embed/rEX1NVl2DnU',
	'https://www.youtube.com/embed/e_u4clV9W6Y',
	'https://www.youtube.com/embed/oYTIXGsjYx8',
	'https://www.youtube.com/embed/hNsbgsP8SKM',
];
var playlist_1_index = 0;
var players_1 = $('#playlist_1 iframe')

//// Old function for when the player had a cool but unresponsive carrousel
// function manage_players_1 () {
// 	if (playlist_1_index == 0) {
// 		$(players_1[0]).fadeOut()
// 		$('#back_arrow_1').fadeOut()
// 	} else if (playlist_1_index == (playlist_1.length - 1)) {
// 		$(players_1.last()).fadeOut()
// 		$('#forward_arrow_1').fadeOut()
// 	} else {
// 		$(players_1[0]).fadeIn()
// 		$(players_1.last()).fadeIn()
// 		$('#back_arrow_1').fadeIn()
// 		$('#forward_arrow_1').fadeIn()
// 	}
// 	$(players_1[0]).attr('src', playlist_1[playlist_1_index - 1]);
// 	$(players_1[1]).attr('src', playlist_1[playlist_1_index]);
// 	$(players_1[2]).attr('src', playlist_1[playlist_1_index + 1]);
// }


function manage_players_1 () {
	if (playlist_1_index == 0) {
		$('#back_arrow_1').fadeOut()
	} else if (playlist_1_index == (playlist_1.length - 1)) {
		$('#forward_arrow_1').fadeOut()
	} else {
		$('#back_arrow_1').fadeIn()
		$('#forward_arrow_1').fadeIn()
	}
	$(players_1[0]).attr('src', playlist_1[playlist_1_index])
}



$('#back_arrow_1').click(function () {
	playlist_1_index--;
	manage_players_1()
})

$('#forward_arrow_1').click(function () {
	playlist_1_index++;
	manage_players_1()
})



var playlist_2 = [
	'https://www.youtube.com/embed/FBHTzWmAZjc',
	'https://www.youtube.com/embed/3tFpfQJeW2w',
	'https://www.youtube.com/embed/0nEGXirvs40',
	'https://www.youtube.com/embed/aZQWPbua0xQ',
	'https://www.youtube.com/embed/w2hKAvx3bHE',
];
var playlist_2_index = 0;
var players_2 = $('#playlist_2 iframe')

//// Old function for when the player had a cool but unresponsive carrousel
// function manage_players_2 () {
// 	if (playlist_2_index == 0) {
// 		$(players_2[0]).fadeOut()
// 		$('#back_arrow_2').fadeOut()
// 	} else if (playlist_2_index == (playlist_2.length - 1)) {
// 		$(players_2.last()).fadeOut()
// 		$('#forward_arrow_2').fadeOut()
// 	} else {
// 		$(players_2[0]).fadeIn()
// 		$(players_2.last()).fadeIn()
// 		$('#back_arrow_2').fadeIn()
// 		$('#forward_arrow_2').fadeIn()
// 	}
// 	$(players_2[0]).attr('src', playlist_2[playlist_2_index - 1]);
// 	$(players_2[1]).attr('src', playlist_2[playlist_2_index]);
// 	$(players_2[2]).attr('src', playlist_2[playlist_2_index + 1]);
// }


function manage_players_2 () {
	if (playlist_2_index == 0) {
		$('#back_arrow_2').fadeOut()
	} else if (playlist_2_index == (playlist_2.length - 1)) {
		$('#forward_arrow_2').fadeOut()
	} else {
		$('#back_arrow_2').fadeIn()
		$('#forward_arrow_2').fadeIn()
	}
	$(players_2[0]).attr('src', playlist_2[playlist_2_index])
}

$('#back_arrow_2').click(function () {
	playlist_2_index--;
	manage_players_2()
})

$('#forward_arrow_2').click(function () {
	playlist_2_index++;
	manage_players_2()
})



$('.arrow').hover(
	function() {$(this).css('color', 'red')},
	function() {$(this).css('color', '#990000')},
)


manage_players_1()
manage_players_2()