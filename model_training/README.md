# Model Training and Experiments

This repository contains Jupyter notebooks for training, evaluating, and comparing Continual‑Learning (CL) BERT classifiers and Retrieval‑Augmented Fine‑Tuning (RAFT) models on a temporal fake‑news detection task. Each notebook corresponds to a specific task that was performed.

---

## Notebook Overview

### 1. `KO_BERT_Baseline+Continual_Models.ipynb`  
  - Loads the Liar2 dataset and splits it into five chronological periods (2007–2015, 2016–17, 2018–19, 2020–21, 2022).  
  - Trains a BERT classifier on the baseline period.  
  - Sequentially fine‑tunes that model on each subsequent period (continual learning).  
 
### 2. `KO_BERT_Continual_Models_vs_RAFT.ipynb`  
  - Performs Continual Learning Update for all time periods
  - Initial RAFT implementation on just baseline period

### 3. `KO_BERT_Continual_Update_Model.ipynb`  
  - Initial Test of investigating Continual Learning Approach to use as baseline
  - Contains one fine-tuning update to a baseline BERT classifier.
 
### 4. `KO_BERT_RAG_Faiss(entailment).ipynb`  
  - Entailment RAFT Model implementation and evaluation of all periods with this RAFT entailment approach

### 5. `KO_BERT_RAG_Faiss(headline+distances).ipynb`  
  - Semantic Similarity RAFT Model implementation and evaluation of all periods with this specific RAFT approach

### 6. `KO_BERT_Testing.ipynb`  
  - Initial Testing of using FakeNewsNet Dataset as our dataset with a BERT classifier

### 7. `LiveData_Experiment_WorldNewsAPI.ipynb`  
  - Testing CL Models and RAFT Models on Live Data

### 8. `Rolling_Window_Experiments(Continual_+_RAG).ipynb`  
  - Rolling Window Evaluation of Continual Learning Models and Semantic Similarity RAFT models for all periods
