# coding=utf-8
from collections import Counter  # 统计词频
from wordcloud import WordCloud, STOPWORDS  # 生成词云、通用词
import matplotlib.pyplot as plt  # 在线显示
import jieba

# from word_analysis import word_counter

# http://blog.csdn.net/vivian_ll/article/details/68067574 成功地址
# http://www.jianshu.com/p/c612847ffa72 要看的地址
comment_text = open('output.txt', 'r', encoding='utf-8').read()
cut_text = " ".join(jieba.cut(comment_text))
cloud = WordCloud(
    # 设置字体，不指定就会出现乱码
    font_path="HYQiHei-25J.ttf",
    # font_path=path.join(d,'simsun.ttc'),
    # 设置背景色
    background_color='white',
    # 词云形状
    # mask=color_mask,
    # 允许最大词汇
    max_words=2000,
    # 最大号字体
    max_font_size=40
)
"""
# data = [open('output.txt', 'r', encoding='utf-8').read()]
# print(data[:10])
# wc = Counter(data)  # 基于Counter自定义的子类（留作业：结巴分词、停用词）
# wordcloud = WordCloud(background_color="white", width=600, height=400, margin=5).fit_words(dict_fre)
"""
wordcloud = WordCloud(background_color="white", width=600, height=400, margin=5).generate(cut_text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
