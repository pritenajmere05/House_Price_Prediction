import pickle
import json
import numpy as np
import config

with open(config.JSON_PATH,'r') as f:
    data = json.load(f)

with open(config.PICKLE_PATH,'rb') as f:
    model = pickle.load(f)

def get_predicted_price(area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,
                        airconditioning,parking,prefarea,furnishingstatus):
    dict1 = {'yes':1 , 'no':0}
    dict2 = {'furnished':2 , 'semi-furnished':1 , 'unfurnished':0}
    test_array = np.zeros([1,12])
    test_array[0,0] = area
    test_array[0,1] = bedrooms
    test_array[0,2] = bathrooms
    test_array[0,3] = stories
    test_array[0,4] = dict1[mainroad]
    test_array[0,5] = dict1[guestroom]
    test_array[0,6] = dict1[basement]
    test_array[0,7] = dict1[hotwaterheating]
    test_array[0,8] = dict1[airconditioning]
    test_array[0,9] = parking
    test_array[0,10] = dict1[prefarea]
    test_array[0,11] = dict2[furnishingstatus]

    predict = model.predict(test_array)

    return predict