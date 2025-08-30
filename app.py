from flask import Flask
##Flask app routing 
##create a simple flask application
app=Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
  return "<h1>wlecome to the web app<h1>"
@app.route('/index')
def index():
  return "welcome to the web page index page"
if __name__=="__main__":
  app.run(debug=True)