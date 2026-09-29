# Bharatanatyam Mudra Recognition

This project classifies Bharatanatyam hand mudras from uploaded images using a trained TensorFlow/Keras model.

## Project overview

- Deep learning model for mudra recognition
- Streamlit web app for uploading an image and predicting the mudra
- Training notebook for model experimentation and evaluation
- Pre-trained model files included in the repository

## Repository structure

- `mudra_app/app.py` – Streamlit web application
- `mudra_classifier.keras` – trained Keras model
- `best_cnn.keras` – alternative trained model
- `class_names.json` – mapping of model output indices to mudra names
- `notebook/Exit_Exam_Mudras.ipynb` – training/evaluation notebook
- `requirements.txt` – Python dependencies
- `screenshots/` – project screenshots

## Requirements

- Python 3.9+
- pip
- A working internet connection to install dependencies

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Priya-on-loop/Bharatnatyam_mudras_recognition.git
   cd Bharatnatyam_mudras_recognition
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Verify the model files are present:

   ```bash
   ls
   ```

   You should see files like `mudra_classifier.keras`, `best_cnn.keras`, and `class_names.json`.

## Run the app

From the project root, start the Streamlit app:

```bash
streamlit run mudra_app/app.py
```

Then open the local URL shown in the terminal (typically `http://localhost:8501`).

## How to use

1. Upload an image of a Bharatanatyam mudra.
2. Click the `Predict Mudra` button.
3. The app will display the predicted mudra and confidence score.

## Notes

- This project uses TensorFlow and Keras for image classification.
- The model expects 128x128 RGB images, matching the app's preprocessing logic.
- If you want to retrain or experiment with the notebook, open `notebook/Exit_Exam_Mudras.ipynb` in Jupyter or JupyterLab.

## Troubleshooting

- If TensorFlow installation fails, make sure your Python version is compatible and consider upgrading `pip`.
- If the app cannot find the model, confirm that all `.keras` files and `class_names.json` are present in the project root.
- If Streamlit does not start, run:

  ```bash
  python -m streamlit run mudra_app/app.py
  ```

## License

This repository does not currently include a license file. If you plan to share or reuse the project publicly, consider adding an appropriate open-source license.
