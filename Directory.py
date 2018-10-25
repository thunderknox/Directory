from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
        return render_template ('index.html', my_string="Wheee", my_list=[0,1,2,3,4,5])


@app.route('/about')
def about():
        return render_template('about.html')


@app.route('/maindirectory')
def maindirectory():
        return render_template('maindirectory')

        







if __name__ == "__main__": 
    app.run(host='0.0.0.0', debug=True)
