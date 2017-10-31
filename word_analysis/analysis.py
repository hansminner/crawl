# coding=utf-8
from collections import Counter  # 统计词频
from wordcloud import WordCloud, STOPWORDS  # 生成词云、通用词
import matplotlib.pyplot as plt  # 在线显示
import jieba
from jieba import analyse

# from word_analysis import word_counter

# http://blog.csdn.net/vivian_ll/article/details/68067574 成功地址
# http://www.jianshu.com/p/c612847ffa72 要看的地址

"""
a=jieba.analyse.extract_tags(sentence, topK = 20, withWeight = False, allowPOS = ())
# sentence:待提取的文本。# topK:返回几个 TF/IDF 权重最大的关键词，默认值为20。
# withWeight:是否一并返回关键词权重值，默认值为False。
# allowPOS:仅包括指定词性的词，默认值为空，即不进行筛选。
"""
comment_text = jieba.cut(open('output.txt', 'r', encoding='utf-8').read(), cut_all=False)
# 必须使用join两个字符连接直接传会报错 转变类型为list
comment_text_1 = "".join(comment_text)
# 通用停用词
jieba.analyse.set_stop_words('stopword.txt')
# 自己项目的停用词
jieba.analyse.set_stop_words('self_stopword.txt')
tags = jieba.analyse.extract_tags(comment_text_1, 50)
cut_text = " ".join(tags)
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
    fit_words(dict_fre) 参数是单词和出现的频率
# wordcloud = WordCloud(background_color="white", width=600, height=400, margin=5).fit_words(dict_fre)
"""
wordcloud = WordCloud(background_color="white", width=5000, height=5000, margin=5).generate(cut_text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
