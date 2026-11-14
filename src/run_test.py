from sklearn.metrics import f1_score


def run_test(model, splits):
    X_train, X_test, y_train, y_test = splits

    from sklearn.metrics import classification_report, confusion_matrix
    import pandas as pd

    import environment
    predictions = model.predict(X_test)

    def prefix_labels(prefix):
        return [prefix + " " + label for label in environment.Target_Labels]

    cm = pd.DataFrame(confusion_matrix(y_test, predictions), index=prefix_labels("actual"), columns=prefix_labels("predicted")).style.set_caption("Confusion Matrix")
    cr = "Classification Report\n" + classification_report(y_test, predictions, zero_division=0, target_names=environment.Target_Labels)

    return {
        "confusion_matrix": cm,
        "classification_report": cr,
        "f1_score": f1_score(y_test, predictions),
    }