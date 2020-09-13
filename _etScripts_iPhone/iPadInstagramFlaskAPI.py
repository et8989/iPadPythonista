from flask import 
class InstaApi(Object)
	app= Flask('insta_api')  
	
	def _init_(self):
	pass      

	@staticmethod
	@app.route('/ping',method=['GET'])
	def ping():
	return "pong"           
	def run(self,debug=False, port=8080):
	 self.app.run(port=port, debug=debug)

if __name__ == '__main__':
	app = InstaApi
	app.run()
