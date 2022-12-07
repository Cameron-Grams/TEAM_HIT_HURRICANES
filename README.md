# Team HIT Analysis of Hurricane related Tweets

### Purpose
The purpose of this project is to provide insight into hurricane related communication found on Twitter. Tweets related to hurricanes can be classified and examined for patterns relating to the time surrounding the hurricane. 

### Concept
The project was developed from an [initial labeled dataset](https://crisisnlp.qcri.org/humaid_dataset.html#) used to train a model to classify Tweets as belonging to one of 9 categories:

1. sympathy and support
2. injured or dead people
3. rescue, volunteering or donnation efforts
4. infrastructure and utility damage
5. requests or urgent needs
6. caution and advice
7. non-humanitarian aid
8. displaced people and evacuations
9. other relevant information

The initial labeled dataset was from 2016 and 2017.  Additional Tweets relating to hurricanes from the storm seasons going back as far as 2012 were collected from the Twitter API and classified into one of the 9 categories. An additional classifier was trained to distiinguish hurricane from non-hurricane related Tweets in order to ensure the integrity of the collection pulled from the API. 

Category 9, "other relevant information", was found to be the largest category across years.  KMeans clustering was used to attempt to break this category down into more granular subcategories, however it was found that any clusters within Category 9 were highly specific to the individual storms in the time period and were not informative to the overall analysis.  

### Methodology
1. Create a Python virtual environment by loading the `requirements.txt` file:

```shell
python -m venv hurricane_tweets
install -r requirements.txt
source env/bin/activate
```

2. Collect Tweets for use in analysis by either:
    1. Augmenting the collection with time features by using notebook `2.a.ADD_FEATURES_BY_KNOWN_IDS`
    2. Collecting Tweets by a specific data range with notebook `2.b.ADDITIONAL_HURRICANE_DATA` (this notebooks requires a Twitter Developer account with Academic Research access)

3. Classify the collection using the notebook `3.PREDICT_YES_NO_HURRICANE` in order to ensure that the collection of tweets is hurricane related. 




