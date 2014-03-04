$(document).ready(function(){




var formSubmitButton = $("#form_submit");

formSubmitButton.on("click", function(event) {
    event.preventDefault(); // prevent the browser form submission from happening
    $.ajax({
        url: "/",
        method: "POST",
        data: $("form#todo_list_form").serialize(),
    }).done(function(responseData){ // data here is not the same as data in .ajax
        // data or responseData is returned by the web server
        alert(responseData);
    }).fail(function(){
        alert('fail!!!');
    });
});

// sends ajax get request to backend and log the response out to the console
// Modify the above function to add the list names in the dom 
// instead of printing it in the console.
var getListsFromServer = function() {
    $.ajax({
        url: '/todo_lists/poll',
        method: "GET"
    }).done(function(data){
        console.log(data);
    });
};




            var assignedHouse = document.getElementById(houseName);
            var assignedStudent = document.createElement('p');
            assignedStudent.innerHTML = studentName;
            console.log(assignedStudent);
            assignedHouse.appendChild(assignedStudent);

});