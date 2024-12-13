from flask import Flask,render_template,request,redirect
from pymongo import MongoClient 
app=Flask(__name__)
my_client=MongoClient("localhost",27017)
my_db=my_client["College"]
students=my_db["students"]
callme=my_db["callme"]
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")
@app.route("/admission",methods=["GET"])
def admission():
    return render_template("admissions.html")
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method== "POST":
        Id=int(request.form["id"])
        name=request.form["name"]
        email=request.form["email"]
        phone=request.form["phone"]
        rank=int(request.form["rank"])
        percent=request.form["percent"]
        course=request.form["course"]
        address=request.form["address"]
        students.insert_one({
            "ID":Id,"Name":name,"email":email,"Phone":phone,"Rank":rank,"Percentage":percent,"Course":course,"Address":address
        })
        return redirect("/register")
    else:
        return render_template("register.html")
@app.route("/view",methods=["GET"])
def view_page():
    raw=list(students.find())
    return render_template("view.html",output=raw)
@app.route("/update",methods=["GET","POST"])
def update_page():
    if request.method=="POST":
        Id=int(request.form["id"])
        field=request.form["field"]
        newdata=request.form["newdata"]
        students.update_one({"ID":Id},{"$set":{field:newdata}})
        return redirect("/update")
    else:
        return render_template("update.html")
@app.route("/delete",methods=["GET","POST"])
def delete_page():
    if request.method=="POST":
        Id=int(request.form["id"])
        students.delete_one({"ID":Id})
        return redirect("/delete")
    else:
        return render_template("delete.html")
@app.route("/callme",methods=["GET","POST"])
def call_me():
    if request.method=="POST":
        name=request.form["name"]
        phone=request.form["phone"]
        email=request.form["email"]
        course=request.form["course"]
        callme.insert_one({
            "name":name,"phone":phone,"email":email,"course":course
        })
        return redirect("/")
    else:
        return render_template("index.html")
app.run(debug=True)