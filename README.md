# JS, the DOM, and AJAX

## External Links
- https://api.jquery.com/jQuery.ajax/

Requires:
- dom manipulation

Covers:
- AJAX w/ jQuery
- serialization
- JSON
- Callbacks
- REST

Bonuses:
- cURl
- Extending APIs
- flask-restful

## APIs! APIs! APIs!
This exercise will deviate slightly from the regular workflow. We have provided the python backend code for you that your todo list app will be intergrating with. 

## Getting Setup
Next, bootstrap your environment by creating a python virtual environment and installing the required packages in requirements.txt. 

## Let's Begin

Start by opening `static/js/app.js` and `index.html`. These are the 2 main files that we'l be working from. Your html should go in `index.html` and your Javascript should go in `static/js/app.js`.

Next, take a look at `api.py`. You'll notice there is some standard flask code up at the top.

````python

@app.route('/')
def index():
    return render_template('index.html')

````

Below that flask code are some classes. All that you need to know to get started is that these classes are a different way of writing web code and will be handling your web requests.

Even though we are mixing flask and flask-restful we can run the python app the same way we have run flask apps in the past, `python api.py`.  

Now that we have everything up and running, it's time to start builing our todo list.

- Instead of doing a regular form submit and page refresh, create a todo list via an ajax post
- Do the same as above with todo list items
- add the ability to delete a list

## Extra Credit
- remove all page refreshes (ie clicking on the todo list > list of items)
- make the lists sortable(by id or alphabetically)
- add support to reorder items in the todo list
- add bootstrap / styling


### Notes on testing your api

cURL is amazing




