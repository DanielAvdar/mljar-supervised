import pandas as pd
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML
from sklearn.datasets import fetch_openml


# df = pd.read_csv(
#    "https://raw.githubusercontent.com/pplonski/datasets-for-start/master/adult/data.csv",
#    skipinitialspace=True,
# )
# X = df[df.columns[:-1]]
# y = (df["income"] == ">50K") * 1

data = fetch_openml(data_id=1590, as_frame=True)
y = (data.target == ">50K") * 1

X = data.data
y = (data.target == ">50K") * 1

sensitive_features = X[["sex", "race"]]  # , "race", "age"]]
print("Input data")
print(X)
print("Sensitive features")
print(sensitive_features)


X_train, X_test, y_train, y_test, S_train, S_test = train_test_split(
    X, y, sensitive_features, stratify=y, test_size=0.3, random_state=42
)


automl = AutoML(algorithms=["Xgboost"])
automl.fit(X_train, y_train, sensitive_features=S_train)
