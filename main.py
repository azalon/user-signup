from flask import Flask, request, redirect
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["GET"])
def index():
    template = jinja_env.get_template('homepage.html')
    return template.render()

@app.route("/submit", methods=["POST"])
def submit():
    has_errors = False
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']
    email_error_1 = ""
    email_error_2 = ""
    email_error_3 = ""
    email_error_4 = ""
    username_error_1 = ""
    username_error_2 = ""
    username_error_3 = ""
    username_error_4 = ""

    password_error = ""
    password_blank = ""
    password_confirmation_blank = ""
    username_blank = ""
    if email: 
        if len(email) < 3 or len(email) > 20:
            has_errors = True
            email_error_1 = "Your email needs to be between 3 and 20 characters."
            
        if "@" not in email:
            has_errors = True
            email_error_2 = "Your email must contain @."

        periods = 0
        for char in email:
            if char == ".":
                periods += 1 
        if periods > 1:
            has_errors = True
            email_error_3 = "Your email can only have one period."

            
        spaces = 0
        for char in email:
            if char == " ":
                spaces += 1
        if spaces > 0:
            has_errors = True
            email_error_4 = "Your email can't have any spaces."

    if username: 
        if len(username) < 3 or len(username) > 20:
            has_errors = True
            username_error_1 = "Your email needs to be between 3 and 20 characters."
            
        if "@" not in username:
            has_errors = True
            username_error_2 = "Your email must contain @."

        periods = 0
        for char in username:
            if char == ".":
                periods += 1 
        if periods > 1:
            has_errors = True
            username_error_3 = "Your email can only have one period."

            
        spaces = 0
        for char in username:
            if char == " ":
                spaces += 1
        if spaces > 0:
            has_errors = True
            username_error_4 = "Your email can't have any spaces."        

    if password != password_confirmation:
        has_errors = True
        password_error = "Your passwords do not match."  
              
              
    
    required_error = "The {0} cannot be left blank."
      
    
   
    if username == "":
        has_errors = True
        username_blank = required_error.format("username")
    if password == "":
        has_errors = True
        password_blank = required_error.format("password")  
    if password_confirmation == "":
        has_errors = True
        password_confirmation_blank = required_error.format("password confirmation")

    


    template = jinja_env.get_template('homepage.html')
    if has_errors == True:
        password = ""
        password_confirmation = ""   
        
        return template.render(username=username, password=password, password_confirmation=password_confirmation,
    email=email, password_error=password_error, password_confirmation_blank=password_confirmation_blank, password_blank=password_blank, username_blank=username_blank, 
    email_error_1=email_error_1, email_error_2=email_error_2, email_error_3=email_error_3, email_error_4=email_error_4, 
    username_error_1=username_error_1, username_error_2=username_error_2,  username_error_3=username_error_3,  username_error_4=username_error_4,)
    else:
        return redirect('/welcome?username={0}'.format(username))

@app.route("/welcome", methods=["GET"])
def welcome():
    username = request.args.get('username')
    template = jinja_env.get_template('welcomepage.html')
    return template.render(username=username)


app.run()







          


