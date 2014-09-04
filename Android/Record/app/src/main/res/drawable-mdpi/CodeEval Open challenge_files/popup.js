jQuery(document).ready(function($){
		
	// Popup window
    $('a.popupWindow').click(function(){
        window.open(
        	this.href,
			'Challenge',
			'left=20, top=20, width=600, height=700, location=0, scrollbars=1'
		);
        return false;
    });

});

