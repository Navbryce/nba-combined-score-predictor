import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

def read_csv_and_get_inputs_and_labels(path, label_column="ttl_pts"):
    df = pd.read_csv(path)
    input = df.loc[:, df.columns != label_column]
    labels = df[[label_column]]
    return input, labels.to_numpy()[:, 0]


def read_csv_and_get_inputs_and_labels_classification(path, label_column="ttl_pts", points_width=10):
    df = pd.read_csv(path)
    input = df.loc[:, df.columns != label_column]
    labels = df[[label_column]]
    categories = np.floor((labels.to_numpy()[:, 0])/points_width).astype(np.int)
    return input, categories


def test_model(model, train, test):
    train_inputs, train_labels = train
    test_inputs, test_labels = test
    model.fit(train_inputs, train_labels)
    train_score = model.score(train_inputs, train_labels)
    train_msqe = mean_squared_error(train_labels, model.predict(train_inputs))
    test_score = model.score(test_inputs, test_labels)
    test_predictions = model.predict(test_inputs)
    test_msqe = mean_squared_error(test_labels, test_predictions)
    return (train_score, train_msqe**.5), (test_score, test_msqe**.5), test_predictions


def test_model_classification(model, train, test):
    train_inputs, train_labels = train
    test_inputs, test_labels = test
    model.fit(train_inputs, train_labels)
    train_accuracy = model.score(train_inputs, train_labels)
    test_accuracy = model.score(test_inputs, test_labels)
    test_predictions = model.predict(test_inputs)

    return train_accuracy, test_accuracy, test_predictions
