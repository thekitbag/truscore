let current_games_state = {}

function addRegisterListeners() {
	document.addEventListener('click', function (event) {
		if (event.target.matches('.reg')) {
			let id = event.target.id[3];
			registerPlayer(id);
		}

	}, false)};


function createElement(type, className, id){
	a = document.createElement(type);
	a.setAttribute("class", className);
	a.setAttribute("id", id);
	return a
}

function attatchElement(element, target){
	return document.getElementById(target).appendChild(element);
}

function jsonPost(url, data) {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", url, true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.onreadystatechange = function () {
	    if (xhr.readyState === 4 && xhr.status === 200) {
	        if (xhr.responseText == "Registration successful") {
	        	window.location.href = "/game";
	        } else if (xhr.responseText == "Player not logged in") {
	        	window.location.href = "/login";
        	}	        
	    }
	};
	//var data = JSON.stringify({"email": "hey@mail.com", "password": "101010"});
	xhr.send(JSON.stringify(data));
}

function registerPlayer(id) {
	jsonPost('/registerPlayer', {'id':id})
}



function addGamesToList(gamedata){
	let number_of_games = gamedata.length
	current_games_state = gamedata
	for (let i = 0; i < number_of_games; i++) {
		let gameid = i+1		
		let game = createElement("div", "game-row", "game"+gameid)
		attatchElement(game,"games-list");			
		for (let j = 0; j < 4; j++){
			keys = ["game_id", "entrants", "player_list", "status"]
			titles = 	["ID", "Size", "Players", "Status"]					
			let game_info_entry = createElement("div", "game-info-entry", "game"+gameid+"box"+j);
			let infotitle = createElement("div", "title", "game"+gameid+"title"+titles[j]);
			let infovalue = createElement("div", "value", "game"+gameid+"value"+titles[j]);
			attatchElement(game_info_entry, "game"+gameid)
			game_info_entry.appendChild(infotitle);
			game_info_entry.appendChild(infovalue);
			infotitle.innerHTML = titles[j]
			infovalue.innerHTML = gamedata[i][keys[j]]			
		}		
		let regbutton = createElement("div", "btn reg", "reg"+gamedata[i]["game_id"]);
		regbutton.innerHTML = "Register";		
		attatchElement(regbutton, "game"+gameid);		
	}	
}

function updateList(gamedata) {
	//for item in gamedata if it exists updateInfo else addgamestolist()
	let number_of_games = gamedata.length
	if (gamedata.length == current_games_state.length) {
		for (let i = 0; i < number_of_games; i++) {
			let gameid = i+1
			let player_list = document.getElementById("game"+gameid+"value"+"Players")
			player_list.innerHTML = gamedata[i]['player_list']
		};
	} else {
		current_games_state = gamedata
		games_list = document.getElementById("games-list")
		while (games_list.firstChild) {
    		games_list.removeChild(games_list.firstChild);
		}
		addGamesToList(gamedata);	
	};	
};


function updateLobby() {
	fetch("/lobbydata")
	  .then(function(response) {
	    return response.json();    
	  })
	  .then(function(myJson) {
	    console.log(myJson);
	    updateList(myJson);	    
  });
}

function getLobbyDataOnPageLoad() {
	fetch("/lobbydata")
	  .then(function(response) {
	    return response.json();    
	  })
	  .then(function(myJson) {
	    console.log(myJson);
	    addGamesToList(myJson);
	    addRegisterListeners();
  });
}


getLobbyDataOnPageLoad()
setInterval(function() {updateLobby();}, 6000);





