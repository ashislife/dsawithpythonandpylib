import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn import tree
import matplotlib.pyplot as plt
# Custom dataset
data = {'Pregnancies': [0, 2, 4, 1, 3, 5, 1, 0, 2, 3], 'Glucose': [85, 140, 160, 120, 150, 99, 130, 100, 110, 180], 'BloodPressure': [66, 70, 80, 75, 90, 60, 72, 85, 76, 88], 'SkinThickness': [29, 35, 0, 25, 32, 28, 30, 27, 31, 36], 'Insulin': [0, 130, 180, 90, 100, 88, 140, 70, 95, 200], 'BMI': [26.6, 30.1, 35.3, 28.2, 33.0, 27.8, 31.6, 29.0, 30.4, 37.5], 'DiabetesPedigreeFunction': [0.351, 0.672, 0.872, 0.238, 0.698, 0.543, 0.821, 0.215, 0.544, 1.2], 'Age': [31, 45, 50, 26, 38, 29, 41, 30, 32, 60], 'Outcome': [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]}
df = pd.DataFrame(data)
print(df)
X = df.drop('Outcome', axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
plt.figure(figsize=(10,10))
tree.plot_tree(clf, filled=True, feature_names=X.columns, class_names=['No', 'Yes'])
plt.title("Decision Tree for Custom Diabetes Dataset")
plt.show()