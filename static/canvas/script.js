$(".canvas-item").mouseover(function(){
    var id = $(this).attr('id');
    $("#" + id + "-edit").show();
    $("#" + id + "-delete").show();
});

$(".canvas-item").mouseout(function(){
    var id = $(this).attr('id');
    $("#" + id + "-edit").hide();
    $("#" + id + "-delete").hide();
});

$(".canvas-item-delete").click(function(){
    var el = $(this).parent();
    var id =  $(this).attr('id');
    var url = $(location).attr('pathname') + id.split('-')[1] + '/delete/';
    var ajax = $.ajax({
        type: 'GET',
        url: url
    });
    ajax.complete(function(jqXHR){
        el.remove();
    });
});

$(".canvas").mouseover(function(){
    var id = $(this).attr('id');
    $("#" + id + "-edit").show();
    $("#" + id + "-delete").show();
});

$(".canvas").mouseout(function(){
    var id = $(this).attr('id');
    $("#" + id + "-edit").hide();
    $("#" + id + "-delete").hide();
});

$(".canvas-delete").click(function(){
    var el = $(this).parent();
    var id =  $(this).attr('id');
    var url = $(location).attr('pathname') + id.split('-')[1] + '/delete/';
    var ajax = $.ajax({
        type: 'GET',
        url: url
    });
    ajax.complete(function(jqXHR){
        el.remove();
    });
});
