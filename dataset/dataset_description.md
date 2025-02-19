# Fake News Knowledge Obsolescence Dataset

The dataset `Fake_News_KO.csv` is a combination of multiple datasets that we use for experiments on combating Knowledge Obsolescence in Fake News Detections. The majority of articles come between 2016 and 2018. This dataset, specifically combines two sources:

- **ISOT Fake NewsDataset:** Dataset containing real and fake news from different subject categories.
- **FakeNewsNet Dataset:** Real and Fake News from gossipcop and politifact (fact checking websites)

In order to properly combine these datasets, preprocessing was done to collect dates, drop columns, and format entries appropriately. The specific code to perform these operations can be found in the following python files:

- **`date_scraper_from_url.py`:** Follows news article URLs to obtain dates for articles from FakeNewsNet.
- **`ISOT_FakeNews_preprocessing.py`:** Filters data and removes unecessary columns from the ISOT dataset.
- **`combine_csvs.py`:** Helper file to combine csv's with the Label, Title, Date format to create our overall dataset.
  
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
