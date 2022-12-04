import pickle
import numpy as np

#"././Model/regression_model.sav"
def predict_model(*data,addr):

    model = pickle.load(open(addr,"rb"))
    data = np.array(data).reshape(1,-1)
    return model.predict(data)

