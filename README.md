# Team HIT Analysis of Hurricane related Tweets
Team Members: [Ki-Hyun Biak](https://github.com/abka0214), [Cameron Grams](https://github.com/Cameron-Grams), and [Ryan Jimenez](https://github.com/rjjimene)

### Purpose
The purpose of this project is to provide insight into hurricane related communication found on Twitter. Tweets related to hurricanes can be classified and examined for patterns relating to the time surrounding the hurricane. 

**Use Case:** *A party interested in the communication on Twitter during a hurricane presents a collection of Tweet ids from known storm periods and asks for insights into how they can better format or structure communication over Twitter by examining trends or patterns in communication during the storm period.* 

### Quick Start
The `6.EXTENDED_PIPELINE.ipynb` notebook demonstrates the integration of the techniques that we developed to examine hurricane related communication over Twitter. **Example A** will execute in the notebook with sample data[^1].  **Example B** requires the use of the features in the DataHandler that draw from the Twitter API.

Employing the data handler and notebooks that collect historical data from Twitter requires an [Twitter Developer Academic Research](https://developer.twitter.com/en/products/twitter-api/academic-research) account. Configure a `config.py` file with the account credentials as specified from the developer account. Additionally the use of the API will require managing the rate-limiting features of the Twitter API.  Cell Blocks from **Example B** should be considered for possible asynchronous use, it may be more efficient to collect the datasets from the API independent of the other functions of the notebook. 

After examining the `6.EXTENDED_PIPELINE.ipynb` notebook the details can be seen in the other notebooks from the **Methodology** section below.

### Concept
The project was developed from the hurricane related Tweets in the [HUMAID datasets](https://crisisnlp.qcri.org/humaid_dataset.html#). These datasets were used to train a model to classify Tweets as belonging to one of 9 categories based on the text of the Tweets.  The 9 categories are:

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

Category 9, "other relevant information", was found to be the largest category across years.  KMeans clustering was used to attempt to break this category down into more granular subcategories (see the `MODEL_DEVELOPMENT` directory, however it was found that any clusters within Category 9 were highly specific to the individual storms in the time period and were not informative to the overall analysis.  

### Methodology
1. To ensure the code used for development functions appropriately create a Python virtual environment by loading the `requirements.txt` file:

```shell
python -m venv hurricane_tweets
source env/bin/activate
pip install -r requirements.txt
```

2. In training the classifier model, the HUMAID datasets of labeled tweets were combined and collected using `2.PRODUCE_FULL_LABELED_DATA.ipynb`. Additional data was used in the analysis by collecting Tweets by either[^2]:
   - Augmenting a collection that has text and Tweet Ids with time features by using notebook `2.a.ADD_FEATURES_BY_KNOWN_IDS`
   - Collecting Tweets from a specific data range with notebook `2.b.ADDITIONAL_HURRICANE_DATA` 

3. Next the collection of Tweets were filtered using the notebook `3.PREDICT_YES_NO_HURRICANE` in order to ensure that the collection of tweets is hurricane related. 

4. Additional facts surrounding the hurricanes were added and the data ranges of the Tweets were normalized as per `4.TRAIN_DATA_ADD_NAME_NORMALIZE_DATE.ipynb`.  The normalized date ranges facilitated the comparison of trends between hurricanes that took place at different times.

5. Notebook `5.SUPERVISED_LEARNING_EDA_PREDICT.ipynb` was used for classification of the Tweets as belonging to one of the 9 categories.  Logistic Regression was found to be the most effective way to classify the Tweets into these sub-categories.  Grid Search with Cross Validation was employed to compare different models with different parameters to see which yielded the best performance, as measured by accuracy and f1 score. Once classified the Tweets could be examined for trends and patterns among the communication across the individual and aggregate time periods for the hurricanes.

6. The `6.EXTENDED_PIPELINE.ipynb` notebook consolidates this process. This notebook relies on three modules for EDA, managing the API calls and DataFrame formating, and the text vectorization using the TFIDVectorizer module from the scikit-learn library. Consolidating the vectorization process was essential in order to ensure that the process of first filtering and then classifying the Tweets could be conducted in a single operation.  There are significant constraints with the rate-limiting from the Twitter API so the process of running the notebook using the DataHandler (**Example B**) will take between 1 and 2 hours.  

[^1]: Notes for formating the module files are embedded as comments in the `6.Extended_Pipeline.ipynb` notebook. 
[^2]: These notebooks require a Twitter Developer account with Academic Research access and an additional config.py file with the values as described.



_This project is released under the Apache License Version 2.0 in order to accommodate the Twitter API code adapted in request_by_IDS.py and request_history.py_


