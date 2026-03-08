from flask_wtf import FlaskForm #wht we use all function in flask form like validator and feild
from wtforms import StringField,EmailField,SubmitField #give the field to input the value
from wtforms.validators import Email,ValidationError,DataRequired  #rules for specific feild
from flask_wtf.file import FileRequired, FileAllowed, FileField  #seaprate module for play with file

class Datainput(FlaskForm) :   #need to extend th flaskform in class
    name = StringField(label="Name" , validators= [DataRequired()])   #get the name from user in name python variable
    email_id = EmailField(label="Enter the email :",validators=[DataRequired(),Email()])  #in email_id python variable # need to download email validator seaprate
    submit= SubmitField("click to send Data and Goto upload") 

class Imageinput(FlaskForm):
    image = FileField(label='Put the image (Here)',validators=[FileRequired(),FileAllowed(['jpg','png','jpeg','gif','webp'],'image only!')])
    submit_img = SubmitField(label="Submit Image")