# training the models and all other function calls will be here
# this file will be integrated to the django server
from .dataPreprocessing import load_data, preprocessData
from .train_model import train
from rest_framework.response import Response
from rest_framework import status

def startMachine():
    data_dir = 'D:/DjangoProjects/HealthHQ/healthify/MLmodels/data/train'
    preprocessData(data_dir)
    train()

    return Response({'message': 'Machine loaded and preprocessed'}, status=status.HTTP_201_CREATED)
