from flask import Flask
import flask
import json

server = Flask(__name__)


@server.route('/ner_entities', methods=['POST', 'GET'])
def roleinfo():


    ipt = flask.request.args.get('content')
    with open(ipt,'r',encoding='utf-8') as read:
        for i in read.readlines():
            x = '输入是{}'.format(i)
            with open('aaa.txt','a',encoding='utf-8') as w:
                w.write('\n')
                w.write(x)
        print(x)
    return json.dumps(x, ensure_ascii=False)


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5151)
