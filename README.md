# Team HIT Analysis of Hurricane related Tweets

### Purpose
The purpose of this project is to provide insight into hurricane related communication found on Twitter. Tweets related to hurricanes can be classified and examined for patterns relating to the time surrounding the hurricane. 

**Use Case:** *A party interested in the communication on Twitter during a hurricane presents a collection of Tweet ids from known storm periods and asks for insights into how they can better format or structure communication over Twitter by examining trends or patterns in communication during the storm period.* 

### Quick Start
Employing the data handler and notebooks that collect historical data from Twitter requires an [Twitter Developer Academic Research](https://developer.twitter.com/en/products/twitter-api/academic-research) account. Configure a `config.py` file with the account credentials as specified from the developer account.

The `6.EXTENDED_PIPELINE.ipynb` notebook demonstrates the integration of the techniques that we developed to examine hurricane related communication over Twitter. 

### Concept
The project was developed from an [initial labeled dataset](https://crisisnlp.qcri.org/humaid_dataset.html#) used to train a model to classify Tweets as belonging to one of 9 categories:

1. sympathy and support
2. injured or dead people
3. rescue, volunteering or donation efforts
4. infrastructure and utility damage
5. requests or urgent needs
6. caution and advice
7. non-humanitarian aid
8. displaced people and evacuations
9. other relevant information

The initial labeled dataset was from 2016 and 2017.  Additional Tweets relating to hurricanes from the storm seasons going back as far as 2012 were collected from the Twitter API and classified into one of the 9 categories. An additional classifier was trained to distinguish hurricane from non-hurricane related Tweets in order to ensure the integrity of the collection pulled from the API. 

Category 9, "other relevant information", was found to be the largest category across years.  KMeans clustering was used to attempt to break this category down into more granular subcategories, however it was found that any clusters within Category 9 were highly specific to the individual storms in the time period and were not informative to the overall analysis.  

### Methodology
1. To ensure the code used for development functions appropriately create a Python virtual environment by loading the `requirements.txt` file:

```shell
python -m venv hurricane_tweets
pip install -r requirements.txt
source env/bin/activate
```

2. For training the HUMAID datasets of labeled tweets were combined and collected using `2.PRODUCE_FULL_LABELED_DATA.ipynb`. Additional data was used in the analysis by collecting Tweets by either[^1]:
   - Augmenting a collection that has text and Tweet Ids with time features by using notebook `2.a.ADD_FEATURES_BY_KNOWN_IDS`
   - Collecting Tweets from a specific data range with notebook `2.b.ADDITIONAL_HURRICANE_DATA` 

3. Filter the Tweets in the collection using the notebook `3.PREDICT_YES_NO_HURRICANE` in order to ensure that the collection of tweets is hurricane related. 

4. Additional facts surrounding the hurricanes were added and the data ranges of the Tweets were normalized as per `4.TRAIN_DATA_ADD_NAME_NORMALIZE_DATE.ipynb`.  The normalized date ranges facilitated comparisons of trends between hurricanes.

5. Notebook `5.SUPERVISED_LEARNING_EDA_PREDICT.ipynb` was used for detailed classification.  Logistic Regression was found to be the most effective way to classify the Tweets into sub-categories.  Grid Search with Cross Validation was employed to compare different models with different parameters to see which yielded the best performance, as measured by accuracy and f1 score. Once classified the Tweets could be examined for trends and patterns among the communication across the individual and aggregate time periods for the hurricanes.

6. The `6.EXTENDED_PIPELINE.ipynb` notebook consolidates this process. This notebook relies and three modules for EDA, managing the API calls and DataFrame formating, and the text vectorization using the TFIDVectorizer module from the scikit-learn library. Consolidating the vectorization process was necessary in order to ensure that the process of first filtering and then classifying could proceed in process.  There are significant constraints with the rate-limiting from the Twitter API so the process of running the notebook will take between 1 and 2 hours.  

[^1]: These notebooks require a Twitter Developer account with Academic Research access and an additional config.py file with the values as described.



_This project is released under the Apache License Version 2.0 in order to accommodate the Twitter API code adapted in request_by_IDS.py and request_history.py_


