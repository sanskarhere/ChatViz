import streamlit as st
from src.preprocess import preprocess
import src.helpers as helpers
import matplotlib.pyplot as plt



st.set_page_config('ChatViz',layout='wide')

st.sidebar.title('WhatSapp Chat Analyser')

file=st.sidebar.file_uploader('Choose a File')

if file is not None:
    bytes_data=file.getvalue()
    data=bytes_data.decode()
    df=preprocess(data)
   
    st.dataframe(df)

    #Fetch Unique User

    user_list=df['user'].unique().tolist()
    user_list.remove('chat_notification')
    user_list.sort()

    # box=st.sidebar.selectbox('Show Analysis',['OverAll','Individual'])
    
    # if box =='Individual':
    #     st.selectbox('Select Individual',user_list)

    user_list.insert(0,'OverAll')
    user=st.sidebar.selectbox('Show Analysis :',user_list)

    if st.sidebar.button('Show analysis'):
       
        col1,col2,col3,col4=st.columns(4)

        msgs,words,media,link=helpers.fetch_stats(user,df)
        with col1:
            st.header('Total Messages')
            st.title(msgs)
            
        with col2:
            st.header('Total words')
            st.title(len(words))

        with col3:
            st.header('Media Shared')
            st.title(media.sum())
            # st.metric('Media Shared',len(media))

        with col4:
            st.header('Total Link')
            st.title(len(link))

        #Find the busiest user in the chat

        if user =='OverAll':
            st.title('Most Busy Users')
            x,df1=helpers.most_busy_user(df)

            fig,ax=plt.subplots()
            col1,col2=st.columns(2)


            with col1:
                ax.bar(x.index,x.values,color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(df1)

        #wordCloud

        df_wc=helpers.create_wordCloud(user,df)

        fig,ax=plt.subplots()

        ax.imshow(df_wc)
        st.pyplot(fig)


        #most common words
        st.title('Most Common Words')
        most_common_df=helpers.most_common_words(user,df)

        fig,ax=plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1])
        
        st.pyplot(fig)