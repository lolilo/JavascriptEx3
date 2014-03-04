from flask import Flask, render_template, request, redirect, flash
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


# handler for asynchronous request
@app.route('/ajax/todo_list', methods=['POST'])
def ajax_todo_list():
    return render_template('ajax_template', new_list=new_list)

@app.route('/todo_lists/<int:id>')
def todo_list_show(id):
    items = todo_item_table.find(todo_list_id=id)
    items = [x for x in items]

    return render_template("todo_list.html", items=items)

@app.route('/todo_lists/<int:id>', methods=["POST"])
def todo_item_create(id):
    resp = todo_item_table.insert(dict(task=request.form.get("task"), todo_list_id=id, done=False))    

    return redirect("/todo_lists/%d" % id)


@app.route('/todo_lists/poll')
def poll_for_lists():
    results = todo_lists.all()
    lists = [l for l in results]
    return render_template("todo_list_partial.html", lists=lists)


if __name__ == '__main__':
    app.run(debug=True)
