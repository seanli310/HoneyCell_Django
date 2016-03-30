

setInterval(task_finished_popup, 3000);

function task_finished_popup() {
	var username = document.getElementById("myUsername").innerHTML;
	
	var modal = document.getElementById('task_completed_modal');

	var close = document.getElementById("task_completed_modal_close");

	var close_btn = document.getElementById("task_completed_modal_close_btn");



	// When the user clicks on close (x) or btn, close the modal
	close.onclick = function() {
	    modal.style.display = "none";
	}
	// When the user clicks on close btn, close the modal
	close_btn.onclick = function() {
		$("#task_completed_modal_body").html("");
		modal.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
	    if (event.target == modal) {
	    	$("#task_completed_modal_body").html("");
	        modal.style.display = "none";
	    }
	}


	$.ajax({
		url: "/task_finished_ajax_check_database/",


		success: function(messageString) {
			console.log("Success");
			// console.log(completed_tasks.task_name);

			if (messageString != "") {
				// open the modal 
		    	modal.style.display = "block";
		    	$("#task_completed_modal_body").append(messageString);
			}

			

	    	
		}
	});


}