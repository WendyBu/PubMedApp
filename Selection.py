import recommender
import pandas as pd
pd.options.display.max_columns = 30

######### select the interest user's id, retrieve their most interested items. #####################

# print(recommender.inspect_interactions(-1479311724257856983, test_set=False).head(20))
# print("BASED on his/her previous browse and action history, his/her top 20 recommended articles are:")

df = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/data/articlewID.csv", sep="\t")
df = df[["contentId", "journal", "title", "text", "year", "url"]]

####  step 1 : Query the top 10 recommended paper and store into userx.csv ##############

# recs1 = recommender.content_based_recommender_model.recommend_items(3938645257702379823, topn=50, verbose=True)
# recs1 = recs1.drop_duplicates(subset=['title']).reset_index(drop=True)
# recs1 = recs1[0:10]
# id1 = recs1.contentId
# recs1x = df[df.contentId == ]
# recs1x.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user1.csv", sep="\t")
#
# recs2 = recommender.content_based_recommender_model.recommend_items(2111379813881770134, topn=50, verbose=True)
# recs2 = recs2.drop_duplicates(subset=['title']).reset_index(drop=True)
# recs2 = recs2[0:10]
# recs2.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user2.csv", sep="\t")
#
recs7 = recommender.content_based_recommender_model.recommend_items(-2626634673110551643, topn=50, verbose=True)
recs7 = recs7.drop_duplicates(subset=['title']).reset_index(drop=True)
recs7 = recs7[0:10]
recs7.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user7.csv", sep="\t")

recs8 = recommender.content_based_recommender_model.recommend_items(-7990997793599977496, topn=50, verbose=True)
recs8 = recs8.drop_duplicates(subset=['title']).reset_index(drop=True)
recs8 = recs8[0:10]
recs8.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user8.csv", sep="\t")



####  step2: extract all 6 columns from orignal paper data, save to userxdata.csv ##############
# user1 = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user1.csv", sep="\t")
# user1id = user1.contentId.tolist()
# df1x = df.loc[df.contentId.isin(user1id)]
# df1x["userID"] = 3938645257702379823
# df1x.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user1data.csv", sep="\t")
#
# user2 = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user2.csv", sep="\t")
# user1id = user2.contentId.tolist()
# df2x = df.loc[df.contentId.isin(user1id)]
# df2x["userID"] = 2111379813881770134
# df2x.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user2data.csv", sep="\t")
#
# user3 = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user3.csv", sep="\t")
# user3id = user1.contentId.tolist()
# df3x = df.loc[df.contentId.isin(user1id)]
# df3x["userID"] = 4340306774493623681
# df3x.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user3data.csv", sep="\t")
#
# user4 = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user4.csv", sep="\t")
# user4id = user1.contentId.tolist()
# df4x = df.loc[df.contentId.isin(user1id)]
# df4x["userID"] = 8239286975497580612
# df4x.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user4data.csv", sep="\t")


user7 = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user7.csv", sep="\t")
user7id = user7.contentId.tolist()
df7x = df.loc[df.contentId.isin(user7id)]
df7x["userID"] = -2626634673110551643
df7x.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user7data.csv", sep="\t")


user8 = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user8.csv", sep="\t")
user8id = user8.contentId.tolist()
df8x = df.loc[df.contentId.isin(user8id)]
df8x["userID"] = -7990997793599977496
df8x.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user8data.csv", sep="\t")


"""
User reference
user4 : 8239286975497580612  d
user3 : 4340306774493623681  d
user2 : 2111379813881770134  #
user1 : 3938645257702379823  #
user5:  3165343501485572509  d
user6:  3302556033962996625  d
user7: -2626634673110551643  d
user8: -7990997793599977496  #

"""