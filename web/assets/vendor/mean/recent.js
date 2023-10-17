$(document).ready(function road(){
    timer = setInterval( function () {
        $.ajax({
            url: "http://175.126.123.217:5657/machbase?q=select value from tag where name ='ph' order by time desc limit 1;",
            dataType: 'json',
            type: 'GET',
            success: function(data){
                var $huMean = data.data[0]['value'];
                 $('.PhRect').empty();
                 $('.PhRect').append($huMean);
               /* $('.PhIcon').append('<i class="fa-solid fa-droplet-percent"></i>')*/; 
            }
        });
        $.ajax({
            url: "http://175.126.123.217:5657/machbase?q=select value from tag where name ='temp' order by time desc limit 1;",
            dataType: 'json',
            type: 'GET',
            success: function(data){
                var $huMean = data.data[0]['value'];
                 $('.tempRect').empty();
                 $('.tempRect').append($huMean);
                 /*$('.temphIcon').append('<i class="fa-solid fa-droplet-percent"></i>');*/
            }
        });
        $.ajax({
            url: "http://175.126.123.217:5657/machbase?q=select value from tag where name ='humi' order by time desc limit 1;",
            dataType: 'json',
            type: 'GET',
            success: function(data){
                var $huMean = data.data[0]['value'];
                 $('.humiRect').empty();
                 $('.humiRect').append($huMean);
                 /*$('.humiIcon').append('<i class="fa-solid fa-droplet-percent"></i>');*/
            }
        });
        $.ajax({
            url: "http://175.126.123.217:5657/machbase?q=select value from tag where name ='Co2' order by time desc limit 1;",
            dataType: 'json',
            type: 'GET',
            success: function(data){
                var $huMean = data.data[0]['value'];
                 $('.Co2Rect').empty();
                 $('.Co2Rect').append($huMean);
                 /*$('.Co2Icon').append('<i class="fa-solid fa-droplet-percent"></i>');*/
            }
        });
        $.ajax({
            url: "http://175.126.123.217:5657/machbase?q=select time from tag order by time desc limit 1;",
            dataType: 'json',
            type: 'GET',
            success: function(data){
                var $huMean = data.data[0]['time'].substr(0,19);
                 $('.time').empty();
                 $('.time').append($huMean);
                 /*$('.Co2Icon').append('<i class="fa-solid fa-droplet-percent"></i>');*/
            }
        });
        
    }, 1000);
});
