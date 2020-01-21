from flask import Flask, request, jsonify, render_template, redirect, url_for
import utils

# Load the model
util = utils.FlaskUtil()
# Elasticbeanstalk looks for 'application' file to start the service by default.
application = Flask(__name__)

@application.route("/")
def home():
    return render_template("index.html")

@application.route('/result', methods=['POST','GET'])
def my_form_post():

    text = util.get_data(request)
    #print(text)
    if text is not None:
        result = util.predictions(text)
        #print(result)
        response = jsonify(result)

    else:
        response = jsonify("Wrong input format")

    response.status_code = 200

    # return redirect(url_for('result'), message='')
    return render_template("result.html",prediction=result['prediction'], confidence=result['confidence'])
    # return response


if __name__ == "__main__":
    application.run( threaded=True,debug=True)