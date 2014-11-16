$(document).ready(function() {
    $('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
     	$.get('/rango/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
       });
	});

	$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/rango/suggest_category/', {suggestion: query}, function(data){
         $('#cats').html(data);
        });
	});

	$('.rango-add').click(function(){
        var catid, title, url;
        var me = $(this)
        catid = $(this).attr("data-catid");
        page_title = $(this).attr("data-title");
        page_url = $(this).attr('data-url');
        $.get('/rango/auto_add_page/', {category_id: catid, title: page_title, url: page_url}, function(data){
         	$('#pages').html(data);
            me.hide()
        });
	});

});
