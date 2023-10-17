function getbtn(){
window_1 = document.getElementById("window_1");
window_2 = document.getElementById("window_2");
Ventil = document.getElementById("Ventil");
w_pump = document.getElementById("w_pump");
}



window_1.addEventListener("click", function() {   
          
        getbtn()
        if (window_1.checked==true){
                fetch("http://175.126.123.217:5001/machbase?q=insert into controll values ('window_1', sysdate, 1);")
                startConnect();
                publish(window_1);
                startDisconnect()
                
        }
        else
        {
                fetch("http://175.126.123.217:5001/machbase?q=insert into controll values ('window_1', sysdate, 0);")
                startConnect();
                var topic = "btn1";
                message = new Paho.MQTT.Message(false); 
                message.destinationName = topic; message.qos = 2; 
                client.send(message);
                startDisconnect()
        }
});
window_2.addEventListener("click", function() {  
           
        getbtn()
        if (window_2.checked==true){
                fetch("http://175.126.123.217:5001/machbase?q=insert into controll values ('window_2', sysdate, 1);")
                var topic = $(element).attr("btn2");
                message = new Paho.MQTT.Message(true); 
                message.destinationName = topic; message.qos = 2; 
                client.send(message);
        }
        else
        {
                fetch("http://175.126.123.217:5001/machbase?q=insert into controll values ('window_2', sysdate, 0);")
                var topic = $(element).attr("btn2");
                message = new Paho.MQTT.Message(false); 
                message.destinationName = topic; message.qos = 2; 
                client.send(message);
        }
});
Ventil.addEventListener("click", function() {    
         
        getbtn()
        if (Ventil.checked==true){
                fetch("http://175.126.123.217:5001/machbase?q=insert into controll values ('Ventil', sysdate, 1);")
                var topic = $(element).attr("btn3");
                message = new Paho.MQTT.Message(true); 
                message.destinationName = topic; message.qos = 2; 
                client.send(message);
        }
        else
        {
                fetch("http://175.126.123.217:5001/machbase?q=insert into controll values ('Ventil', sysdate, 0);")
                var topic = $(element).attr("btn3");
                message = new Paho.MQTT.Message(false); 
                message.destinationName = topic; message.qos = 2; 
                client.send(message);
        }
});
w_pump.addEventListener("click", function() {     
        
        getbtn()
        if (w_pump.checked==true){
                fetch("http://175.126.123.217:5001/machbase?q=insert into controll values ('w_pump', sysdate, 1);")
                var topic = $(element).attr("btn4");
                message = new Paho.MQTT.Message(true); 
                message.destinationName = topic; message.qos = 2; 
                client.send(message);
        }
        else
        {
                fetch("http://175.126.123.217:5001/machbase?q=insert into controll values ('w_pump', sysdate, 0);")
                var topic = $(element).attr("btn4");
                message = new Paho.MQTT.Message(false); 
                message.destinationName = topic; message.qos = 2; 
                client.send(message);
        }
});
timer = setInterval( function () {
        getbtn();
        $.ajax({
                url: "http://175.126.123.217:5001/machbase?q=select value from controll where name ='window_1' order by time desc limit 1;",
                dataType: 'json',
                type: 'GET',
                success: function(data){
                    var $huMean = data['value'];
                     if ($huMean == 1)
                     {
                        $('input[id="btn1"]').prop('checked',true);
                     }
                     else
                     {
                        $('input[id="btn1"]').prop('checked',false);

                     }
                }
            });
            $.ajax({
                url: "http://175.126.123.217:5001/machbase?q=select value from controll where name ='window_2' order by time desc limit 1;",
                dataType: 'json',
                type: 'GET',
                success: function(data){
                    var $huMean = data['value'];
                     if ($huMean == 1)
                     {
                        $('input[id="btn2"]').prop('checked',true);
                     }
                     else
                     {
                        $('input[id="btn2"]').prop('checked',false);

                     }
                }
            });
            $.ajax({
                url: "http://175.126.123.217:5001/machbase?q=select value from controll where name ='Ventil' order by time desc limit 1;",
                dataType: 'json',
                type: 'GET',
                success: function(data){
                    var $huMean = data['value'];
                     if ($huMean == 1)
                     {
                        $('input[id="btn3"]').prop('checked',true);
                     }
                     else
                     {
                        $('input[id="btn3"]').prop('checked',false);

                     }
                }
            });
            $.ajax({
                url: "http://175.126.123.217:5001/machbase?q=select value from controll where name ='w_pump' order by time desc limit 1;",
                dataType: 'json',
                type: 'GET',
                success: function(data){
                    var $huMean = data['value'];
                     if ($huMean == 1)
                     {
                        $('input[id="btn4"]').prop('checked',true);
                     }
                     else
                     {
                        $('input[id="btn4"]').prop('checked',false);

                     }
                }
            });
    }, 1000);


    