from flask import current_app

def search_query(cls, query, page, per_page):
    q = cls.query.all()
    search = {
        'hits': {
            'hits': [
                {
                    '_id': 1,
                    'name': 'name'},
                {
                    '_id': 2,
                    'name': 'name2'}],
            'total': {
                'value': 2}}}
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids, search['hits']['total']['value']
