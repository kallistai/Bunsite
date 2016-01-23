$(document).ready(function(){
	
	$("#addPlayer").click(function() {
		var playerName = $("#player").val();
		$("#players").append("<tr><td>" + playerName + "</td><td><input type='text' name='Commander' id='deck'></td><td><input type='button' value='Remove' class='removePlayer'></td></tr>");
		$("#player").val('');
	});
	
	$('#players').on('click', '.removePlayer', function(){
   		$(this).closest('tr').remove();
	});
});