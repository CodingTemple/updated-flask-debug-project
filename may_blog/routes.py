from may_blog import app
from flask import render_template, request

# Import for Forms
from may_blog.forms import UserInfoForm, PostForm

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