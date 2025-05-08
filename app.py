from fastapi import FastAPI, UploadFile, File, HTTPException
from scipy.signal import butter, filtfilt
from keras.models import load_model
import numpy as np
import io
import uvicorn

app = FastAPI()


localisation_model = load_model('/home/spider/Downloads/Epilepsy_Detection_and_Localization_using_Deep_Learning_Techniques-main/localiser_model.h5')

model_paths = {
    "gru": '/home/spider/Downloads/Epilepsy_Detection_and_Localization_using_Deep_Learning_Techniques-main/best_gru_model.hdf5', #gated reccurent units
    "lstm": '/home/spider/Downloads/Epilepsy_Detection_and_Localization_using_Deep_Learning_Techniques-main/best_lstm_model.hdf5', # long short term memmory
    "rnn": '/home/spider/Downloads/Epilepsy_Detection_and_Localization_using_Deep_Learning_Techniques-main/best_rnn_model.hdf5', # reccurent nural network
    "deeplearning": '/home/spider/Downloads/Epilepsy_Detection_and_Localization_using_Deep_Learning_Techniques-main/detection_model.h5' #ANN
}


detection_models = {name: load_model(path) for name, path in model_paths.items()}

lowcut = 0.5
highcut = 85
fs = 173.61
order = 5
nyquist = 0.5 * fs
low = lowcut / nyquist
high = highcut / nyquist
b, a = butter(order, [low, high], btype='band')

expected_shapes = {
    "gru": (1, 23, 178),
    "lstm": (1, 23, 178),
    "rnn": (1, 23, 178),
    "deeplearning": (1, 4097, 1),
}

def reshape_for_model(signal, shape, model_name=""):
    try:
        if shape == (1, 23, 178):
            return signal[:23*178].reshape(1, 23, 178)
        elif shape == (1, 4097, 1):
            return signal[:4097].reshape(1, 4097, 1)

        else:
            raise ValueError(f"Unsupported shape {shape} for model {model_name}")
    except Exception as e:
        raise ValueError(f"Reshape failed for model {model_name}: {e}")

def process_signal(file: UploadFile):
    contents = file.file.read()
    signal = np.loadtxt(io.StringIO(contents.decode()))
    filtered = filtfilt(b, a, signal)
    return filtered

@app.post("/detection/")
async def detection(file: UploadFile = File(...)):
    try:
        signal = process_signal(file)
        predictions = []

        for name, model in detection_models.items():
            expected_shape = expected_shapes[name]
            reshaped = reshape_for_model(signal, expected_shape, name)
            pred = float(model.predict(reshaped)[0][0])
            predictions.append(pred)

        average_confidence = float(np.mean(predictions))
        prediction_str = "SEIZURE DETECTED" if average_confidence >= 0.5 else "NO SEIZURE DETECTED"
        return {
            "detection": prediction_str,
            "average_confidence": round(average_confidence, 4),
            "individual_confidences": [round(p, 4) for p in predictions]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/localisation/")
async def localisation(file: UploadFile = File(...)):
    try:
        signal = process_signal(file)
        reshaped = signal.reshape(1, len(signal), 1)
        prediction = localisation_model.predict(reshaped)
        prediction_str = "FOCAL SIGNAL" if int(round(prediction[0][0])) == 0 else "NON-FOCAL SIGNAL"
        return {"localisation": prediction_str}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)

