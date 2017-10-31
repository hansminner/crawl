# coding=utf-8
from collections import Counter  # 统计词频
from wordcloud import WordCloud, STOPWORDS  # 生成词云、通用词
from jieba import analyse
import matplotlib.pyplot as plt  # 在线显示
import jieba
import pandas
import numpy

# 另一种取出停用词的方法 这个方法是遍历分词后的list再把不在停用词的字典中的词集合到final字符串中
stopwords = {}.fromkeys([line.rstrip() for line in open('stopword.txt', encoding='utf-8')])
comment_text = jieba.cut(open('output.txt', 'r', encoding='utf-8').read(), cut_all=False)
segments = []
for seg in comment_text:
    if seg not in stopwords:
        segments += seg

segmentDF = pandas.DataFrame({'segments': segments})
# segStat = segmentDF.groupby(by=["segment"])["segment"].agg({"计数": numpy.size}).reset_index()
# .sort(columns=["计数"], ascending=False)
segcount = segmentDF.groupby(['segments'])
# print(segcount)
segcount.agg([{"count": numpy.size}]).reset_index().sort(columns=["count"], ascending=False)

segcount.head(100)
wordcloud = WordCloud(background_color="white", width=500, height=500, margin=5).generate(segcount)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
