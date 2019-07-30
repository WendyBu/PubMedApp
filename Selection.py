# import recommender
import pandas as pd
pd.options.display.max_columns = 30

from sqlalchemy import create_engine



# print(recommender.inspect_interactions(-1479311724257856983, test_set=False).head(20))
# print("BASED on his/her previous browse and action history, his/her top 20 recommended articles are:")
#
df = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/data/articlewID.csv", sep="\t")
df = df[["contentId", "journal", "title", "text", "year", "url"]]

####  Query the top 10 recommended paper and store into userx.csv ##############

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
# recs3 = recommender.content_based_recommender_model.recommend_items(4340306774493623681, topn=50, verbose=True)
# recs3 = recs3.drop_duplicates(subset=['title']).reset_index(drop=True)
# recs3 = recs3[0:10]
# recs3.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user3.csv", sep="\t")
#
# recs4 = recommender.content_based_recommender_model.recommend_items(8239286975497580612, topn=50, verbose=True)
# recs4 = recs2.drop_duplicates(subset=['title']).reset_index(drop=True)
# recs4 = recs2[0:10]
# recs4.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user4.csv", sep="\t")

# engine = create_engine("mysql://root:matt123@localhost/ada")
# df = pd.DataFrame(['A','B'],columns=['new_tablecol'])
# df.to_sql(name='new_table', con=engine, if_exists='append')


####  extract all 6 columns from orignal paper data, save to userxdata.csv ##############
user1 = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user1.csv", sep="\t")
user1id = user1.contentId.tolist()
df1x = df.loc[df.contentId.isin(user1id)]
df1x["userID"] = 3938645257702379823
df1x.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user1data.csv", sep="\t")

user2 = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user2.csv", sep="\t")
user1id = user2.contentId.tolist()
df2x = df.loc[df.contentId.isin(user1id)]
df2x["userID"] = 2111379813881770134
df2x.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user2data.csv", sep="\t")

user3 = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user3.csv", sep="\t")
user3id = user1.contentId.tolist()
df3x = df.loc[df.contentId.isin(user1id)]
df3x["userID"] = 4340306774493623681
df3x.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user3data.csv", sep="\t")

user4 = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user4.csv", sep="\t")
user4id = user1.contentId.tolist()
df4x = df.loc[df.contentId.isin(user1id)]
df4x["userID"] = 8239286975497580612
df4x.to_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user4data.csv", sep="\t")



"""
user4 : 8239286975497580612
user3 : 4340306774493623681
user2 : 2111379813881770134
user1 : 3938645257702379823

"""