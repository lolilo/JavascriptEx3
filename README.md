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
Bootstrap your environment by creating a python virtual environment and installing the required packages in requirements.txt. 

## Let's Begin
Start by opening `static/js/app.js` and `index.html`. These are the 2 main files that we'l be working from. Your html should go in `index.html` and your Javascript should go in `static/js/app.js`.

Now that we have everything up and running, it's time to start builing our todo list.

Instructions:

Building upon what you just did in `post.md`(NO COPY/PASTING):

Create Todo lists using $.ajax
- Clicking the submit button should post a new todo list to the server.  
- If it's successful, append the new todo item

Do the same thing for the todo items.
- Clicking the submit button should post a new todo item to the server.  
- If it's successful, append the new todo item

For these next two, you'll need to tie python into the mix.
- Add the ability to delete a todo list, todo list item.
- Add the ability to mark a todo item as done.

Finally, Remove all page refreshes (ie clicking on the todo list > list of items)


Bonus:
- make the lists sortable(by id or alphabetically)
- add support to reorder items in the todo list
- add bootstrap / styling

