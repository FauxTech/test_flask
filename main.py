from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# the url_function that we are importing will find exact locations of routs
# for us, we will use it in our layout template

# instantiating Flask object from flask lib
app = Flask(__name__)

# secret key for our application which will protect against modifying cookies
# cross-site requests etc.
app.config['SECRET_KEY'] = '3527bff60b049fc0b17f7f5d36473245'

# dummy data
posts = [
    {
        'author': 'M.Craft',
        'title': 'Sample post',
        'content': 'Some sample string',
        'date_posted': '05/02/2021'
    },
    {
        'author': 'J.Craft',
        'title': 'Some extra stuff',
        'content': 'Another string, get used to it',
        'date_posted': '06/02/2021'
    }
]


# route decorator, handles the backend stuff
# allows us to write a function that will return what will be shown to us
# at this for this route (in this case /  and /home)
@app.route('/')
@app.route('/home')
def home():
    # we are using here render_template function from flask lib
    # this function renders a template that we saved in the template folder
    # in our project
    # with need to specify at least one argument which is the name of the
    # template that we want to render (in this case it's home.html)
    # we can also provide other attributes (in this example we created
    # attribute posts which we assign the value of our dummy data (list of
    # dictionaries we named posts)
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    # in this example we created attribute title to which we assigned
    # the string 'About'
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # method that validates our data after submitting
    if form.validate_on_submit():
        # success in this flash is a category we provide, it will be used
        # to get success class from bootstrap
        # this flash message is a one time alert, goes away after reload
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (form.email.data == 'admin@blog.com'
                and form.password.data == 'password'):
            flash(f'You have logged as {form.email.data}', 'success')
            return redirect(url_for('home'))
        else:
            flash('Wrong login or password!', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    # allows us to run our application (in this case in debug mode)
    app.run(debug=True)
