from transformers import pipeline
import joblib

def train_model(data_path, model_output_path):
    model = pipeline("sentiment-analysis", model="Aniemore/rubert-tiny2-russian-emotion-detection")
    joblib.dump(model, model_output_path)


if __name__ == "__main__":
    train_model('data/processed/data.csv', 'model/model.joblib')