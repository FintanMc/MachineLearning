import environment
from get_dataset import get_dataset

def get_data_splits():
    from sklearn.model_selection import train_test_split

    data = get_dataset()
    target = environment.Target

    X = data.drop(columns=[target])
    y = data[target]

    return train_test_split(X, y, test_size=environment.Test_Size, stratify=y, random_state=environment.Random_State)

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    print(get_data_splits())