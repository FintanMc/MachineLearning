from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from pandas import DataFrame
import environment

def grid_cross_validation(model, X_train, y_train, param_grid):
    cv_strategy = StratifiedKFold(n_splits=5, shuffle=True, random_state=environment.Random_State)

    cv = GridSearchCV(
        model, 
        param_grid, 
        cv=cv_strategy, 
        scoring="f1",
        return_train_score=True,
        refit = "f1"
    )

    cv.fit(X_train, y_train)
    
    return [
        cv,
        cv.best_estimator_.fit(X_train, y_train),
        DataFrame([cv.best_params_], index=["Best Parameter"]).T.rename(mapper=lambda x: x.split("__")[-1])
    ]