from truscore import app
from flask import Flask
from elasticsearch import Elasticsearch


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return _es

connect_elasticsearch()


if __name__ == "__main__":
	Flask.run(app)

