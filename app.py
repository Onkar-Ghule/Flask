from flask import Flask,render_template
##Flask app routing 
##create a simple flask application
app=Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
  return "<h1>wlecome to the web app<h1>"
@app.route('/index')
def index():
  return "welcome to the web page index page"
@app.route('/success/<int:score>')
#variable rule 
#1.the data is by default string we can change its type  
def success(score):
  return "the person has passe with score:"+str(score)
@app.route('/fail/<score>')
def fail(score):
  return "the person has fail with score:"+score

if __name__=="__main__":
  app.run(debug=True) 