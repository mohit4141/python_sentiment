from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

dset=[]
pos_word_list=[]
neu_word_list=[]
neg_word_list=[]
f=open("tweet_tokens.txt","r")
for word in f.read().split('\n'):
    # print (word.split('\n'))
    # print(type(word))
    # exit()

    # dset.append(word)
    if (sid.polarity_scores(word)['compound']) >= 0.5:
        pos_word_list.append(word)
        # print(sid.polarity_scores(word)['compound'])
    elif (sid.polarity_scores(word)['compound']) <= -0.5:
        neg_word_list.append(word)
        # print(sid.polarity_scores(word)['compound'])

    else:
        neu_word_list.append(word)        
        # print(sid.polarity_scores(word)['compound'])
    # exit()
f.close()           

# print(dset)
# print('Positive :',len(pos_word_list))        
# print('Neutral :',len(neu_word_list)    )
# print('Negative :',len(neg_word_list) )
