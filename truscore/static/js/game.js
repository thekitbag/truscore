var socket = io.connect('http://' + document.domain + ':' + location.port);
        socket.on('connect', function() {
            socket.emit('connect event');
        });

function unRegisterPlayer() {
	console.log("X")
	url = '/unRegister'
	var xhr = new XMLHttpRequest();
	xhr.open("POST", url, true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.onreadystatechange = function () {
	    if (xhr.readyState === 4 && xhr.status === 200) {
	        if (xhr.responseText == "Player Unregistered") {
	        	window.location.href = "/lobby";
	        } 	        
	    }
	};
	//var data = JSON.stringify({"email": "hey@mail.com", "password": "101010"});
	xhr.send();
}


document.getElementById("unregister").addEventListener("click", function(){
    unRegisterPlayer();
});