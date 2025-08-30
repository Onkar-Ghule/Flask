from flask import Flask,render_template,request,redirect,url_for
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
@app.route("/form",methods=['GET','POST'])
def form():
  if request.method=="GET":
    return render_template("form.html")
  else:
    maths=float(request.form["maths"])
    science=float(request.form["science"])
    history=float(request.form["history"])
    avg_marks=(maths+science+history)/3
    res=""
    if avg_marks>=50:
       res="success"
    else:
      res="fail"
    return redirect(url_for(res,score=avg_marks))
if __name__=="__main__":
  app.run(debug=True) 