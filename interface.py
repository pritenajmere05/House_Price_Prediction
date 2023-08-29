from flask import Flask , request , render_template
from utils import get_predicted_price
import config
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_price' , methods = ['POST'])
def predict():

    data = request.form
    area = float(data['Area'])
    bedrooms = float(data['Bedrooms'])
    bathrooms = float(data['Bathrooms'])
    stories = float(data['Stories'])
    mainroad = data['Main_Road_Connectivity']
    guestroom = data['Guestroom']
    basement = data['Basement']
    hotwaterheating = data['Hot_Water_heating']
    airconditioning = data['Airconditioning']
    parking = int(data['Parking'])
    prefarea = data['Preffered_Area']
    furnishingstatus = data['Furnishing']

    predict_price = get_predicted_price(area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,
                                        hotwaterheating,airconditioning,parking,prefarea,furnishingstatus)
    
    return render_template('index.html',final_price = np.ceil(predict_price))

if __name__== '__main__':
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)