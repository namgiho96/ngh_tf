# 디자인 패턴중 훅 메소드 패턴
# 메소드 별로 순서를 정하는 것이다
# 후킹 하는것이다 순서대로 훅킹
import re
import matplotlib.pyplot as plt
import pandas as pd

from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from konlpy.tag import Okt


class SamsungService:
    def __init__(self):
        self.texts = []
        self.tokens = []
        self.okt = Okt()
        self.stopWords = []
        self.freqtxt = []

    def extract_Token(self, payload):
        print('1. >>> text 문서에서 토큰을 추출')
        filename = payload.context + payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.texts = f.read()

        # print(f'{self.texts[:300]}')
        # .format 해라가 바뀐 분법

    def extract_Hanguel(self):
        print('2. >>> 한글만 추출 하세요~!!')
        texts = self.texts.replace('\n', ' ')

        tokenizer = re.compile(r'[^ ㄱ-힣]')
        # 표현식으로 만들어라 한글 빼고 다 지워줘라

        self.texts = tokenizer.sub('', texts)
        # print(f'{self.texts[:300]}')

    def conversion_Token(self):
        print('3. 토큰으로 반환해!!!')
        self.tokens = word_tokenize(self.texts)
        # print(f'{self.texts[:300]}')

    def compound_Noun(self):
        print('4. 복합 명사는 묶어서 fitering 으로 출력')
        print('>>> ex) 삼성전자의 스마트폰은 --> 삼성전자 스마트폰')
        noun_token = []
        for token in self.tokens:
            token_pos = self.okt.pos(token)
            temp = [txt_tag[0] for txt_tag in token_pos
                    if txt_tag[1] == 'Noun']
            if len("".join(temp)) > 1:
                noun_token.append("".join(temp))
        self.texts = " ".join(noun_token)
        # print(f'{self.texts[:300]}')

    def extract_Stopword(self, payload):
        print('5. >>> stopword 추출')
        filename = payload.context + payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.stopWords = f.read()
            self.stopWords = self.stopWords.split(' ')
        # print(f'{self.stopWords[:10]}')

    def filtering_Text_With_Stopword(self):
        print('6. >>>')
        self.texts = word_tokenize(self.texts)
        self.texts = [text for text in self.texts
                      if text not in self.stopWords]

    def freqient_Text(self):
        self.freqtxt = pd.Series(dict(FreqDist(self.texts))) \
            .sort_values(ascending=False)

    def draw_Wordcloud(self, payload):
        print('>>> 워드크라우드 작성 ')
        filename = payload.context + payload.fname
        wcloud = WordCloud(filename,
                           relative_scaling=0.2,
                           background_color='white').generate(" ".join(self.texts))
        plt.figure(figsize=(12, 12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
