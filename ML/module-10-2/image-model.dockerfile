FROM tensorflow/serving:2.7.0

COPY clothing-model /models/dapper-model/1
ENV MODEL_NAME="dapper-model"
