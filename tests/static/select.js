//$(document).ready(function($){ 
//$("#my_select").empty();

	$("#my_select").change(function(){
		var n = $("#my_select").val();
	
		switch(n){
			case "1":
			{
				$(".habrahabr\\.ru").css('display',"block");
				$(".maduza\\.io").css('display',"block");
				$(".lenta\\.ru").css('display',"block");
				break;
			}
			case "2":
			{
				$(".habrahabr\\.ru").css('display',"block");
				$(".maduza\\.io").css('display',"none");
				$(".lenta\\.ru").css('display',"none");
				break;
			}
			case "3":
			{
				$(".habrahabr\\.ru").css('display',"none");
				$(".maduza\\.io").css('display',"block");
				$(".lenta\\.ru").css('display',"none");
				break;
			}
			case "4":
			{
				$(".habrahabr\\.ru").css('display',"none");
				$(".maduza\\.io").css('display',"none");
				$(".lenta\\.ru").css('display',"block");
				break;
			}
		}

	});


//};