import pandas as pd
from sklearn.metrics import accuracy_score, f1_score
import joblib


def evaluate_model(data_path, model_path):
    df = pd.read_csv(data_path)
    model = joblib.load(model_path)

    texts = df['text'].tolist()
    true_labels = df['label'].tolist()

    preds = model(texts)
    pred_labels = [pred['label'] for pred in preds]

    accuracy = accuracy_score(true_labels, pred_labels)
    f1 = f1_score(true_labels, pred_labels, average='weighted')

    metrics = {
        'accuracy': accuracy,
        'f1_score': f1
    }

    print(metrics.get(accuracy))
    print(metrics.get(f1_score))


if __name__ == "__main__":
    evaluate_model('data/processed/data.csv', 'model/model.joblib')
