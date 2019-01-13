function getMoreInfo(id) {
	let data = {"id": id}
	url = '/getMoreInfo'
	var xhr = new XMLHttpRequest();
	xhr.open("POST", url, true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.onreadystatechange = function () {
	    if (xhr.readyState === 4 && xhr.status === 200) {
	    	let parsed_json = JSON.parse(xhr.responseText);
	    	addMoreInfoContainer(id);
			populateMoreInfo(id, parsed_json);
		}
	};
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
	xhr.send(JSON.stringify(data));
}

function populateMoreInfo(product, json) {
	let modal = document.getElementById(product+"-more-info-modal")
	console.log(json);
	modal.innerHTML = json['best bits'];

}


function addMoreInfoContainer(idName) {
	let row = document.getElementById(idName);
	let modal = document.createElement("div");
	let close_btn = document.createElement("div");
	modal.setAttribute("class", "modal");
	modal.setAttribute("id", idName+"-more-info-modal");
	close_btn.setAttribute("class", "close-btn")
	row.appendChild(modal);
	modal.appendChild(close_btn);
	modal.style.display = 'block'

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
