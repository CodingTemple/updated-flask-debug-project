from may_blog import app, db, Message, mail
from flask import render_template, request

# Import for Forms
from may_blog.forms import UserInfoForm, PostForm

# Import for Models
from may_blog.models import User, Post


# Home Route
@app.route('/')
def home():
    customer_name = "Joel"
    order_number = 1
    item_dict = {1:"Ice Cream", 2:"Bread", 3:"Lemons",4:"Cereal"}
    return render_template("home.html", customer_name = customer_name, order_number = order_number, item_dict = item_dict)

# Register Route
@app.route('/register', methods=['GET','POST'])
def register():
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        # Get Information
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n",username,password,email)
        # Create an instance of User
        user = User(username,email,password)
        # Open and insert into database
        db.session.add(user)
        # Save info into database
        db.session.commit()

        # Flask Email Sender 
        msg = Message(f'Thanks for Signing Up! {email}', recipients=email)
        msg.body = ('Congrats on signing up! Looking forward to your posts!')
        msg.html = ('<h1> Welcome to May_Blog!</h1>' '<p> This will be fun! </p>')

        mail.send(msg)
    return render_template('register.html',form = form)

# Post Submission Route
@app.route('/posts', methods=['GET','POST'])
def posts():
    post = PostForm()
    if request.method == 'POST' and post.validate():
        title = post.title.data
        content = post.content.data
        print('\n',title,content)
    return render_template('posts.html', post = post)