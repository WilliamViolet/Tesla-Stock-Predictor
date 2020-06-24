import GetOldTweets3 as got

tweetCriteria = got.manager.TweetCriteria().setUsername("elonmusk")\
                                           .setSince("2020-06-21")\
                                           .setUntil("2020-06-24")\
                                           .setMaxTweets(10)

for i in range(9):
    print(got.manager.TweetManager.getTweets(tweetCriteria)[i].text)
    print("\n")
