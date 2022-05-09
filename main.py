from author import GetAcess
from sentiment import Sentiment
from totalMention import TotalMention

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
    totalMentions_widget = TotalMention()


    ''' Topics and filters '''
    ### Get Topic ID
    id_unpacked_s22f = author.listening_topics('Unpacked_S22F')
    id_cdj = author.listening_topics('[CDJ]S22F_Purchase (new)','[CDJ]S22F_Consideration (new)','[CDJ]S22F_Advocate (new)','[CDJ]S22F_Aware/Interest (new)')
    
    ### Get keyword Query
    queryGOS = '(GOS OR \"Game optimizing service\" OR gameoptimizingservice OR 지오에스 OR \"게임 최적화 서비스\" OR 게임최적화서비스)'
    queryBTS = 'BTS OR 방탄* OR GalaxyXBTS OR BTS_twt OR jimin OR "ji min" OR 지민 OR 박지민 OR RM OR namjoon OR "nam joon" OR 남준 OR 김남준 OR taehyung OR "tae hyung" OR 뷔 OR 태형 OR 김태형 OR jhope* OR "j hope" OR 제이홉 OR 호석 OR 정호석 OR suga OR yoongi OR "yoon gi" OR 슈가 OR 윤기 OR 민윤기 OR jin OR seokjin OR "seok jin" OR 진 OR 석진 OR 김석진 OR jungkook OR "jung Kook" OR 정국 OR 전정국'
    queryPreOrder = '"사전 예약" OR 사전예약 OR "예약 판매" OR 예약판매 OR "선 주문" OR 선주문 OR pre-order OR preorder OR "pre order" OR pre-booking OR prebooking OR "pre booking" OR pre-reservation OR prereservation OR "pre reservation"'

    ### Get Theme
    themeKR = "61320296f89dc175467fcc94" # South Korea Region
    themeTW = "625532185da6f64a309571d2" # Samsung Official - TW


    ''' Export Data '''
    ### 1. S22F, BTS, BTS 외, Pre-Order ###
    df_s22f = totalMentions_widget.totalMentions_topic(startTime, endTime, id_unpacked_s22f)
    df_bts = totalMentions_widget.totalMentions_topic(startTime, endTime, id_unpacked_s22f, keywordQuery = queryBTS)
    df_bts['BTS 외'] = df_s22f['Total Mention'] - df_bts['Total Mention'] # except bts : s22f - bts
    df_pre_order = totalMentions_widget.totalMentions_topic(startTime, endTime, id_unpacked_s22f, keywordQuery = queryPreOrder)

    ### 2. CDJ ###
    df_cdj = totalMentions_widget.totalMentions_topic(startTime, endTime, id_cdj)

    ### 3. 본사, 지법인 ###
    


    ### 4. 권역별 ###



    ### 5. Giveaway : 공식 계정, 공식 계정 외, 권역별 ###



    ### 6. Sentiment : GOS, GOS - 한국, Unpack_S22F ###
    df_unpack_s22f = sentiment_widget.sentiment_topic(startTime, endTime, id_unpacked_s22f)
    df_gos = sentiment_widget.sentiment_topic(startTime, endTime, id_unpacked_s22f, keywordQuery = queryGOS)
    df_gos_KR = sentiment_widget.sentiment_topic(startTime, endTime, id_unpacked_s22f, keywordQuery = queryGOS, theme = themeKR)


    # DataFrame : pd.merge()
    merge_df1 = pd.merge(df_s22f, df_bts, how="outer", on="Date")
    merge_df2 = pd.merge(merge_df1,df_pre_order, how="outer", on="Date")


    merge_outer_df1 = pd.merge(df_gos,df_gos_KR, how="outer", on="Date")
    merge_outer_df2 = pd.merge(merge_outer_df1, df_unpack_s22f, how="outer", on="Date")
    merge_outer_df2.columns = [
        'Date',
        'GOS Sum', 'GOS Pos', 'GOS Neg',
        'GOS-KR Sum', 'GOS-KR Pos', 'GOS-KR Neg',
        'unpack_S22F Sum', 'unpack_S22F Pos', 'unpack_S22F Neg'
    ]

    file_name = "totalMentions.csv"
    df_cdj.to_csv(file_name)


# if __name__ == "__main__":
#     start = datetime(2022,4,1,0,0,0)   # 2022-04-11 00:00:00
#     end = datetime(2022,4,30,23,59,59)  # 2022-04-30 23:59:59

#     startTime = round(start.timestamp()*1000)
#     endTime = round(end.timestamp()*1000)


#     print(startTime, endTime)


#     print(datetime.fromtimestamp(startTime/1e3))
#     print(datetime.fromtimestamp(endTime/1e3))


