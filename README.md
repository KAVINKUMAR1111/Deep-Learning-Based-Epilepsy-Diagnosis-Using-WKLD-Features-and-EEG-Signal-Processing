# WKLD-Based Epilepsy Diagnosis System

An AI-powered system for real-time epileptic seizure detection and brain zone localization using EEG signals. This project leverages WKLD-based feature extraction and deep learning models, with a **FastAPI** backend and a **PyQt5** GUI frontend for visualization and treatment suggestion.

---

## 🚀 Features

* Real-time seizure detection from EEG signals
* Focal and non-focal brain region localization
* Dynamic EEG plotting with seizure zone highlighting
* Severity level classification based on model confidence
* Personalized treatment recommendations
* FastAPI backend with multiple deep learning models
* PyQt5-based dark theme GUI

---

## 🧠 Technologies Used

* Python 3.11
* TensorFlow 2.12
* FastAPI
* Keras
* NumPy, SciPy, Matplotlib
* PyQt5
  
---

## ⚙️ How to Run

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/KAVINKUMAR1111/Deep-Learning-Based-Epilepsy-Diagnosis-Using-WKLD-Features-and-EEG-Signal-Processing
cd Deep-Learning-Based-Epilepsy-Diagnosis-Using-WKLD-Features-and-EEG-Signal-Processing
```

### 🔹 Step 2: Setup Python Environment (Python 3.11 Required)

We recommend using a virtual environment:

```bash
python3.11 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### 🔹 Step 3: Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 Step 4: Start the FastAPI Server

```bash
python app.py
```

This will launch the API at: `http://127.0.0.1:8000`

---

### 🔹 Step 5: Run the PyQt5 GUI

Open a new terminal:

```bash
python client.py
```

This GUI will allow you to:

* Upload `.txt` EEG files
* Visualize the filtered EEG waveform
* View real-time seizure prediction and localization
* Get treatment suggestions based on severity

---



## 📜 License

Open Sourced

---

## 🙋‍♂️ Author

**Kavinkumar S**

---

## 📬 Contact / Feedback

Feel free to reach out for contributions, collaborations, or questions!

Gmail : kavin11112003@gmail.com

