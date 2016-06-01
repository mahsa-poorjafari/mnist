from django.shortcuts import render
import cPickle, gzip, numpy
from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn import datasets
from nolearn.dbn import DBN
import numpy as np

from django.views.generic import ListView


def index(request):

    print "[X] downloading data..."
    dataset = datasets.fetch_mldata("MNIST Original")
    (trainX, testX, trainY, testY) = train_test_split(
        dataset.data / 255.0, dataset.target.astype("int0"), test_size=0.33)

    dbn = DBN(

        [trainX.shape[1], 300, 10],
        learn_rates=0.3,
        learn_rate_decays=0.9,
        epochs=10,
        verbose=1)
    dbn.fit(trainX, trainY)
    preds = dbn.predict(testX)
    showclassifications = classification_report(testY, preds)
    testlenght = np.random.choice(np.arange(0, len(testY)), size=(10,))
    return render(request, 'index.html', {'dbn': dbn, 'preds': preds, 'showclassifications': showclassifications})
    # return render(request, 'index.html', {'dbn': dbn, 'testlenght': testlenght})


    # return HttpResponse(dataset.data / 255.0)