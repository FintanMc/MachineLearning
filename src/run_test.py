def run_test(model, splits):
    X_train, X_test, y_train, y_test = splits

    from sklearn.metrics import classification_report, confusion_matrix
    import pandas as pd

    import environment
    predictions = model.predict(X_test)

    cm = pd.DataFrame(confusion_matrix(y_test, predictions), index=environment.Target_Labels, columns=environment.Target_Labels).style.set_caption("Confusion Matrix")
    cr = "Classification Report\n" + classification_report(y_test, predictions, zero_division=0, target_names=environment.Target_Labels)

    return [cm, cr]