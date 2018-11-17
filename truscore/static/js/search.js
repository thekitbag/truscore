function getMoreInfo(id) {
	let data = {"id": id}
	url = '/getMoreInfo'
	var xhr = new XMLHttpRequest();
	xhr.open("POST", url, true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.onreadystatechange = function () {
	    if (xhr.readyState === 4 && xhr.status === 200) {
	    	let parsed_json = JSON.parse(xhr.responseText);
	        displayMoreInfo(parsed_json);	        
	    }
	};
	//var data = JSON.stringify({"email": "hey@mail.com", "password": "101010"});
	xhr.send(JSON.stringify(data));
}

function GetRatingScreen(id) {
	alert(id);
}

function displayMoreInfo(json) {
	let container = document.getElementById('search-results');
	let modal = document.createElement("div");
	modal.setAttribute("class", "modal");
	modal.setAttribute("id", "more-info-modal");
	container.appendChild(modal);
	let close_btn = document.createElement("div");
	close_btn.setAttribute("class", "close-btn");
	close_btn.setAttribute("id", "close-more-info");
	modal.appendChild(close_btn);
	close_btn.innerHTML = "X";
	console.log(json);
	let trend_container = document.createElement("div");
	trend_container.setAttribute("class", "modal-container");
	trend_container.setAttribute("id", "trend-container");
	let recent_votes_container = document.createElement("div");
	recent_votes_container.setAttribute("class", "modal-container");
	recent_votes_container.setAttribute("id", "recent-votes-container");
	modal.appendChild(trend_container);
	modal.appendChild(recent_votes_container);
	trend_container.innerHTML = Object.keys(json['trend'])
	recent_votes_container.innerHTML = Object.keys(json['recent votes'])
}


function addMoreInfoListeners() {
	document.addEventListener('click', function (event) {
		if (event.target.matches('.more-info')) {
			let id = event.target.id[11];
			getMoreInfo(id)
		}

	}, false)};

function addRateListeners() {
	document.addEventListener('click', function (event) {
		if (event.target.matches('.rate')) {
			let id = event.target.id[6];
			GetRatingScreen(id)
		}

	}, false)};

function addCloseButtonListener() {
	document.addEventListener('click', function (event) {
		if (event.target.matches('.close-btn')) {
			let modal = document.getElementById('more-info-modal')
			let container = document.getElementById('search-results')
			container.removeChild(modal);
			
		}

	}, false)};

addMoreInfoListeners();
addRateListeners();
addCloseButtonListener();


