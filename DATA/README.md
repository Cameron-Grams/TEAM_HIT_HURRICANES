## Data used to study the patterns

In keeping with Twitter's current policy on storing limited information about Tweets the notebooks for this project have been configured to use the Tweets contained in the HUMAID dataset (the API endpoint in th  `6.A.data_handler.py` points to a single csv aggregation), and information that can be gathered by Tweet id. This directory has the collection of ids and lables need for the analysis.  Using these ids requires a [Twitter Developer Academic Research](https://developer.twitter.com/en/products/twitter-api/academic-research) account.

The files  `all_seven_sample.csv` and `mix_2016_2017_ids.txt` represent a small portion of what is possible and are intended to be used only for a demonstration (**Example A** in the `6.EXTENDED_PIPELINE.ipynb` notebook). The two text files contain the Tweet ids and are used with the Data Handler object (**Example B** in the `6.EXTENDED_PIPELINE.ipynb` notebook).


