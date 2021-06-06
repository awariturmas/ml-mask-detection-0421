# Detecção de Máscaras com Machine Learning
==============================

## Roadmap para Deploy na GCP

1. Build da Docker Image
```bash
# Faz o build as imagens do app e frontend
$ sudo docker-compose -f api/docker-compose.yml build
```

2. Autenticar na GCP
```bash
# Login na GCP Account
$ gcloud auth login --no-launch-browser
# Configura projeto principal
$ gcloud config set project <PROJECT_ID>
# Permite o acesso ao Google Container Registry
$ gcloud auth configure-docker
```

3. Cria a tag do container no GCR
```bash
# Configura a tag dentro do container registry
$ sudo docker tag api_fastapi gcr.io/<PROJECT_ID>/fastapi
# Faz o push da imagem no GCR
$ sudo docker push gcr.io/<PROJECT_ID>/fastapi
```

4. Deploy dentro do Cloud Run
```bash
$ gcloud run deploy fastapi \
  --image gcr.io/awari-mask-cloudrun/fastapi \
  --platform managed \
  --allow-unauthenticated \
  --memory '2G'
```
