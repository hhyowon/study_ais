radius_se = float(input('radius_se: '))
texture_se = float(input('texture_se: '))
area_se = float(input('area_se: '))

import pickle

with open('datasets/BreastCancerWisconsin_Regression.pki','rb') as regression_file :
    loaded_model = pickle.load(regression_file)
    input_labels = [[radius_se, texture_se, area_se]]  # 학습했던 설명변수 형식 
    result_predict = loaded_model.predict(input_labels)
    print('Predict radius_mean Result : {}'.format(result_predict))
    pass