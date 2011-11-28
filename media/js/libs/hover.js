$(function() {
	// set opacity to 100%
	$(".featured-project-bg").css("opacity","1.0");
	$(".featured-project-bg").hover(function () {	 
		// set opacity to 50%
		$(this).stop().animate({
			opacity: 0.5
		}, "slow");
	},
	 
	function () {	 
		// set opacity back to 100%
		$(this).stop().animate({
			opacity: 1.0
		}, "slow");
	});
});