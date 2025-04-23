# Combating Knowledge Obsolescence with Explainable RAFT

A retrieval‑augmented fine‑tuning (RAFT) approach built on BERT to detect fake news under concept drift. We compare standard continual‑learning (CL) models against RAFT variants that ground their predictions in up‑to‑date real‑world headlines via FAISS. We also experiment with Live Data, comparing RAFT approaches, and investigate the importance of FAISS Indexes.

[Video presentation](https://www.youtube.com/watch?v=iJRgj5-gUAc) of our project

---

## Running Our Jupyter Notebooks

You can run the jupyter notebooks locally or on Google Colab. We recommend Google Colab for ease of dependency installation. Please set aside a couple hours for each experiment since downloading the files and training models is a time consuming process.

### 1. Clone the repo
```bash
git clone https://github.com/RohitP123/Fake-News-KO.git
```
If running locally, you will need to manually download the dependencies listed at the top of the jupyter notebook you are running

## Demo (on Google Collab)

Below we describe running some of our Jupyter Notebooks to replicate our models and findings.

The dataset csv's required for running the following 3 notebooks are:
- Liar2_combined.csv
  - Found in the datasets folder of the repo
- Kaggle Dataset: [4.5M Headlines 2007-2022[10 Largest Sites]](https://www.kaggle.com/datasets/jordankrishnayah/45m-headlines-from-2007-2022-10-largest-sites/data?select=is_available.csv)
  - Download the headlines.csv from the kaggle dataset page (will be used for retrieval)

### Creating our RAFT Model with Semantic Similarity: KO_BERT_RAG_Faiss(headline + distance).ipynb
1. Download `KO_BERT_RAG_Faiss(headline + distance).ipynb` and upload it to Google Colab.
2. Upload the Liar2 csv dataset to the google colab
3. Select a GPU as runtime type (eg. T4) (you can run on CPU, but we heavily recommend using a GPU as these are compute intesive tasks)
4. Run each cell up until the Faiss Index Creations Step
5. If first time running, you will need to create the Faiss Indexes for retrieval in the RAFT model or you can download the `faiss_indexes_new.zip` and `faiss_headlines_new.pkl` from this [OneDrive](https://gtvault-my.sharepoint.com/:f:/g/personal/rpatil73_gatech_edu/EqOQFqN11yJLt9gyjwH51a4BOELilGgtITOHWIdjZb8JRg?e=soyFko) (If you have Faiss Indexes downloaded, skip to step 6)
    - Ignore the Faiss Index Creation Section
    - In order to create Faiss Indexes, refer to the following file `Enhanced_Faiss_Index.ipynb` located in the Faiss folder [here](https://github.com/RohitP123/Fake-News-KO/blob/main/Faiss/Enhanced_Faiss_Index.ipynb)
      - This jupyter notebook allows for the creation of Faiss Indexes with the enhanced dataset that you downloaded from Kaggle
      - Download and Upload this notebook to google colab
      - Upload `headlines.csv` dataset that you downloaded from Kaggle
      - Run the notebook to create 5 Faiss Indexes that will be used in our 5 RAFT models
      - Download the Faiss Index zip that is created and the faiss_headlines.pkl that is created after execution of this entire notebook
      - proceed to step 6
6. If not first time running, and you have saved the Faiss Indexes
    - First find the code block that defines the search_similar_articles function. Run this code block
    - Then move to the Load Faiss Indexes section
      - Upload the Faiss Indexes Zip from Step 5 as well as the faiss_headlines.pkl
      - Run the 2 cells to load the indexes
7. Now move onto the RAFT models section
8. Run the remaining code blocks to train and evaluate each RAFT model that is trained on a baseline period and fine tuned on future periods
9. After running all cells you will have the new models zipped in colab and can download them if you would like.


### Creating our RAFT Model with Entailment: KO_BERT_RAG_Faiss(entailment).ipynb
1. Same steps as above in terms of data upload and Faiss Index Creations
2. This notebook is a different variant of RAFT that uses Entailment
3. Running the notebook will show classification reports for each entailment RAFT model

### Baseline Continual Learning Models: KO_BERT_Baseline+Continual_Models.ipynb
1. We need a baseline to compare our RAFT models. We can get this baseline by running this file to create our Continual Learning Models which serve as a baseline
2. Simply upload the Liar2_combined.csv to the google colab
3. Run all cells in the notebook
4. Download the Continual Learning Models

### Live Data Experiments: LiveData_Experiment_WorldNewsAPI.ipynb
1. For this notebook we need a different CSV that contains scraped headlines
2. Download the [politifact-sample.csv](https://github.com/RohitP123/Fake-News-KO/blob/main/dataset/liveDataScraping/politifact-sample.csv) and [live_data_retrieval_headlines.csv](https://github.com/RohitP123/Fake-News-KO/blob/main/dataset/liveDataScraping/live_data_retrieval_headlines.csv) from dataset/liveDataScraping in the Repository
    - These are respectively used for the test dataset and the Faiss Index for retrieval
      - To retrieve the Faiss Index, instead of runnning the cell for creating it, you can download `faiss_live_headlines.index` from this [OneDrive](https://gtvault-my.sharepoint.com/my?id=%2Fpersonal%2Frpatil73%5Fgatech%5Fedu%2FDocuments%2FCS6365%2DCombating%20KO%20with%20RAFT).
3. Upload the `LiveData_Experiment_WorldNewsAPI.ipynb` notebook to google colab and upload the two csvs as well
4. Also upload Continual Learning Baseline Period Model, CL period 4 model, and RAFT period 4 model which you may have downloaded from previous notebooks mentioned
5. Run all cells in the notebook
    - These cells include creating the Faiss Index from live_data_retrieval_headlines.csv, and evaluation the 3 uploaded models and generating their classification report on the live data
6. You will see evaluation metrics of the three models uploaded

### Live Data Experiments: Zero-shot LLM Inference 
1. For this notebook we need a different CSV that contains scraped headlines
2. Download the [politifact-sample.csv](https://github.com/RohitP123/Fake-News-KO/blob/main/dataset/liveDataScraping/politifact-sample.csv) and [live_data_retrieval_headlines.csv](https://github.com/RohitP123/Fake-News-KO/blob/main/dataset/liveDataScraping/live_data_retrieval_headlines.csv) from dataset/liveDataScraping in the Repository
    - These are respectively used for the test dataset and the Faiss Index for retrieval
3. Upload the `KO_LLM_Classifier.ipynb` notebook to google colab and upload the two csvs as well
4. Since we load a Llama 3 8B model from hugging face, you must make a [Hugging Face account](https://huggingface.co/) and [request acess to the Llama 3 8b model](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct/discussions/142).
    - Make sure to include "Georgia Tech" as affliation when requesting access to the model via Hugging Face
5. Run all cells in the notebook, feel free to change the prompts to experiment 
