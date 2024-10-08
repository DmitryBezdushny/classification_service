# classification_service

## train model:
1. Put heart.csv to ./data
2. Run the notebook ./notebooks/training_script.ipynb

## build image:
sudo docker build -t classification_service .

## run container:
sudo docker run -it -p 8000:8000 --privileged -v $PWD:/app classification_service

## test the app

### example 1:

request:
```
  curl -X POST http://127.0.0.1:8000/predict \
      -H "Content-Type: application/json" \
      -d '{
            "age": 37,
            "sex": 0,
            "cp": 0,
            "trestbps": 112,
            "chol": 149,
            "fbs": 0,
            "restecg": 1,
            "thalach": 125,
            "exang": 0,
            "oldpeak": 1.6,
            "slope": 1,
            "ca": 0,
            "thal": 2
          }'
```
response:
```{"score":1.0}```

### example 2:

request:
```
curl -X POST http://127.0.0.1:8000/predict \
    -H "Content-Type: application/json" \
    -d '{
          "age": 41,
          "sex": 1,
          "cp": 0,
          "trestbps": 110,
          "chol": 172,
          "fbs": 0,
          "restecg": 0,
          "thalach": 158,
          "exang": 0,
          "oldpeak": 0.0,
          "slope": 2,
          "ca": 0,
          "thal": 3
        }'
```
response:
```{"score":0.0}```