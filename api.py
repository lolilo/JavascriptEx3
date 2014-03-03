from flask import Flask, render_template, request, redirect, flash
from flask.ext import restful
from flask.ext.restful import reqparse, Api, Resource
import json
import dataset

app = Flask(__name__)
app.secret_key = "Shhhhh!! Something Secret"
db = dataset.connect('sqlite:///database.db')

# Assign vars for our database tables
todo_item_table = db['todo_items']
todo_lists = db['todo_lists']

@app.route('/')
def index():
    return render_template('index.html', lists=todo_lists)

@app.route('/', methods=['POST'])
def index_post():
    list_name = request.form.get('todo_list_name')

    if not list_name:
        flash("I'm sorry, but you'll need to specify a list name")

    else:
        todo_lists.insert(dict(list_name=list_name))

        flash('Todo list %s created' % list_name)

    return redirect('/')

@app.route('/todo_lists/<int:id>')
def todo_list_show(id):
    items = todo_item_table.find(todo_list_id=id)
    items = [x for x in items]

    return render_template("todo_list.html", items=items)

@app.route('/todo_lists/<int:id>', methods=["POST"])
def todo_item_create(id):
    resp = todo_item_table.insert(dict(task=request.form.get("task"), todo_list_id=id))    

    return redirect("/todo_lists/%d" % id)

# flask-restful api code
api = restful.Api(app)

# flask-restful provides a more powerful way flask of validating arguments than flask.
# the req parse will ensure that the arguments to the api are valid before 
# running any of the request code
parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('list_name', type=str)

# Handle showing (get), creating (post), and deletion (delete) of lists
class TodoList(restful.Resource):

    def get(self,todo_list_id=None):
        """
            Handle showing either 1 list or all of the lists

        """
        todo_lists = db['todo_lists']

        if todo_list_id:
            return todo_lists.find_one(id=todo_list_id)

        else:
            lists = todo_lists.all()

            results = [row for row in lists] 
            return results

    def post(self):
        todo_lists = db['todo_lists']

        args = parser.parse_args()
        resp = todo_lists.insert(dict(list_name=args["list_name"]))

        return resp

    def delete(self, todo_list_id):
        todo_lists = db['todo_lists']

        todo_lists.delete(id=todo_list_id)
        return '', 204 # No Content, we don't want to send anything back on deletion

# Handle showing (get), creating (post), and deletion (delete) of todo items
class TodoItem(restful.Resource):
    def get(self, todo_list_id, todo_item_id=None):
        todo_item_table = db['todo_items']

        if todo_item_id:
            return todo_item_table.find_one(id=todo_list_id)
        else:
            items = todo_item_table.all()
            results = [row for row in items]
            return results

    def post(self, todo_list_id):
        todo_item_table = db['todo_items']

        resp = todo_item_table.insert(task=args['task'], todo_list_id=todo_list_id)
        return resp

    def delete(self, todo_list_id, todo_item_id):

        todo_item_table = db['todo_items']
        todo_item_table.delete(id=todo_item_id)

        return '', 204 # No Content, we don't want to send anything back on deletion


# These lines of code are how we register routes with flask-restful to their 
# respective classes and functions
# similar to @app.route('/') in regular flask
api.add_resource(TodoList, '/api/todo_lists', '/api/todo_lists/<int:todo_list_id>')
api.add_resource(TodoItem, '/api/todo_lists/<int:todo_list_id>/todo_items', '/api/todo_lists/<int:todo_list_id>/todo_items/<int:todo_item_id>')


if __name__ == '__main__':
    app.run(debug=True)
