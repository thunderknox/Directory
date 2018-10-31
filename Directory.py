from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
        return render_template ('index.html',title="Home" )

@app.route('/about')
def about():
        return render_template('about.html', title="About")


@app.route('/maindirectory')
def maindirectory():
        return render_template('maindirectory.html', title="Maindirectory")

        
@app.route('/nustyle')
def nustyle():
	return render_template('nustyle.html')

@app.route('/oldschool')
def oldschool():
	return render_template('oldschool.html')

@app.route('/euphoric')
def euphoric(): 
	return render_template('euphoric.html')

@app.route('/rawstyle')
def rawstyle():
	return render_template('rawstyle.html')







if __name__ == "__main__": 
    app.run(host='0.0.0.0', debug=True)
