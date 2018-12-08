import re
import regex_utils

regular_corp_name = re.compile('^[A-Z]{6,13}')
regular_product_code = re.compile('^\d{4}\D{0,3}\d{4}')
regular_cas_num = re.compile('\d+-\d+-?\d+\D{0,2}$')
regular_product_name = re.compile('^[A-Z][a-z]{5,}')

class RegexProcessing:
    def __init__(self,text):
        self.text = text
        self.corp_name = ''
        self.product_name = ''
        self.product_code = ''
        self.cas_number = ''
        self.info = dict()
        self.processing()
        
    def processing(self):
        self.extract()
        self.store()
        
    def extract(self):
        for line in self.text:
            if regular_corp_name.match(line):
                self.corp_name= regex_utils.compare_corp_name(regular_corp_name.match(line))   
            elif regular_product_code.match(line):
                product_code =regular_product_code.match(line)
                dash = re.compile('\D+')
                self.product_code = dash.sub('-', product_code.group())
            elif regular_cas_num.search(line):
                self.cas_number = regular_cas_num.search(line).group()
            elif regular_product_name.match(line):
                self.product_name = regular_product_name.match(line).group()
                
    def store(self):
        self.info['corp_name'] = self.corp_name
        self.info['product_name'] = self.product_name
        self.info['product_code'] = self.product_code
        self.info['cas_number'] = self.cas_number

if __name__ == '__main__':
    pass
else:
    print(__name__)