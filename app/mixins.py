dict#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:12:09 2021

@author: epaphradito
"""
from flask import url_for
from app import db

from app.search import search_query

class SearchableMixin(object):
    @classmethod
    def search(cls, expression, page, per_page):
        ids, total = search_query(
            cls.__tablename__, 
            expression,
            page,
            per_page)
        if total == 0:
            return cls.query.filter_by(id=0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in_(ids)).order_by(
            db.case(when, value=cls.id)
        ), total
    

# db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
# db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)

class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
                },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page, 
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
                }
            }
        
        return data