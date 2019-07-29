"""
******Prepare the Article data******
* don't run it again, it will take about 1 hr.
* The output is the article dataset.  store in 'data/articlewID.xls'
source: Pubmed  https://www.ncbi.nlm.nih.gov/pubmed/
Establish the API access with pubmed database
Collect about 3000 articles' metadata, including 17 diseases or topics
The metadata include: journal title, article title, article abstract, article type, publish year...
Since the API limited the query request, so it set up a sleep time after each query.
"""


import pandas as pd
import urllib
from bs4 import BeautifulSoup
import requests
from xml.etree import ElementTree
from lxml import etree
from time import sleep

pd.set_option("display.max_columns", 100)


def query_pubmed(key):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=" + key + "[TIAB]" + "&retmax=200"
    response = urllib.request.urlopen(url, timeout=None)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    num = 0
    pubmedIDList = []
    for id in soup.find_all('id'):
        num +=1
        pubmed_ID = id.string
        pubmedIDList.append(pubmed_ID)
    return num, pubmedIDList


def getContents(pubmedID):
    absUrl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=" + pubmedID + "&retmode=xml"
    # https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=30217816&retmode=xml
    response = requests.get(absUrl, timeout=None)
    parser = etree.XMLParser(recover=True)
    response = response.content
    fixed_response = response.replace(b'\x0c', b'')
    root = ElementTree.fromstring(fixed_response, parser=parser)

    JournalTitle = " "
    ArticleTitle = " "
    Abstract = " "
    year = " "
    lang = " "
    type = " "
    region = " "
    if root:
        for child in root.iter('*'):
            if child.tag == "Title":
                JournalTitle = child.text
            if child.tag == "ArticleTitle":
                ArticleTitle = child.text
            if child.tag == "AbstractText":
                Abstract = child.text
            if child.tag == "Year":
                year = child.text
            if child.tag == "Language":
                lang = child.text
            if child.tag == "PublicationType":
                type = child.text
            if child.tag == "Country":
                region = child.text
        print("from def: ", JournalTitle, ArticleTitle, Abstract, year, lang, type, region)
        return [JournalTitle, ArticleTitle, Abstract, year, lang, type, region]
    else:
        return None


def collectData():
    keywords = ['cancer', 'diabetes', 'stroke', 'Alzheimer', 'Diarrhea', 'heart disease', 'flu', 'stress', 'aging', \
                   'tuberculosis', 'vaccine', 'smoking', 'HIV', 'asthma', 'Cirrhosis', 'obesity', 'headache', 'depression']
    # keywords = ['cancer', 'diabetes', 'stroke', 'Alzheimer']    #1   800
    # keywords =['Diarrhea']     #2  150
    # keywords = ['flu']   #3  250
    # keywords = ['aging', 'stress']      #4  400
    # keywords = ['tuberculosis', 'vaccine', 'smoking']   #5  600
    # keywords = ['heart+disease']   #6  160
    # keywords = ['HIV', 'asthma', 'Cirrhosis', 'obesity']   #7 640
    # keywords = ['headache', 'depression']   #8 320
    entries = []
    publicationList = []
    for key in keywords:
        publication_num, pubIDList = query_pubmed(key)
        publicationList.extend(pubIDList)
        print("total number of articles:", len(publicationList))
        # print("ids: ", pubIDList)
        print("key: ", key)
        # print("publication list: ", publicationList)
        for id in pubIDList:
            text = getContents(id)
            sleep(0.4)
            if text:
                url = "https://www.ncbi.nlm.nih.gov/pubmed/" + id
                text.extend([id, url, key])
                entries.append(text)
                try:
                    with open('temp/temp.txt', 'a') as f:       # In case the Server stop by any reason, save the query result as temp file.
                        text = ['None' if v is None else v for v in text]
                        f.writelines('\t'.join(text))
                        f.writelines('\n')
                except:
                    print("did not write in ", text)

            else:
                print("no information for ", id)
    df = pd.DataFrame(columns=['JournalTitle', 'ArticleTitle', 'Abstract', 'year', 'lang', 'type', 'region', 'PMID', 'url', 'key'], data=entries)
    df.to_csv('output/testdata.xls', sep="\t")


def articleDataset():
    df1 = pd.read_csv('output/testdata1.xls', sep="\t")
    df2 = pd.read_csv('output/testdata2.xls', sep="\t")
    df3 = pd.read_csv('output/testdata3.xls', sep="\t")
    df4 = pd.read_csv('output/testdata4.xls', sep="\t")
    df5 = pd.read_csv('output/testdata5.xls', sep="\t")
    df6 = pd.read_csv('output/testdata6.xls', sep="\t")
    df7 = pd.read_csv('output/testdata7.xls', sep="\t")
    df8 = pd.read_csv('output/testdata8.xls', sep="\t")
    df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], ignore_index=True)
    df = df.sample(frac=1).reset_index(drop=True)
    df.to_csv('data/articles.xls', sep="\t")
    # print(df.head(5))
    # print(df.shape)
    pass


def addID():
    df = pd.read_csv('data/articles.xls', sep="\t")
    df = df.head(3047)
    dfID = pd.read_csv('data/contentID.csv', sep="\t")

    print(df.shape)
    print(dfID.shape)
    dfs = pd.concat([df, dfID['contentId']], axis=1, ignore_index=True)
    print(dfs.shape)
    print(dfs.head())
    dfs.rename(columns={0: 'index', 1: 'oldIndex', 2: 'journal', 3: 'title', 4:'text', 5: 'year', 6: 'lang', 7: 'type', 8: 'region', \
                        9: 'PMID', 10: 'url', 11: 'key', 12: 'contentId'}, inplace=True)
    print(dfs.head(3))
    # dfs.to_csv('data/articlewID.csv', sep="\t")
    dfs.to_csv('data/articlewID.xls', sep="\t")


if __name__ == "__main__":
    # collectData()
    # articleDataset()
    # addID()
    pass



