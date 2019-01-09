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

function sendRating(score, establishment) {
	let data = {"score": score, "establishment":establishment}
	url = '/sendRating'
	var xhr = new XMLHttpRequest();
	xhr.open("POST", url, true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.onreadystatechange = function () {
	    if (xhr.readyState === 4 && xhr.status === 200) {
	        console.log(xhr.responseText);	        
	    }
	};
	//var data = JSON.stringify({"email": "hey@mail.com", "password": "101010"});
	xhr.send(JSON.stringify(data));
}

function populateMoreInfo(json) {
	//this could be DRYed out a bit
	let trend = document.getElementById("trend-container")
	let recent_votes = document.getElementById("recent-votes-container")
	let best_bits = document.getElementById("best-bits-container")
	let worst_bits = document.getElementById("worst-bits-container")
	let comments = document.getElementById("comments-container")
	let trend_keys = Object.keys(json['trend'])
	let recent_votes_keys = Object.keys(json['recent votes'])
	let worst_bits_keys= Object.keys(json['worst bits'])
	let best_bits_keys= Object.keys(json['best bits'])
	let comments_keys= Object.keys(json['comments'])
	addDataToContainer(json, 'trend', trend, trend_keys)
	addDataToContainer(json, 'recent votes', recent_votes, recent_votes_keys)
	addDataToContainer(json, 'best bits', best_bits, best_bits_keys)
	addDataToContainer(json, 'worst bits', worst_bits, worst_bits_keys)
	addDataToContainer(json, 'comments', comments, comments_keys)

}

function addDataToContainer(data, groupKey, container, itemKeys) {	
	for (let i=0; i < itemKeys.length; i++) {
		let row = document.createElement("div");
		row.setAttribute("class", "row")
		row.setAttribute("id", groupKey+"row"+i)
		let title = document.createElement("div");
		let value = document.createElement("div");
		title.setAttribute("class", "more-info-data title");
		value.setAttribute("class", "more-info-data value");
		let key = itemKeys[i]
		title.innerHTML = key
		value.innerHTML =data[groupKey][key]
		container.appendChild(row)
		row.append(title)
		row.append(value)
	}
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
	addMoreInfoContainer("trend-container");
	addMoreInfoContainer("recent-votes-container");
	addMoreInfoContainer("best-bits-container");
	addMoreInfoContainer("worst-bits-container");
	addMoreInfoContainer("comments-container");
	populateMoreInfo(json)	
}

function addMoreInfoContainer(idName) {
	let container = document.createElement("div");
	container.setAttribute("class", "modal-container");
	container.setAttribute("id", idName);
	let modal = document.getElementById("more-info-modal")
	modal.appendChild(container);

}

function addMoreInfoListeners() {
	document.addEventListener('click', function (event) {
		if (event.target.matches('.result')) {
			let id = event.target.id;
			getMoreInfo(id)
		}

	}, false)};

function addRateListeners() {
	document.addEventListener('click', function (event) {
		if (event.target.matches('.rate')) {
			let length = event.target.id.length
			let button_id = event.target.id.slice(5,length);
			console.log(button_id)
			let id = 'rating-modal-' + button_id
			document.getElementById(id).style.display = 'block'
		}

	}, false)};

function addCloseButtonListener() {
	document.addEventListener('click', function (event) {
		if (event.target.matches('.close-btn')) {
			event.target.parentNode.parentNode.style.display = 'none';			
		}

	}, false)};

function addSubmitButtonListener() {
	document.addEventListener('click', function (event) {
		if (event.target.matches('.submit-rating')) {
			let length = event.target.id.length
			let name = event.target.id.slice(5,length);
			let selector_id = 'rating-selector-'+name
			let dropdown = document.getElementById(selector_id)
			let selected = dropdown.options[dropdown.selectedIndex].value;
			sendRating(selected, name);		
			
		}

	}, false)};

function addSubmitNewButtonListener() {
	document.addEventListener('click', function (event) {
		if (event.target.matches('.submit-new-rating')) {
			let name = document.getElementById("establishment-name").value
			let dropdown = document.getElementById('rating-selector-new')
			let selected = dropdown.options[dropdown.selectedIndex].value;
			sendRating(selected, name);		
			
		}

	}, false)};

function addNewReviewListener() {
	document.addEventListener('click', function (event) {
		if (event.target.matches('#btn-new-review')) {
			document.getElementById('new-rating-modal').style.display = 'block'
					
		}

	}, false)};

function addNextScreenListener() {
	document.addEventListener('click', function (event) {
		if (event.target.matches('.next-screen')) {
			let divs_to_hide = document.getElementsByClassName("form-group-1")
			let divs_to_show = document.getElementsByClassName("form-group-2")
			let next_button = document.getElementById('next-screen-btn')
			let submit_button = document.getElementById('submit')
			next_button.style.display = 'none';
			submit_button.style.display = 'block';
			//divs_to_hide.push({4:next_button});
			//divs_to_show.push(submit_button);
			for(var i = 0; i < divs_to_hide.length; i++){
		        divs_to_hide[i].style.display = "none";
    		}
    		for(var i = 0; i < divs_to_show.length; i++){
		        divs_to_show[i].style.display = "block";
    		}
					
		}

	}, false)};

//this should obvs one single listener innit
addNewReviewListener();
addMoreInfoListeners();
addRateListeners();
addCloseButtonListener();
addSubmitButtonListener();
addSubmitNewButtonListener();
addNextScreenListener();
