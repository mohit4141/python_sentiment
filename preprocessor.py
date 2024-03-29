import time
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from textblob import TextBlob
import enchant

result=[]
lemmatizer = WordNetLemmatizer() 
count=0
start_time=time.time()
pol=0
sub=0
# cloud=[]
d = enchant.Dict("en_US")
with open('article370_tweets.csv','r',encoding='utf8') as file:
    f=open("tweet_tokens.txt","w+")

    for line in file:
        # i+=1
        twt = re.sub(r'^https?:\/\/.*[\r\n]*', '', line, flags=re.MULTILINE)
        twt = re.sub(r'^pic.twitter.com*', '', twt, flags=re.MULTILINE)
        twt = ' '.join(re.sub("(@[A-Za-z]+)|([^A-Za-z \t])|(\w+:\/\/\S+)", " ", twt).split()) 
        
        

        twt = twt.lower()
        twt = word_tokenize(twt)
        # print(line)
        result.append(line)
        stop_words = list(set(stopwords.words('english')))
        
        stop_words.extend(["pic","twitter","com"])
        result=[]
        for l in twt :
            if l not in stop_words and len(l)>2 and d.check(l):
                l = lemmatizer.lemmatize(l)
                # result.append(l)
                f.write((l+'\n'))
        # print(result)
        # f.write((result))
        # blob = TextBlob(str(result))
        # sent=blob.sentiment
        # pol+=sent.polarity
        # sub+=sent.subjectivity
        count+=1
        # print(sent,pol,sub)


    f.close()

print("Execution time is: {}".format(time.time()-start_time))
# print("\n Subjectivity of the topic is: ",sub/count )    