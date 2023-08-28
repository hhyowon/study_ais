texture_mean = float(input('texture_mean: '))
perimeter_mean = float(input('perimeter_mean: '))

import pickle

with open('datasets/BreastCancerWisconsin_Regression.pki','rb') as regression_file : # /datasets 안쓴 이유 : 최상위경로가 아니라 현재 vscode 코드경로 따라가서
    loaded_model = pickle.load(regression_file)
    input_lables = [[texture_mean, perimeter_mean]]  # 학습했던 설명변수 형식 
    result_predict = loaded_model.predict(input_lables)
    print('Predict radius_mean Result : {}'.format(result_predict))
    pass