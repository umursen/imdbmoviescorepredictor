from sklearn.ensemble import RandomForestRegressor
from sklearn import cross_validation
import numpy as np

class RandomForest:

    def __init__(self,X,y):
        self.X = X
        self.y = y

    def divide_dataset(self, independent, dependent, percent=20):
        print('Dividing data as %80 training data and %20 testing data\n')
        ratio = 100/percent
        n = len(independent)/ratio
        return independent[:n], dependent[:n], independent[n:], dependent[n:]

    def accuracy_metric(self, actual, predicted, error_range = 1):
        correct = 0
        for i in range(len(actual)):
            difference = actual[i] - predicted[i]
            if difference < error_range and difference > -error_range:
    			correct += 1
        return correct / float(len(actual)) * 100.0

    def evaluate_algorithm(self, data, regressor):
        return regressor.predict(data)

    def test_performance(self):
        features = self.X
        results = self.y
        # kfcv_regressor_results = self.test_with_kfcv(train_set=features,train_set_values=results)
        dataset_divison_regressor_results = self.test_with_dataset_separation(features,results)

    def test_with_kfcv(self, train_set, train_set_values, n_folds=10, tree_numbers=[10,50,100,200]):
        print('\nTesting with KFCV\n')
        results = []

        for tree_number in tree_numbers:
            cv = cross_validation.KFold(len(train_set), n_folds=n_folds)
            regressor = RandomForestRegressor(n_estimators=tree_number, random_state = 0)

            scores = []

            for train_cv, test_cv in cv:
                probs = regressor.fit(train_set[train_cv], train_set_values[train_cv]).predict(train_set[test_cv])
                scores.append(self.accuracy_metric(probs, train_set_values))

            results.append((tree_number, np.array(scores).mean()))

            print('Tree Number: %d' % tree_number)
            print('Score: %s' % np.array(scores).mean())


    def test_with_dataset_separation(self, X, y, tree_numbers=[10,50,100,200]):

        print('\nEvaluating with data separation\n')

        test_set, test_set_real_values, train_set, train_set_real_values = self.divide_dataset(X,y)
        test_set_length = len(test_set)

        for tree_number in [10,50,100,200]:

            regressor = RandomForestRegressor(n_estimators=tree_number, random_state = 0)
            regressor.fit(train_set, train_set_real_values)

            y_preds = []

            for n in range(test_set_length):
                y_preds.append(regressor.predict([test_set[n]]))

            scores = self.accuracy_metric(y_preds, test_set_real_values)

            print('Trees Number: %d' % tree_number)
            print('Scores: %s' % scores)