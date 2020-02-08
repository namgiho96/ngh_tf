import nltk
from textMining.entity import Entity
from textMining.samsung_service import SamsungService


class Ctrl:
    def __init__(self):
        pass

    def download_Dictionary(self):
        nltk.download('all')

    def download_Analysis(self):
        entity = Entity()
        service = SamsungService()
        entity.fname = 'kr-Report_2018.txt'
        entity.context = './data/'

        # 디자인 패턴중 훅 메소드 패턴
        service.extract_Token(entity)
        service.extract_Hanguel()
        service.conversion_Token()
        service.compound_Noun()
        entity.fname = 'stopwords.txt'
        service.extract_Stopword(entity)

        service.filtering_Text_With_Stopword()
        service.freqient_Text()
        entity.fname = 'D2Coding.ttf'
        service.draw_Wordcloud(entity)




