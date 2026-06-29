import pandas as pd
from urlextract import URLExtract
from wordcloud import WordCloud
from collections import Counter


extract=URLExtract()
def fetch_stats(user:str,df:pd.DataFrame)-> tuple:
    '''Shows Stats of User'''

    if user != 'OverAll':
        df=df[df['user']==user]

    #num of msg
    num_msgs=df.shape[0]

    #2 number of words
    num_words=[]
    for message in df['message']:
        num_words.extend(message.split())
    

    #3 Number of Media

    num_media=df['message']=='<Media omitted>\n'


    #4 Number of Links

    num_link=[]

    for message in df['message']:
        num_link.extend(extract.find_urls(message))


    return num_msgs,num_words,num_media,num_link


def most_busy_user(df:pd.DataFrame)->tuple:
    x=df['user'].value_counts().head()
    

#user -> message percent 
    df= round(df['user'].value_counts()/df.shape[0]*100,2).reset_index().rename(columns={'index':'name','user':'percent'})
    return x,df 

# def create_wordCloud(selected_user,df):

#     if selected_user !='OverAll':
#         df=df[df['user']==selected_user]

#     wc=WordCloud(width=500,height=500,min_font_size=10)

#     df_wc=wc.generate(df['message'].str.cat(sep=' '))

#     return df_wc
def create_wordCloud(selected_user, df):

    print(df.columns.tolist())
    print(df.head())

    if selected_user != 'OverAll':
        df = df[df['user'] == selected_user]

    wc = WordCloud(width=500, height=500, min_font_size=10)

    df_wc = wc.generate(df['message'].str.cat(sep=' '))

    return df_wc


def most_common_words(user,df):
    #most common words in chat except stop words etc 
    f=open('./resources/stop_hinglish.txt')

    stop_words=f.read()

    if user!='OverAll':
        df=df[df['user']==user]
    
    temp=df[df['user']!='chat_notification']

    temp=temp[temp['message']!='<Media omitted>\n']

    words=[]

    for message in temp['message']:
        for word in message.split():
            if word not in stop_words:
                words.append(word)

    most_common_df=pd.DataFrame(Counter(words).most_common(20))

    return most_common_df