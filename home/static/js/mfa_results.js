
var result_data = JSON.parse(document.getElementById('result_data').textContent);

var result_blocks = $('.result_dots');

for (var i = 0; i < result_blocks.length; i++) {
	var dots_row = $(result_blocks[i]).find('.result_dot');
	var score = result_data[i];
	if (score < 4) {
		var color = 'red';
	} else if (score < 8) {
		var color = 'yellow';
	} else {
		var color = 'SpringGreen'
	}
	for (var j = 0; j < score; j++) {
		$(dots_row[j]).css('background-color', color);
	}
}