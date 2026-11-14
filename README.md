# Machine Learning Portfolio
### Fintan McCamley | 23385751

# Table of Contents

## Notebooks
1. [**Dataset Audit**](./notebooks/dataset_audit.ipynb)
2. [**Preprocessing and Baseline**](./notebooks/preprocessing.ipynb)
3. [**Model Evaluation**](./notebooks/models.ipynb)

## [Data Source](./data/README.md)

# AI usage declaration
Generative AI models such as **Google Gemini** and **Github Copilot** were used while creating this portfolio for the following reasons:

- Explaining Machine learning concepts
- Explaining the scikitlearn and pandas python libraries
- Explaining python errors

Any code written by AI tools was studied and rewritten by myself to ensure that I learn the machine learning process effectively.

No markdown or notes were written using AI tools.

# Get Started

## 1. Start a virtual environment

Open a terminal in the root directory and run the following

```powershell
python -m venv FMC_ML_Portfolio
```
### or
```powershell
uv venv
```

## 2. Install dependancies

```powershell
pip install -r requirements.txt
```
### or
```powershell
uv pip install -r requirements.txt
```

## 3. [**Open the first Notebook**](./notebooks/dataset_audit.ipynb)
Use **jupyter notebook** however you find convenient.

### Terminal
```powershell
jupyter notebook
```
or through **VS Code**, or any other method.

It is recommended to run all cells before reading.

# Tweak

Environment variables are stored in [.env](.env)

### You may change
```powershell
Random_State=42 # Random seed for model evaluation
Test_Size=0.30 # Proportion of dataset to hold for testing
```

**N.B.** Restart the python kernal upon any changes to environment variables
