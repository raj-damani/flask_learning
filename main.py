from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self, name, test):
		return {"name":name, "test":test}
		
	"""def post(self):
		return {"data":"Hello World"}"""
videos = {}
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str,help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="views")
video_put_args.add_argument("likes", type=int, help="likes")

class Video(Resource):
	def get(self, video_id):
		return videos[video_id]
	def put(self, video_id):
		args = video_put_args.parse_args()
		return {video_id:args}
		 	
api.add_resource(Video,'/video/<int:video_id>')
			
#api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")


if __name__ == "__main__":
	app.run(debug=True)
	
