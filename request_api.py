import requests
import sys
import time
def get_document_name_result(txt):
    requests.post('http://{}:{}/ner_entities?content={}'.format('127.0.0.1', 5151,txt))
txt=sys.argv[1]
# txt = 'bbb.txt'
a=time.time()
get_document_name_result(txt)
print(time.time()-a)