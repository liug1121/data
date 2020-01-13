$(function(){
	$("#search_more").click(function(){
		htmlData = ''
		startPage = $('.datas').length
		words = $("#search_words").val()
	    $.post("searchmore/",{size:10, startPage:startPage - 1, words:words} ,function(data, status){
	    		htmlData = data
	    		if(htmlData.length == 1)
	    			$("#search_more").html('没有更多数据了');
	    		else
	    			$("#list").append(htmlData)
	    });
	  });
});