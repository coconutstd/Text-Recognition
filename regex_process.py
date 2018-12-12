import re
import regex_utils

#DAEJUNG용 정규식
regular_corp_name = re.compile('[A-Z]{5,13}')
regular_cas_num = re.compile('\d+-\d+-?\d+\D{0,2}$')
#regular_product_code = re.compile('^\d{4,7}\D{0,3}\d{4}')
#regular_product_name = re.compile('^[A-Z][a-z]{5,}')

#SIGMA용 정규식
regular_product_code = re.compile('(?P<pcode>\d{4,7})-\d{1,3}[A-Z]{1,3}')
regular_product_name = re.compile('([A-Z]{1,2}[,.-][A-Z]{1,2}[,.-])?[A-Z][a-z]{3,}')

#SIGMA_back용 정규식
regular_cas_number = re.compile('(\d{2,5})[.:-]?(\d{1,3})[.:-]?(\d{1,3})?')

class RegexProcessing:
    def __init__(self,text):
        self.text = text
        self.corp_name = ' '
        self.product_name = ' '
        self.product_code = ' '
        self.cas_number = ' '
        self.info = dict()
        self.processing()
        
    def processing(self):
        self.extract()
        self.store()
        
    def extract(self):
        for line in self.text:
            if regular_product_code.search(line):
                product_code =regular_product_code.search(line)
                self.product_code = product_code.group("pcode")
                #SIGMA일 경우 Product Code 찾고 Product Name 찾음
                if regular_product_name.search(line):
                    self.product_name = regular_product_name.search(line).group()
                #dash = re.compile('\D+')
                #self.product_code = dash.sub('-', product_code.group())
            elif regular_corp_name.match(line):
                self.corp_name= regex_utils.compare_corp_name(regular_corp_name.match(line))   
            #SIGMA는 search
            #DAEJUNG은 match
            elif regular_cas_number.search(line):
                self.cas_number = regular_cas_number.search(line).group()
            #SIGMA의 경우 search
            #DAEJUNG의 경우 match
            #elif regular_product_name.search(line):
            #    self.product_name = regular_product_name.search(line).group()
                
    def store(self):
        self.info['corp_name'] = self.corp_name
        self.info['product_name'] = self.product_name
        self.info['product_code'] = self.product_code
        self.info['cas_number'] = self.cas_number

if __name__ == '__main__':
    pass
else:
    print(str(__name__)+' module loaded')