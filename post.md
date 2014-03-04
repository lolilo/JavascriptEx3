## Posting to the server

Here is a sample ajax request to post data to a url.  Open the todo list ( http://localhost:5000 ) in Xhrome and copy the ajax code below into the Chrome console(you can access the console by right clicking anywhere on the page and selecting "Inspect Element"). It will fail but you can take a look at what happens in the Network tab of the Chrome inspector.

````javascript

        $.ajax({
            url: "/url",
            method: "POST",
            data: {
                list_name: "List Name"
            },

        }).done(function(data){
            alert(data);
        }).fail(function(){
            alert('fail!!!');
        });
    
````


## Form Serialization 
Let's take a look at the form that has the data we're sending. It looks something like this:

````html
<form id="todo_list_form" method="POST">
    <input type="text" name="todo_list_name">
    <input type="submit" id="form_submit" value="Create new list">
</form>
````

In order to submit this form to the server, we'll need to convert it to a key-value string. The keys will be the names of the form elements, with the values being the dom element's value. Fortunately jQuery provides this function for us.

To see this in action, type something in the list name input and run the following serialization fucntion in the Chrome inspector console.

````javascript
$("form#todo_list_form").serialize();

````

You'll see a response that looks exactly like a query string. This is all that is required for preparing the data to post to a server. 


Let's tie it all together now. Conceptually we want to tie in a button click, form serialization, and the ajax function.

````javascript
// on button click / form submission
    // grab data from form
    // send data to server
        // if success
            // update the page
        // if fail
            // warn the user

````


DON'T COPY AND PASTE, but write the following code in the document.ready function given to you in `static/js/app.js`. While you write the code, try and think about what it's doing and which callback function will get called before running the code and refreshing.


How would the code run without the done function? What if you left off the fail callback?


```javascript

    var formSubmitButton = $("#form_submit");

    formSubmitButton.on("click", function(event){
        e.preventDefault(); // prevent the browser form submission from happening
        $.ajax({
            url: "/",
            method: "POST",
            data: $("form#todo_list_form").serialize(),
        }).done(function(data){
            alert(data);
        }).fail(function(){
            alert('fail!!!');
        });

    });
```

At this point if you haven't tested the code, save your files and refresh the page to try it out.  You'll see the done callback is being called (it's sending an alert with the data), but we don't see the page updating. 

We're halfway there! Continue this adventure on `polling.md`



