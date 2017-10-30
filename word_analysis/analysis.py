# coding=utf-8
from collections import Counter  # 统计词频
from wordcloud import WordCloud, STOPWORDS  # 生成词云、通用词
import matplotlib.pyplot as plt  # 在线显示

data = [open('output.txt', 'r', encoding='utf-8').read()]
# print(data[:10])
wc = WordCounter(data)  # 基于Counter自定义的子类（留作业：结巴分词、停用词）
dict_fre = 'hao'
wordcloud = WordCloud(background_color="white", width=600, height=400, margin=5).fit_words(dict_fre)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
