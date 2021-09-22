from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv('./learndataedited.csv')
features_train, features_test, target_train, target_test = train_test_split(df.drop(labels='label', axis=1),df['label'] ,test_size =0.25, random_state=0)

""" from sklearn.linear_model import Lasso
Lasso = Lasso(alpha=0.1,random_state=0)
Lasso.fit(features_train.values,target_train.values)
target_pred_Lasso = Lasso.predict(features_test.values)
print(target_pred_Lasso) """

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=5000)
model.fit(features_train.values, target_train.values)

predicted = model.predict(features_test.values)
print(predicted)
print(target_test)