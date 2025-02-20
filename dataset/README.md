# Fake News Knowledge Obsolescence Dataset

The dataset `Fake_News_KO.csv` is a combination of multiple datasets that we have either explored or plan to use for experiments on combating Knowledge Obsolescence in Fake News Detections. The majority of articles come between 2016 and 2018. We have explored and considered the following datasets:

- **FakeNewsNet Dataset:** Real and Fake News from gossipcop and politifact (fact checking websites). [Original FakeNewsNet Paper](https://arxiv.org/abs/1809.01286)
- **ISOT Fake NewsDataset:** Dataset containing real and fake news from different subject categories. We plan to incorporate this dataset in the future if more data is needed. [ISOT dataset](https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets)
- **NELA:**- We initially planned to use NELA, but after reading the [NELA-2020 paper](https://arxiv.org/pdf/2102.04567), we found the data was created by simply labeling articles as reliable or not depending on the source that made them. We believe this is a flawed approach since unreliable sources can still contain real news at times.

In order to properly combine these datasets, preprocessing was done to collect dates, drop columns, and format entries appropriately. The specific code to perform these operations can be found in the following python files:

- **`date_scraper_from_url.py`:** Follows news article URLs to obtain dates for articles from FakeNewsNet.
- **`ISOT_FakeNews_preprocessing.py`:** Filters data and removes unecessary columns from the ISOT dataset.
- **`combine_csvs.py`:** Helper file to combine csv's with the Label, Title, Date format to create our overall dataset.


Update:
Note, for initial experimentation, we used `FakeNewsNet_combined.csv`. This is because the labeling for the ISOT dataset is based only on the source of the news rather than the content. When we ran our initial BERT classifier with ISOT data included, we achieved unrealistically high (>95%) accuracies, which we attribute to the unrealistic labels of the data. We switched to `FakeNewsNet_combined.csv` and obtained 84 percent accuracy which you can see from the model_training folder. FakeNewsNet creates labels based on per-article reviews rather than just the credibility of the source 
  
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
