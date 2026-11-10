from pathlib import Path
import environment

def get_data_splits():
    from sklearn.model_selection import train_test_split

    import pandas as pd
    Teen_Mental_Health_Dataset = pd.read_csv(Path(Path.cwd().parent / environment.Dataset_PATH));

    target = environment.Target

    X = Teen_Mental_Health_Dataset.drop(columns=[target])
    y = Teen_Mental_Health_Dataset[target]

    return train_test_split(X, y, test_size=environment.Test_Size, random_state=environment.Random_State)

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    print(get_data_splits())