import scrapy

class DmozSpider(scrapy.Spider):
    name = "lelem"
    start_urls = [
        # "http://www.leleketang.com/let3/knowledges.php?from=undefined&cid=295610",
        # 'http://www.leleketang.com/let3/knowledges.php?from=undefined&cid=253457',
        # 'http://www.leleketang.com/let3/knowledges.php?from=undefined&cid=252340',
        # 'http://www.leleketang.com/let3/knowledges.php?from=undefined&cid=278143',
        # 'http://www.leleketang.com/let3/knowledges.php?from=undefined&cid=284030',
        # 'http://www.leleketang.com/let3/knowledges.php?from=undefined&cid=294477',
        # 'http://www.leleketang.com/let3/knowledges.php?from=undefined&cid=290761',
        # 'http://www.leleketang.com/let3/knowledges.php?from=undefined&cid=287272',
        # 'http://www.leleketang.com/let3/knowledges.php?from=undefined&cid=288376',
        # 'http://www.leleketang.com/let3/knowledges.php?from=undefined&cid=291357',

        'http://www.leleketang.com/let3/knowledges.php?from=undefined&cid=249577'
    ]


    def parse(self, response):
        datalist = response.css('.cal_root')
        print('--------')

        for item1 in datalist:
            filename = item1.css('.cal_name a::attr(title)').extract_first()
            code = item1.css('.cal_name a::attr(data-cid)').extract_first()
            link = 'http://www.leleketang.com/let3/knowledge_list.php?cid='+str(code)
            with open('目录.txt', 'a') as f:
                f.write(filename+" ")
                f.write(code + " ")
                f.write(link+'\n')