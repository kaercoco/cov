from flask import Flask,render_template,request,jsonify
import utils

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")


@app.route("/c1")
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({"confirm":data[0],"suspect":data[1],"heal":data[2],"dead":data[3]})


@app.route("/time")
def get_time():
    return utils.get_time()

@app.route('/ajax',methods=["GET","POST"])
def ajax():
    return '10000'

@app.route('/tem')
def tem():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
