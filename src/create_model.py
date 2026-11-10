def create_model(model):
    from sklearn.pipeline import make_pipeline
    from preprocessor import preprocessor

    pipeline = make_pipeline(preprocessor, model)
    
    return pipeline