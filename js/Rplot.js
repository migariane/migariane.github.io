(function($) {
    $(document).ready(function() {
	
	$('#Rplot').scianimator({
	    'images': ['images/Rplot1.png', 'images/Rplot2.png', 'images/Rplot3.png', 'images/Rplot4.png', 'images/Rplot5.png', 'images/Rplot6.png', 'images/Rplot7.png', 'images/Rplot8.png', 'images/Rplot9.png', 'images/Rplot10.png', 'images/Rplot11.png', 'images/Rplot12.png'],
	    'width': 480,
	    'delay': 1000,
	    'loopMode': 'loop'
	});
	$('#Rplot').scianimator('play');
    });
})(jQuery);
