import environment

def grid_cross_validation(model, X_train, y_train, param_grid):
    from sklearn.model_selection import StratifiedKFold
    cv_strategy = StratifiedKFold(n_splits=5, shuffle=True, random_state=environment.Random_State)

    metrics = environment.Metrics

    from sklearn.model_selection import GridSearchCV
    cv = GridSearchCV(
        model, 
        param_grid, 
        cv=cv_strategy, 
        scoring=metrics, 
        return_train_score=True,
        refit = "f1"
    )

    cv.fit(X_train, y_train)

    return cv