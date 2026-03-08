from flask import Flask,request,render_template,url_for,Response,redirect,session
from form import Datainput,Imageinput  #from form Module import the Datainput class

app =Flask(__name__)
app.secret_key= "project-secreate-key"
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route("/",methods=["POST","GET"]) #this is page firstly open(defult)
def home():  # in that page using from (flask -wtf) we get the data from user 
 obj_Class= Datainput()  
 #creating object (obj_class ) of class Datapoint()
 if obj_Class.validate_on_submit(): 
    name= obj_Class.name.data
    email= obj_Class.email_id.data #geting the email data(email_id(variable of flask) to email (variable of email))
      #to get data mindit the object name

     # Store in session so we can use them on other pages
    session["name"] = name
    session["email"] = email
    
    return redirect(url_for("upload")) #if process of geting data from registration form is done then go to the page("upload")
 
 return render_template("registration.html",form =obj_Class) # first this this is return becuse no any post request is get 
    # IF ANY ERROR IS HAPPEN LIKE 
    #             - Data is incomplete , not write post etc also this run or return Repetedly
 
@app.route("/upload",methods =["POST","GET"])  #GET - to get the user form for image submission\
                                              #POST - to post or send the image to the serve or python backend
def upload():
   image_Obj = Imageinput()   #this is object of class IMageInput from same form module
   name_for_upload_page = session.get["name"]   #get to paste on upload form

   if image_Obj.validate_on_submit():   # validator to chck we get image if not then render on upload page
      iamge_file = image_Obj.image.data      #get the image from form of imageinput in file image_file
      



   



   return render_template("upload.html",name=name_for_upload_page)






@app.route("/result", methods= ["GET","POST"])
def result():
   return render_template("result.html")
   










if __name__=="__main__":
    app.run(debug=True)