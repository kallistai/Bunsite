$(document).ready(function(){
	
	$("#addPlayer").click(function() {
		var playerName = $("#player").val();
		var commanderName = $("#commander").val();
		$("#players").append("<tr><td>" + playerName + "</td><td>" + commanderName + "</td><td><input type='button' value='Remove' class='removePlayer'></td></tr>");
		$("#player").val('');
		$("#commander").val('');
	});
	
	$('#players').on('click', '.removePlayer', function(){
   		$(this).closest('tr').remove();
	});

	$('#gameStart').click(function(){
		var myTableArray = [];

$("table#players tr").each(function() {
    var arrayOfThisRow = [];
    var tableData = $(this).find('td');
    if (tableData.length > 0) {
        tableData.each(function() { arrayOfThisRow.push($(this).text()); });
        myTableArray.push(arrayOfThisRow);
    }
});

alert(myTableArray);
		window.location.href = "gametracker.html";
	});
});