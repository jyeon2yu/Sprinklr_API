from author import GetAcess
from sentiment import Sentiment
from datetime import datetime
import pandas as pd


if __name__ == "__main__":
    
    """ Date Setting """
    start = datetime(2022,4,1,0,0,0)   # 2022-04-11 00:00:00
    end = datetime(2022,4,30,23,59,59)  # 2022-04-18 23:59:59

    startTime = round(start.timestamp()*1000)
    endTime = round(end.timestamp()*1000)


    """ Export of Sentiment Data """
    author = GetAcess()
    sentiment_widget = Sentiment()

    topicID = author.listening_topics('Unpacked_S22F')
    kQuery = "(GOS OR \"Game optimizing service\" OR gameoptimizingservice OR 지오에스 OR \"게임 최적화 서비스\" OR 게임최적화서비스)"
    theme = author

    ### Sentiment DataFfame ###
    unpack_S22F = sentiment_widget.sentiment_topic(startTime, endTime, topicID)
    gos = sentiment_widget.sentiment_topic(startTime, endTime, topicID, keywordQuery = kQuery)
    gos_KR = sentiment_widget.sentiment_topic(startTime, endTime, topicID, keywordQuery = kQuery)


    # DataFrame : pd.merge()
    merge_outer_df1 = pd.merge(gos,gos_KR, how="outer", on="date")
    merge_outer_df2 = pd.merge(merge_outer_df1, unpack_S22F, how="outer", on="date")
    merge_outer_df2.columns = [
        'Date',
        'GOS Sum', 'GOS Pos', 'GOS Neg',
        'GOS-KR Sum', 'GOS-KR Pos', 'GOS-KR Neg',
        'unpack_S22F Sum', 'unpack_S22F Pos', 'unpack_S22F Neg'
    ]

    file_name = "sentiment.csv"
    merge_outer_df2.to_csv(file_name)


# if __name__ == "__main__":
#     start = datetime(2022,4,1,0,0,0)   # 2022-04-11 00:00:00
#     end = datetime(2022,4,30,23,59,59)  # 2022-04-30 23:59:59

#     startTime = round(start.timestamp()*1000)
#     endTime = round(end.timestamp()*1000)


#     print(startTime, endTime)


#     print(datetime.fromtimestamp(startTime/1e3))
#     print(datetime.fromtimestamp(endTime/1e3))


