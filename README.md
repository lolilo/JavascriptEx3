# JS, the DOM, and AJAX

Requires:
- Javascript
- dom manipulation
- jQuery

Covers:
- AJAX w/ jQuery
- callbacks
- form serialization


## Getting Setup
Clone this repo from Github. Once you have the code, you can bootstrap your environment by creating a python virtual environment and installing the required packages in requirements.txt. 

````bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
````

## Let's Begin

Follow the walkthroughs in https://github.com/hackbrightacademy/Javascript3/blob/master/post.md and then https://github.com/hackbrightacademy/Javascript3/blob/master/polling.md. Once you finish those, the assignment is below.

Assignment:

Building upon what you just did in `post.md`(NO COPY/PASTING) and without polling the server:

Create Todo lists using $.ajax
- Clicking the submit button should post a new todo list to the server using `$.ajax`.  
- add the new todo list to the end of the list using the done event

Do the same thing for the todo items.
- Clicking the submit button should post a new todo item to the server using `$.ajax`.  
- add the new todo item to the end of the list using the done event

Remove the page refresh that happens when clicking on a list name.
- clicking on a list name should clear the list of lists and replace it with the list of todo items.
- Add a button for the user to go back to the list of lists

For these next two, you'll need to write some python in addition to javascript. Feel free to modify the html at this point to finish this assignment.

Add the ability to mark a todo item as done.
- add an event to the checkboxes so clicking a checkbox marks that item as done(via an ajax request)
- write a flask handler that accepts post requests
- the route should be `/todo_lists/<int:list_id>/todo_item/<int:item_id>/done`
- the flask handler should return the list of items rendered in `todo_items_partial.html`.
- the ajax `done` event should update the list

to handle the database update, you will find https://dataset.readthedocs.org/en/latest/api.html#dataset.Table.update to be helpful.

Add the ability to delete todo lists and todo items.
- add a button next to each item / list that triggers a click event to send a post request to the server
- write two more flask handlers that accept post requests
- the routes should be `/todo_lists/<int:list_id>/delete` and `/todo_lists/<int:list_id>/todo_item/<int:item_id>/delete` respectively. 
- after deleting the list or item, the handler should the relevant rendered *_partial.html tempalte to the browser so it can update the page.
- the ajax `done` event should update the list


To handle the database delete, you will find https://dataset.readthedocs.org/en/latest/api.html#dataset.Table.delete helpful.





Bonus:
- make the lists sortable(by id or alphabetically)
- add support to reorder items in the todo list
- add bootstrap / styling

