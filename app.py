from flask import Flask
import dataset
from flask.ext import restful
from flask.ext.restful import reqparse, abort, Api, Resource
import json

app = Flask(__name__)
api = restful.Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('list_name', type=str)
db = dataset.connect('sqlite:///database.db')

@app.route('/')
def index():
	return "Hello World"

class TodoList(restful.Resource):

	def get(self,todo_list_id=None):

		todo_lists = db['todo_lists']

		if todo_list_id:
			return todo_lists.find_one(id=todo_list_id)

		else:
			lists = todo_lists.all()

			results = []
			for row in lists:
				results.append(row)

			return results

	def post(self):
		todo_lists = db['todo_lists']

		args = parser.parse_args()
		resp = todo_lists.insert(dict(list_name=args["list_name"]))

		return resp

	def delete(self, todo_list_id):
		todo_lists = db['todo_lists']

		todo_lists.delete(id=todo_list_id)
		return '', 204

class TodoItem(restful.Resource):
	def get(self, todo_list_id, todo_item_id=None):
		todo_item_table = db['todo_items']

		if todo_item_id:
			return todo_item_table.find_one(id=todo_list_id)
		else:
			results = []
			for row in todo_item_table.all():
				results.append(row)

			return results

	def post(self, todo_list_id):
		todo_item_table = db['todo_items']

		resp = todo_item_table.insert(task=args['task'])
		return resp

	def delete(self, todo_list_id, todo_item_id):

		todo_item_table = db['todo_items']
		todo_item_table.delete(id=todo_item_id)

		return '', 204



api.add_resource(TodoList, '/todo_lists', '/todo_lists/<int:todo_list_id>')
api.add_resource(TodoItem, '/todo_lists/<int:todo_list_id>/todo_items', '/todo_lists/<int:todo_list_id>/todo_items/<int:todo_item_id>')


if __name__ == '__main__':
	app.run(debug=True)
