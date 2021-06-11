import pickle
from deepfeatx.image import ImageFeatureExtractor


def load_model(path):
    """Funcao que carrega o modelo

    Args:
        path (string): endereço para o modelo

    Returns:
        model: model instance
    """
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model


def load_vectorizer():
    """Carrega o vetorizador de imagens

    Returns:
        model: model instance
    """
    return ImageFeatureExtractor()


def _vectorize(vectorizer, url):
    """Funcao auxiliar que recebe o vetorizador e a url de uma imagem e vetoriza essa imagem.

    Args:
        vectorizer (model.instance]): Instancia do vetorizador
        url (str): url para uma imagem

    Returns:
        [np.array]: feature vector da imagem
    """
    return vectorizer.url_to_vector(url)


def predict(url, vectorizer, model):
    """Funcao de previsao

    Args:
        url (string): url da imagem
        vectorizer (model.instance): vetorizador
        model (mode.istance): modelo de previsao com ou sem mascara

    Returns:
        dict: dicionario de previsao
    """
    decoder = model.classes_
    vector = _vectorize(vectorizer, url)
    probas = model.predict_proba(vector)
    idx = probas.argmax()
    predicted_class = decoder[idx]
    predicted_confidence = probas[0][idx]
    return {
        "url": url,
        "predicted_class": predicted_class,
        "predicted_confidence": predicted_confidence,
    }
