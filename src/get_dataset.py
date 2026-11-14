def get_dataset():
    import pandas as pd
    from pathlib import Path
    import environment

    Teen_Mental_Health_Dataset = pd.read_csv(Path(Path.cwd().parent / environment.Dataset_PATH))
    return Teen_Mental_Health_Dataset