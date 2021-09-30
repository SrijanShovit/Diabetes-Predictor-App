from flask import Flask,render_template,request
import pickle
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if (request.method == 'POST'):
        FS = int(request.form['FS'])
        FU = int(request.form['FU'])
        with open('my_model','rb') as f:
            model = pickle.load(f)
        result = model.predict([[FS,FU]])
        if result[0] == 1:
            return render_template('home.html',data=["😣 You might be a diabetes patient","red"])
        else:
            return render_template('home.html',data=["🥳 You don't have diabetes","green"])
    else:
        return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile/<string:name>')
def profile(name):
    return "Hello"+str(name)

@app.route('/profile/<int:id>')
def profile2(id):
    return "id"+str(id)

@app.route('/predict',methods=['POST']) 
def submit():
    if (request.method == 'POST'):
        FS = int(request.form['FS'])
        FU = int(request.form['FU'])
        with open('my_model','rb') as f:
            model = pickle.load(f)
        result = model.predict([[FS,FU]])
        if result[0] == 1:
            return "You might be a diabetes patient"
        else:
            return "You don't have diabetes"
    else:
        return "Something went wrong"



if __name__ == '__main__':
    app.run(debug=True)