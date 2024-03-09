from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


class ClassifyWineData:
    def __init__(self, data):
        x = data.drop(columns=['class'])
        y = data['class']
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=89, random_state=42)

    def __call__(self):
        y_pred_logistic_regression = self.logistic_regression()
        y_pred_decision_tree = self.decision_tree()
        y_pred_knn = self.knn()
        print('--- Logistic regression classification metrics ---')
        print(f'Accuracy: {self.accuracy(y_pred_logistic_regression):.3f}')
        print(f'Average precision: {self.average_precision(y_pred_logistic_regression):.3f}')
        print(f'Average recall: {self.average_recall(y_pred_logistic_regression):.3f}\n')
        print('--- Decision tree classification metrics ---')
        print(f'Accuracy: {self.accuracy(y_pred_decision_tree):.3f}')
        print(f'Average precision: {self.average_precision(y_pred_decision_tree):.3f}')
        print(f'Average recall: {self.average_recall(y_pred_decision_tree):.3f}\n')
        print('--- KNN regression classification metrics ---')
        print(f'Accuracy: {self.accuracy(y_pred_knn):.3f}')
        print(f'Average precision: {self.average_precision(y_pred_knn):.3f}')
        print(f'Average recall: {self.average_recall(y_pred_knn):.3f}')

    def logistic_regression(self):
        model = LogisticRegression(max_iter=10 ** 4)
        model.fit(self.x_train, self.y_train)
        y_pred = model.predict(self.x_test)
        return y_pred

    def decision_tree(self):
        model = DecisionTreeClassifier()
        model.fit(self.x_train, self.y_train)
        y_pred = model.predict(self.x_test)
        return y_pred

    def knn(self):
        model = KNeighborsClassifier(n_neighbors=7)
        model.fit(self.x_train, self.y_train)
        y_pred = model.predict(self.x_test)
        return y_pred

    def accuracy(self, y_pred):
        correct = np.sum(self.y_test == y_pred)
        total = len(self.y_test)
        return correct / total

    def average_precision(self, y_pred):
        ind_class_1_true = set(np.where(self.y_test == 1)[0])
        ind_class_1_pred = set(np.where(y_pred == 1)[0])
        ind_class_2_true = set(np.where(self.y_test == 2)[0])
        ind_class_2_pred = set(np.where(y_pred == 2)[0])
        ind_class_3_true = set(np.where(self.y_test == 3)[0])
        ind_class_3_pred = set(np.where(y_pred == 3)[0])
        precision_class_1 = len(ind_class_1_true.intersection(ind_class_1_pred)) / len(ind_class_1_pred)
        precision_class_2 = len(ind_class_2_true.intersection(ind_class_2_pred)) / len(ind_class_2_pred)
        precision_class_3 = len(ind_class_3_true.intersection(ind_class_3_pred)) / len(ind_class_3_pred)
        avg_precision = 1 / 3 * (precision_class_1 + precision_class_2 + precision_class_3)
        return avg_precision

    def average_recall(self, y_pred):
        ind_class_1_true = set(np.where(self.y_test == 1)[0])
        ind_class_1_pred = set(np.where(y_pred == 1)[0])
        ind_class_2_true = set(np.where(self.y_test == 2)[0])
        ind_class_2_pred = set(np.where(y_pred == 2)[0])
        ind_class_3_true = set(np.where(self.y_test == 3)[0])
        ind_class_3_pred = set(np.where(y_pred == 3)[0])
        recall_class_1 = len(ind_class_1_true.intersection(ind_class_1_pred)) / len(ind_class_1_true)
        recall_class_2 = len(ind_class_3_true.intersection(ind_class_2_pred)) / len(ind_class_2_true)
        recall_class_3 = len(ind_class_3_true.intersection(ind_class_3_pred)) / len(ind_class_3_true)
        avg_recall = 1 / 3 * (recall_class_1 + recall_class_2 + recall_class_3)
        return avg_recall
