### Polling
#### Where we ask if we're there yet...a lot

### Helpful functions
`window.setInterval`[https://developer.mozilla.org/en-US/docs/Web/API/Window.setInterval]


### Getting started
Greetings weary travelers.  At this point you've posted your data to the server but would like to have it update the page, not just alert us.

Let's write a function that sends an ajax get request to our backend and log the response out to the console.


````javascript

var getListsFromServer = function() {
    $.ajax({
            url:'/todo_lists/poll',
            method: "GET"
        }).done(function(data){
            console.log(data);
        });
}

````

Take a peek at the response in the console. We can see it's just HTML. Modify the above function to add the list names in the dom instead of printing it in the console.

Now, let's setup our interval timer to poll the server for new list names every 20 seconds.

````
// Poll the server every 20 seconds
setInterval(getListsFromServer, 20000); 

````

Save your files, refresh your browser. Open a new browser window to the list app side-by-side with your first window. Start creating a bunch of new lists in one window. Every 20 seconds, you'll see the other windows todo lists update. Awesome!
