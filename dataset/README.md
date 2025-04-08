# Fake News Knowledge Obsolescence Dataset

The dataset `Fake_News_KO.csv` is a combination of multiple datasets that we have either explored or plan to use for experiments on combating Knowledge Obsolescence in Fake News Detections. The majority of articles come between 2016 and 2018. We have explored and considered the following datasets:

- **FakeNewsNet Dataset:** Real and Fake News from gossipcop and politifact (fact checking websites). [Original FakeNewsNet Paper](https://arxiv.org/abs/1809.01286)
- **ISOT Fake NewsDataset:** Dataset containing real and fake news from different subject categories. We plan to incorporate this dataset in the future if more data is needed. [ISOT dataset](https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets)
- **NELA:**- We initially planned to use NELA, but after reading the [NELA-2020 paper](https://arxiv.org/pdf/2102.04567), we found the data was created by simply labeling articles as reliable or not depending on the source that made them. We believe this is a flawed approach since unreliable sources can still contain real news at times.
- **Liar2:**- This is the current dataset that we are using that contains real and fake statements/articles from 2007 - 2023. The labels range from 0-5 on a range of false to true. We decided to group the labels 0-2 as False and 3-5 as True.

In order to properly combine these datasets, preprocessing was done to collect dates, drop columns, and format entries appropriately. The specific code to perform these operations can be found in the following python files:

- **`date_scraper_from_url.py`:** Follows news article URLs to obtain dates for articles from FakeNewsNet.
- **`ISOT_FakeNews_preprocessing.py`:** Filters data and removes unecessary columns from the ISOT dataset.
- **`combine_csvs.py`:** Helper file to combine csv's with the Label, Title, Date format to create our overall dataset.

In order to test our models on live data, we have created scripts to both load live fact-check labeled data from the [Google Fact Check Tools Api](https://developers.google.com/fact-check/tools/api/) as well as collecting reputable sources for our retrieveal database from [World News Api](https://worldnewsapi.com/docs/). All scripts and sample data are contained in the liveDataScraping/ folder
- **`WorldNewsAPIFactualData.ipynb`:** Collect relevant headlines and summaries for retrieval database from WorldNewsApi, currently we support BBC news only.
- **`bbc_news_sample_data.csv`:** Sample data collected from WorldNewsAPIFactualData.ipynb.
- **`liveDataGoogleApi.ipynb`:** Collect fact-checked news headlines from the Google Fact Check Tools Api.
- **`google_api_sample_livedata.csv`:** Sample data collected from liveDataGoogleApi.ipynb.



Update:
Note, for initial experimentation, we used `FakeNewsNet_combined.csv`. This is because the labeling for the ISOT dataset is based only on the source of the news rather than the content. When we ran our initial BERT classifier with ISOT data included, we achieved unrealistically high (>95%) accuracies, which we attribute to the unrealistic labels of the data. We switched to `FakeNewsNet_combined.csv` and obtained 84 percent accuracy which you can see from the model_training folder. FakeNewsNet creates labels based on per-article reviews rather than just the credibility of the source.

Update:
We decided to switch datasets once again. We are now using Liar2, which has a broader range of years (2007 - 2023) as well as manually labeled labels which makes the data higher quality. We believe this wider range will better apply to our problem of concept drift/knowledge obsolescence.
  
## Dataset Structure

The combined dataset contains the following columns:

| Column | Description |
| ------ | ----------- |
| **label** | Represents if the data is true (1) or false (0). |
| **title** | The title of the news article. |
| **date**  | The publication date of the article in `YYYY-MM-DD` format. |
  
## Dataset Preview
The following shows some example rows of our dataset.

| label | title                                  | date       |
|-------|----------------------------------------|------------|
| 0     | Donald Trump Sends Out Embarrassing New Year’s Eve Message; This is Disturbing | 2017-12-31 |
| 1     | U.S. senators to issue legislation sanctioning Russia over election interference | 2017-01-09 |
| 1     | Saudi Arabia, U.S. play down reports of curbs on military support  | 2016-12-18 |

## Acknowledgements

```bibtex
@article{shu2018fakenewsnet,
  title={FakeNewsNet: A Data Repository with News Content, Social Context and Dynamic Information for Studying Fake News on Social Media},
  author={Shu, Kai and Mahudeswaran, Deepak and Wang, Suhang and Lee, Dongwon and Liu, Huan},
  journal={arXiv preprint arXiv:1809.01286},
  year={2018}
}

@article{shu2017fake,
  title={Fake News Detection on Social Media: A Data Mining Perspective},
  author={Shu, Kai and Sliva, Amy and Wang, Suhang and Tang, Jiliang and Liu, Huan},
  journal={ACM SIGKDD Explorations Newsletter},
  volume={19},
  number={1},
  pages={22--36},
  year={2017},
  publisher={ACM}
}

@article{shu2017exploiting,
  title={Exploiting Tri-Relationship for Fake News Detection},
  author={Shu, Kai and Wang, Suhang and Liu, Huan},
  journal={arXiv preprint arXiv:1712.07709},
  year={2017}
}

@article{xu2024enhanced,
  author={Xu, Cheng and Kechadi, M-Tahar},
  journal={IEEE Access}, 
  title={An Enhanced Fake News Detection System With Fuzzy Deep Learning}, 
  year={2024},
  volume={12},
  number={},
  pages={88006-88021},
  keywords={Fake news;Fuzzy logic;Benchmark testing;Social networking (online);Deep learning;Task analysis;Natural language processing;Classification algorithms;Deep learning;fuzzy deep learning;fake news;fake news detection;fact-checking;NLP;classification systems;benchmark},
  url={https://doi.org/10.1109/ACCESS.2024.3418340},
  doi={10.1109/ACCESS.2024.3418340}}

@inproceedings{xu2023fuzzy,
   author = {Xu, Cheng and Kechadi, M-Tahar},
   title = {Fuzzy Deep Hybrid Network for Fake News Detection},
   year = {2023},
   isbn = {9798400708916},
   publisher = {Association for Computing Machinery},
   address = {New York, NY, USA},
   url = {https://doi.org/10.1145/3628797.3628971},
   doi = {10.1145/3628797.3628971},
   booktitle = {Proceedings of the 12th International Symposium on Information and Communication Technology},
   pages = {118–125},
   numpages = {8},
   keywords = {Classification Systems, Deep Learning, Hybrid Learning Models, Fuzzy Deep Learning, Fake News Detection},
   location = {<conf-loc>, <city>Ho Chi Minh</city>, <country>Vietnam</country>, </conf-loc>},
   series = {SOICT '23}
}
