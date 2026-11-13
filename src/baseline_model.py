from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import environment
from preprocessor import preprocessor

baseline_model = make_pipeline(preprocessor, LogisticRegression(max_iter=1000, random_state=environment.Random_State))