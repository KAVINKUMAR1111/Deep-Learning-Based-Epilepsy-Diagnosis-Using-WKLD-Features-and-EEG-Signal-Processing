# Deep-Learning-Based-Epilepsy-Diagnosis-Using-WKLD-Features-and-EEG-Signal-Processing

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

## 📁 Project Structure

```
├── backend/
│   ├── main.py                # FastAPI server
│   ├── model_loader.py        # Model handling logic
│   ├── requirements.txt       # Backend dependencies
│   └── models/                # Trained .h5 and .hdf5 model files
│
├── frontend/
│   ├── gui_app.py             # PyQt5 GUI entry point
│   └── assets/                # Fonts, icons, etc.
│
├── README.md
└── .gitignore
```

---

## ⚙️ How to Run

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/wkld-epilepsy-diagnosis.git
cd wkld-epilepsy-diagnosis
```

### 🔹 Step 2: Setup Python Environment (Python 3.11 Required)

We recommend using a virtual environment:

```bash
python3.11 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### 🔹 Step 3: Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

> 📌 Make sure your `requirements.txt` includes:

```
tensorflow==2.12.0
fastapi
uvicorn
numpy
scipy
keras
```

### 🔹 Step 4: Start the FastAPI Server

```bash
uvicorn main:app --reload
```

This will launch the API at: `http://127.0.0.1:8000`

---

### 🔹 Step 5: Run the PyQt5 GUI

Open a new terminal:

```bash
cd frontend
python gui_app.py
```

This GUI will allow you to:

* Upload `.txt` EEG files
* Visualize the filtered EEG waveform
* View real-time seizure prediction and localization
* Get treatment suggestions based on severity

---

## ✅ Requirements

* Python 3.11 only
* TensorFlow 2.12 only

---

## 📷 Screenshots

*Add screenshots of the GUI here if needed*

---

## 📜 License

MIT License

---

## 🙋‍♂️ Author

**Kavinkumar S**

---

## 📬 Contact / Feedback

Feel free to reach out for contributions, collaborations, or questions!
