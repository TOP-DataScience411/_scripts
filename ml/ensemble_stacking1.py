from numpy import array
from pandas import DataFrame, read_csv, Series
from sklearn.linear_model import RidgeClassifier, LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from pathlib import Path
from sys import path


script_dir = Path(path[0])

data = read_csv(
    script_dir / 'sonar.csv',
    names=[f'attr{i}' for i in range(1, 61)] + ['target']
)
data.loc[data['target'] == 'R', 'target'] = 0
data.loc[data['target'] == 'M', 'target'] = 1
data['target'] = data['target'].astype(dtype=int)

x_train, x_test, y_train, y_test = train_test_split(
    data.loc[:, :'attr60'],
    data['target'],
    test_size=0.3,
    random_state=1
)


models_1st_lvl = [
    KNeighborsClassifier(n_neighbors=3),
    RidgeClassifier(),
    DecisionTreeClassifier(max_depth=6),
]
model_2nd_lvl = LogisticRegression()

y_trained_preds_1st_lvl = []
y_preds_1st_lvl = []
models_accuracy = []
for model in models_1st_lvl:
    model.fit(x_train, y_train)
    y_trained_preds_1st_lvl.append(model.predict(x_train))
    q = model.predict(x_test)
    y_preds_1st_lvl.append(q)
    models_accuracy.append(accuracy_score(y_test, q))

y_preds_1st_lvl = DataFrame(
    {
        'knn': y_preds_1st_lvl[0],
        'ridge': y_preds_1st_lvl[1],
        'dec_tree': y_preds_1st_lvl[2],
        # 'target': y_test,
    }
)

model_2nd_lvl.fit(y_preds_1st_lvl, y_test)

y_preds_all_1st_lvl = array(
      array(y_trained_preds_1st_lvl).T.tolist() 
    + y_preds_1st_lvl.values.tolist()
).T
y_preds_all_1st_lvl = DataFrame(
    {
        'knn': y_preds_all_1st_lvl[0],
        'ridge': y_preds_all_1st_lvl[1],
        'dec_tree': y_preds_all_1st_lvl[2],
        # 'target': y_train + y_test,
    }
)

y_preds_all_2nd_lvl = model_2nd_lvl.predict(y_preds_all_1st_lvl)
y_test_all_2nd_lvl = y_train.values.tolist() + y_test.values.tolist()

models_accuracy = Series({
    'knn': models_accuracy[0],
    'ridge': models_accuracy[1],
    'dec_tree': models_accuracy[2],
    'ensemble': accuracy_score(y_test_all_2nd_lvl, y_preds_all_2nd_lvl),
})
print(models_accuracy.round(2))


