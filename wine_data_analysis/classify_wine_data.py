from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


class ClassifyWineData:
    def __init__(self, data):
        """Classify wine data using logistic regression, decision tree, and 
        k-nearest neighbors classifiers.
        
        Parameters
        ----------
        data : pandas.core.frame.DataFrame
            The wine dataset containing features and target variables.
            
        Returns
        -------
        None.
        
        """
        x = data.drop(columns=['class'])
        y = data['class']
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=89, random_state=42)

    def __call__(self):
        # predict values with three classification methods
        y_pred_logistic_regression = self.logistic_regression()
        y_pred_decision_tree = self.decision_tree()
        y_pred_knn = self.knn()
        
        # show the classification metrics for logistic regression model
        print('--- Logistic regression classification metrics ---')
        print(f'Accuracy: {self.accuracy(y_pred_logistic_regression):.3f}')
        print(f'Average precision: {self.average_precision(y_pred_logistic_regression):.3f}')
        print(f'Average recall: {self.average_recall(y_pred_logistic_regression):.3f}\n')
        
        # show the classification metrics for decision tree classifier
        print('--- Decision tree classification metrics ---')
        print(f'Accuracy: {self.accuracy(y_pred_decision_tree):.3f}')
        print(f'Average precision: {self.average_precision(y_pred_decision_tree):.3f}')
        print(f'Average recall: {self.average_recall(y_pred_decision_tree):.3f}\n')
        
        # show the classification metrics for KNN regression classifier
        print('--- KNN regression classification metrics ---')
        print(f'Accuracy: {self.accuracy(y_pred_knn):.3f}')
        print(f'Average precision: {self.average_precision(y_pred_knn):.3f}')
        print(f'Average recall: {self.average_recall(y_pred_knn):.3f}')

    def logistic_regression(self):
        """Fit a logistic regression model to the training data and predicts 
        classes for the test data.
        
        Returns
        -------
        y_pred : numpy.ndarray
            Predicted classes for the test data.
            
        """
        # create logistic regression model
        model = LogisticRegression(max_iter=10 ** 4)
        # train model with the train data
        model.fit(self.x_train, self.y_train)
        # predict values for test data
        y_pred = model.predict(self.x_test)
        return y_pred

    def decision_tree(self):
        """Fit a decision tree classifier to the training data and predicts 
        classes for the test data.
        
        Returns
        -------
        y_pred : numpy.ndarray
            Predicted classes for the test data.
            
        """
        # create decision tree classifier 
        model = DecisionTreeClassifier()
        # train model with the train data
        model.fit(self.x_train, self.y_train)
        # predict values for test data
        y_pred = model.predict(self.x_test)
        return y_pred

    def knn(self):
        """Fit a k-nearest neighbors classifier to the training data and 
        predicts classes for the test data.
        
        Returns
        -------
        y_pred : numpy.ndarray
            Predicted classes for the test data.
            
        """
        # create k-nearest neighbors classifier 
        model = KNeighborsClassifier(n_neighbors=7)
        # train model with the train data
        model.fit(self.x_train, self.y_train)
        # predict values for test data
        y_pred = model.predict(self.x_test)
        return y_pred

    def accuracy(self, y_pred):
        """Compute the accuracy of the classifier.
        
        Parameters
        ----------
        y_pred : numpy.ndarray
            Predicted classes for the test data.
        
        Returns
        -------
        acc : float
            Accuracy of the classifier.
            
        """
        # calculate the number of correctly predicted classes
        correct = np.sum(self.y_test == y_pred)
        # calculate the number of the test values
        total = len(self.y_test)
        # calculate the accuracy
        acc = correct / total
        return acc

    def average_precision(self, y_pred):
        """Compute the average precision of the classifier.
        
        Parameters
        ----------
        y_pred : numpy.ndarray
            Predicted classes for the test data.
        
        Returns
        -------
        avg_precision : float
            Average precision of the classifier.
            
        """
        # calculate the number of predicted and true classes
        ind_class_1_true = set(np.where(self.y_test == 1)[0])
        ind_class_1_pred = set(np.where(y_pred == 1)[0])
        ind_class_2_true = set(np.where(self.y_test == 2)[0])
        ind_class_2_pred = set(np.where(y_pred == 2)[0])
        ind_class_3_true = set(np.where(self.y_test == 3)[0])
        ind_class_3_pred = set(np.where(y_pred == 3)[0])
        
        # calculate precisions for every class
        precision_class_1 = len(ind_class_1_true.intersection(ind_class_1_pred)) / len(ind_class_1_pred)
        precision_class_2 = len(ind_class_2_true.intersection(ind_class_2_pred)) / len(ind_class_2_pred)
        precision_class_3 = len(ind_class_3_true.intersection(ind_class_3_pred)) / len(ind_class_3_pred)
        
        # calculate the average precision
        avg_precision = 1 / 3 * (precision_class_1 + precision_class_2 + precision_class_3)
        return avg_precision

    def average_recall(self, y_pred):
        """Compute the average recall of the classifier.
        
        Parameters
        ----------
        y_pred : numpy.ndarray
            Predicted classes for the test data.
        
        Returns
        -------
        avg_recall : float
            Average recall of the classifier.
            
        """
        # calculate the number of predicted and true classes
        ind_class_1_true = set(np.where(self.y_test == 1)[0])
        ind_class_1_pred = set(np.where(y_pred == 1)[0])
        ind_class_2_true = set(np.where(self.y_test == 2)[0])
        ind_class_2_pred = set(np.where(y_pred == 2)[0])
        ind_class_3_true = set(np.where(self.y_test == 3)[0])
        ind_class_3_pred = set(np.where(y_pred == 3)[0])
        
        # calculate recalls for every class
        recall_class_1 = len(ind_class_1_true.intersection(ind_class_1_pred)) / len(ind_class_1_true)
        recall_class_2 = len(ind_class_3_true.intersection(ind_class_2_pred)) / len(ind_class_2_true)
        recall_class_3 = len(ind_class_3_true.intersection(ind_class_3_pred)) / len(ind_class_3_true)
        
        # calculate the average recall
        avg_recall = 1 / 3 * (recall_class_1 + recall_class_2 + recall_class_3)
        return avg_recall
