from flask import Flask, flash, render_template, request

app = Flask(__name__)

@app.route('/')
def index_view():
    print('request:', request.method)
    # flash('Request Success.', 'success')
    context = {
        'name': 'sagar',
        'surname': 'bartaula',
    }
    return render_template('home/index.html', **context)


@app.route('/register')
def register_view():
    print(request)
    return render_template('auth/register.html')

if __name__ == '__main__': app.run(debug=True)