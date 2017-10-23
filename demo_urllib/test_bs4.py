import bs4
import re

html_doc = """
    <td valign="top" class="text12px-160" width="81%">
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/106437.html" target="_blank">政治认知力：衡量国家治理能力的前提性标准</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/106272.html" target="_blank">杨光斌 ：滥用“民粹主义”已成西方掩饰政治真相的手段</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/106265.html" target="_blank">新自由主义酿成全球民粹大潮</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/105997.html" target="_blank">论意识形态的国家权力原理</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/105960.html" target="_blank"> 论意识形态的国家权力原理 ——兼论中国国家权力的结构性问题</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/105828.html" target="_blank">论世界政治体系</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/102945.html" target="_blank">曾毅 西方如何建构民主话语权</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/101062.html" target="_blank">“民主方舟”驶向何方？——2016年世界民主乱局分析</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/100091.html" target="_blank">观察中国政治要有认识论上突破</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/95514.html" target="_blank">丰裕中的思想贫困——兼论中国教育—科学管理体制的问题与出路</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/94647.html" target="_blank">不能做“合法性”概念的囚徒</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/90922.html" target="_blank">"法治中国”时代的新政治科学——政治学立场的政治法学（研究大纲）</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/90135.html" target="_blank">中国比较政治学需要自信与自觉</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/89384.html" target="_blank">从国际政治比较看“治理民主”的优势</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/89051.html" target="_blank">“回到中国”的社会科学及政治学的学科性贡献</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/80506.html" target="_blank">发展中国家搞“党争民主”祸害无穷——中国民主实践的分层性与多样性</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/79807.html" target="_blank">民主与世界政治冲突</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/79330.html" target="_blank">福山政治观点的转变说明了什么——“政治制度衰败论”揭示了美国否决型政体的真相</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/77567.html" target="_blank">“国家治理体系和治理能力现代化”的世界政治意义</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/73597.html" target="_blank">走出集权-分权的二元对立误区</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/72156.html" target="_blank">杨光斌 曾毅：中国社会纷争的观念之维与因应之道</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/67887.html" target="_blank">当前世界民主变种与未来大势</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/67604.html" target="_blank">杨光斌 舒卫方：“公正社会”取向的国家治理与制度建设</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/64275.html" target="_blank">社会权利优先的中国政治发展选择</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/58911.html" target="_blank">党的十八大与中国政治的发展</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/58287.html" target="_blank">早发达国家的政治发展次序问题</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/53592.html" target="_blank">民主与中国的未来</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/52040.html" target="_blank">新国家理论述评</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/49266.html" target="_blank">政体理论的回归与超越——建构一种超越“左”右的民主观</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/41299.html" target="_blank">杨光斌 尹冬华：我国人民代表大会制度的民主理论基础</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/41298.html" target="_blank">制度范式：一种研究中国政治变迁的途径</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/41285.html" target="_blank">以制度为中心的历史发展观——现代化研究的新视野</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/41284.html" target="_blank">国家结构理论的解释力与适用性问题</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/41283.html" target="_blank">我国现行中央—地方关系下的社会公正问题与治理</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/41282.html" target="_blank">政治的形式与现代化的成败</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/35376.html" target="_blank">制度变迁中的政党中心主义</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/31648.html" target="_blank">现代国家成长中的国家形态问题</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/25603.html" target="_blank">公民参与和当下中国的治道变革</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/19735.html" target="_blank">杨光斌 郑伟铭：国家形态与国家治理</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/19416.html" target="_blank">政治学：从古典主义到新古典主义</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/19378.html" target="_blank">杨光斌 高卫民：探索宏观的新制度主义</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/15545.html" target="_blank">国家兴衰的集体行动理论解析——奥尔森集体行动理论的贡献与误区</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/15510.html" target="_blank">新制度主义政治学在中国的发展</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/15427.html" target="_blank">我国经济转型时期国家经济行为的政治学分析</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/15244.html" target="_blank">我国经济转型时期国家权力结构的制度分析</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/13492.html" target="_blank">观念、制度与经济绩效——中国与印度经济改革的政治学理论价值</a><br>
        <img src="images/yypl-81.gif" width="8" height="13"> 
        <a href="/data/6767.html" target="_blank">中国经济转型时期国家经济行为的政治学分析</a><br>
    </td>
    <p class="title">fast</p>
    """
soup = bs4.BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print('get all link')
links = soup.find_all('a')
for link in links:
    print(link.name, link['href'], link.get_text())

print('get 106437')
link_node = soup.find('a', href='/data/15510.html')
print(link_node.name, link_node['href'], link_node.get_text())

print('reg')
# 使用正则表达式匹配含有相关字符的
link_node = soup.find('a', href=re.compile("10"))
print(link_node.name, link_node['href'], link_node.get_text())

print('get p获得p段落中的文字')
# 获取指定class的内容
p_node = soup.find('p', class_='title')
print(p_node.name, p_node.get_text())
