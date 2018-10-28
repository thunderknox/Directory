from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
        return render_template ('index.html',title="Index" )

@app.route('/about')
def about():
        return render_template('about.html', title="About")


@app.route('/maindirectory')
def maindirectory():
        return render_template('maindirectory.html', title="Maindirectory")

        







if __name__ == "__main__": 
    app.run(host='0.0.0.0', debug=True)
