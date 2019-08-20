import twint
from textblob import TextBlob
# Configure
c = twint.Config()
# c.Username = " "
c.Search = "#article370"
c.Limit = 20000
# c.Since = "2019-08-06"
c.Format = "Tweet id: {id} | Tweet: {tweet}"
c.Store_object = True
tweets=[]
c.Store_object_tweets_list = tweets
# Run
c.Store_csv = True
# CSV Fieldnames
c.Custom["tweet"] = ["tweet"]
# Name of the directory
c.Output = "twitter"
twint.run.Search(c)
# print(len(tweets))
# print(str(tweets[12]))
# TextBlob(tweets).sentiment()
