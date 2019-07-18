import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_columns = 30

# df = pd.read_csv('testdata.csv', sep=",", index_col=0)
# # print(df)
# #
# # ax = df.transpose().plot(kind='bar', figsize=(15, 8))
# # for p in ax.patches:
# #     ax.annotate("%.3f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()), \
# #                 ha='center', va='center', xytext=(0, 10), textcoords='offset points')
# # plt.show()


df = pd.read_csv('data/shared_articles.csv')
print(df.shape)
print(df.head(3))
print(df.columns)
print(df.contentId.nunique())
print(df.nunique())

"""
Index(['timestamp', 'eventType', 'contentId', 'authorPersonId',
       'authorSessionId', 'authorUserAgent', 'authorRegion', 'authorCountry',
       'contentType', 'url', 'title', 'text', 'lang'],
      dtype='object')
3057
timestamp          3121
eventType             2
contentId          3057
authorPersonId      252
authorSessionId    2017
authorUserAgent     114
authorRegion         19
authorCountry         5
contentType           3
url                3029
title              3011
text               3019
lang                  5
"""