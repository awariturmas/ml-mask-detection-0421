from fastapi import FastAPI
from utils.io_utils import load_config
from utils.model_utils import load_model, load_vectorizer, predict

config = load_config()
model = load_model(config["paths"]["model"])
vectorizer = load_vectorizer()

app = FastAPI()


@app.get("/")
def read_root():
    return "Up and running"


@app.get("/predict/")
def predict_url(url):
    """Endpoint de previsao

    Args:
        url ([str]): url da imagem

    Returns:
        [dict]: dicionario de previsao
    """
    return predict(url, vectorizer, model)
