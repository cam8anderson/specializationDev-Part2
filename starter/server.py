from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, add_cupcake_dictionary, cupcake_search, delete_one_cupcake 


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', cupcakes = get_cupcakes('cupcakes.csv'))

@app.route('/cupcakes')
def all_cupcakes():
    return render_template('cupcakes.html', cupcakes = get_cupcakes('cupcakes.csv'))

@app.route('/cupcake_individual/<name>')
def individual_cupcakes(name):
    cupcake = cupcake_search('cupcakes.csv', name)
    
    if cupcake:

        return render_template('cupcake_individual.html', cupcake=cupcake)
    else:
        return "Cupcake not found"

@app.route('/order')
def order():
    return render_template('order.html', cupcakes = get_cupcakes('current_order.csv'))

@app.route('/add_cupcake/<name>')
def add_cupcake(name):
    cupcake = cupcake_search('cupcakes.csv', name)

    if cupcake:
        add_cupcake_dictionary('current_order.csv', cupcake)
        return redirect(url_for('home'))
    else:
        return "this cupcake doesn't exist" 
    
@app.route('/delete_cupcake/<name>')
def delete_cupcake(name):
    cupcake = cupcake_search('current_order.csv', name)

    if cupcake:
        delete_one_cupcake('current_order.csv', name)
        return redirect(url_for('order'))
    else:
        return "this cupcake doesn't exist" 

if __name__ == "__main__":
    app.env = 'development'
    app.run(debug=True, port=8000, host='localhost')
#finished part 4 finish part 5