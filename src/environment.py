import os
from dotenv import load_dotenv
load_dotenv()

Dataset_PATH=os.getenv('Dataset_PATH')
Target=os.getenv('Target')
Target_Labels=os.getenv('Target_Labels').split(', ')
Metrics=os.getenv('Metrics').split(', ')
Random_State = int(os.getenv('Random_State'))
Test_Size = float(os.getenv('Test_Size'))