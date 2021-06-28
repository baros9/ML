import flask
from flask import Flask, jsonify
from flask import request, url_for, render_template
import joblib as jb
import pickle
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)
cors = CORS(app, resources  = {
    r"/*" : {
        "origins" : "*"
    }
}

)

# main index page route
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['GET', 'POST'])
def predict():
    print('beuz')
    model = jb.load(open('model_RF.joblib', 'rb'))
    
     #print(model)
    if request.args['Airtight'] == '' or request.args['Relative_Humidity'] == '' or request.args['Vapor_pressure_deficit'] == '' or request.args['Specific_humidity'] == ''  or request.args['Specific_humidity']== '' or request.args['Water_vapor_concentration'] == '' or request.args['Vapor_pressure'] == '' or request.args['Temperature_dew_point'] == '' or request.args['Saturation_vapor_pressure'] == '' or request.args['Temperature_in_Kelvin'] == '' :
         return "Veuillez remplire la formulaire"
    else:
        predict_weather = model.predict([[float(request.args['Airtight']),
                                float(request.args['Relative_Humidity']),
                                float(request.args['Vapor_pressure_deficit']),
                                float(request.args['Specific_humidity']),
                                float(request.args['Water_vapor_concentration']),
                                float(request.args['Vapor_pressure']),
                                float(request.args['Temperature_dew_point']),
                                float(request.args['Saturation_vapor_pressure']),
                                float(request.args['Temperature_in_Kelvin']),
                                
                                ]])
            #print(request.args['Temperature_in_Kelvin'])
        output =  str(round(predict_weather[0],2))
            #return int(12.0)
        return output + ' ' + '°C'



if __name__ == "__main__":
    app.run(debug=True)
    #predict()
# from flask import Flask#create an instance of Flask
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return render_template('index.html')
# if __name__ == '__main__':
#     app.run(debug=True)

