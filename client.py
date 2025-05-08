import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QTextEdit
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import requests

class EEGApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧠 Epilepsy Diagnosis & Treatment System")
        self.setStyleSheet("background-color: #1e1e2f; color: white;")
        self.setGeometry(200, 100, 950, 750)

        layout = QVBoxLayout()

        # Title
        title = QLabel("Epilepsy Detection, Localisation & Treatment Suggestion")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setStyleSheet("color: #00bfff;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Upload Button at the top
        upload_btn = QPushButton("Upload EEG Signal")
        upload_btn.setStyleSheet("background-color: #007acc; color: white; font-size: 16px;")
        upload_btn.clicked.connect(self.load_file)
        layout.addWidget(upload_btn)

        # EEG Graph
        self.graph_canvas = FigureCanvas(plt.figure(figsize=(8, 3)))
        layout.addWidget(self.graph_canvas)

        # Output Text
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("background-color: #2e2e3a; color: white; font-size: 15px;")
        layout.addWidget(self.output_text)

        self.setLayout(layout)

    def plot_graph(self, signal):
        self.graph_canvas.figure.clear()
        ax = self.graph_canvas.figure.add_subplot(111)
        ax.plot(signal, color='blue')
        ax.set_title("EEG Signal", color='white')
        ax.tick_params(colors='white')
        ax.set_facecolor("#2e2e3a")
        self.graph_canvas.figure.tight_layout()
        self.graph_canvas.draw()

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open EEG File", "", "Text Files (*.txt)")
        if not file_path:
            return

        try:
            signal = np.loadtxt(file_path)
            self.plot_graph(signal)

            # Detection Call
            with open(file_path, 'rb') as f:
                detection_response = requests.post("http://127.0.0.1:8000/detection/", files={'file': f})
            detection_data = detection_response.json()

            avg_conf = detection_data.get("average_confidence", 0.0)

            individual_confidences = detection_data.get("individual_confidences", [])
            model_names = ["GRU", "LSTM", "RNN", "ANN"]
            model_confidences = dict(zip(model_names, individual_confidences))

            severity_score = avg_conf * 10

            if severity_score < 5:
                result_msg = "<b style='color:green'>No Seizure Detected</b><br><br>"
                localisation_msg = "<b style='color:green'>Localization:</b> Safe<br>"
                suggestion_msg = (
                    "✅ Signal appears normal.<br>"
                    "🧘 No medication is needed at this time.<br>"
                    "📆 Continue routine check-ups and healthy lifestyle."
                )
            else:

                with open(file_path, 'rb') as f:
                    localisation_response = requests.post("http://127.0.0.1:8000/localisation/", files={'file': f})
                localisation_data = localisation_response.json()
                localisation = localisation_data.get("localisation", "")

                if severity_score <= 8:
                    severity_level = "<b style='color:orange'>Mild Severity</b>"
                else:
                    severity_level = "<b style='color:red'>High Severity</b>"

                result_msg = "<b style='color:red'>Seizure Detected</b><br>"
                result_msg += f"{severity_level}<br>"

                if "FOCAL" in localisation.upper():
                    result_msg += "<b style='color:green'>Focal Seizure</b><br>"
                    suggestion_msg = (
                        "⚠️ A focal seizure has been detected.<br><br>"
                        "🧠 Origin in a specific brain region.<br>"
                        "💊 Treatment: Antiepileptic medication (e.g., carbamazepine, lamotrigine).<br>"
                        "🛠️ If drug-resistant: Consider surgery or neurostimulation."
                    )
                else:
                    result_msg += "<b style='color:red'>Non-Focal Seizure</b><br>"
                    suggestion_msg = (
                        "⚠️ A generalized seizure has been detected.<br><br>"
                        "🧠 Affects both brain hemispheres.<br>"
                        "💊 Treatment: Broad-spectrum medications (e.g., valproate, levetiracetam).<br>"
                        "📋 EEG monitoring recommended for detailed analysis."
                    )

                localisation_msg = f"<b style='color:white'>Localization:</b> {localisation}<br>"

            confidence_html = "<b>Model Confidence Scores:</b><br>"
            for model_name, score in model_confidences.items():
                confidence_html += f"🔹 {model_name}: {score * 100:.2f}%<br>"
            confidence_html += f"<br><b>Overall Confidence:</b> {avg_conf * 100:.2f}%<br>"

            html = (
                f"{result_msg}<br>"
                f"{localisation_msg}<br><br>"
                f"{confidence_html}<br>"
                f"<b>Treatment Suggestions:</b><br>{suggestion_msg}"
            )

            self.output_text.setHtml(html)

        except Exception as e:
            self.output_text.setHtml(f"<b>Error:</b><br>{str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = EEGApp()
    win.show()
    sys.exit(app.exec_())
