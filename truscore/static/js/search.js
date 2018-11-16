function getMoreInfo(id) {
	let data = {"id": id}
	url = '/getMoreInfo'
	var xhr = new XMLHttpRequest();
	xhr.open("POST", url, true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.onreadystatechange = function () {
	    if (xhr.readyState === 4 && xhr.status === 200) {
	        displayMoreInfo(xhr.responseText);	        
	    }
	};
	//var data = JSON.stringify({"email": "hey@mail.com", "password": "101010"});
	xhr.send(JSON.stringify(data));
}

function GetRatingScreen(id) {
	alert(id);
}

function displayMoreInfo(text) {
	let container = document.getElementById('search-results')
	let modal = document.createElement("div")
	modal.setAttribute("class", "modal");
	modal.setAttribute("id", "more-info-modal")
	container.appendChild(modal)
	modal.innerHTML = text
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


addMoreInfoListeners()
addRateListeners()

