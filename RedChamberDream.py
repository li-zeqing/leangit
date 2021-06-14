#《红楼梦》人物统计Top20
import jieba
excludes = {"什么","一个","我们","那里","如今","你们","说道","知道",
            "姑娘","起来","这里","出来","他们","众人","奶奶","自己","一面","太太","只见",
            "两个","怎么","没有","不是","不知","这个","听见","这样","进来","咱们","告诉",
            "就是","东西","回来","大家","只是","只得","这些","不敢","出去","所以",
            "不过","不好","姐姐","丫头","的话","一时","鸳鸯","过来","不能","心里","如此",
            "今日","银子","二人","答应","几个","还有","只管","一回","这么","说话","那边",
            "这话","外头","打发","自然","今儿","罢了","那些","听说","小丫头","屋里","如何","问道"}

txt  = open("红楼梦.txt","r",encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word)==1 :
        continue
    elif word =="老太太":
        rword = "贾母"
    elif word =="黛玉":
        rword = "林黛玉"
    elif word == "老爷":
        rword = "贾赦"
    elif word == "二爷":
        rword = "贾琏"
    else:
        rword = word
    counts[rword] = counts.get(rword , 0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key = lambda x:x[1], reverse=True)
for i in range(20):
    word , count = items[i]
    print("{0:<10}{1:>5}".format(word,count))