#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 04:53:00 2025

@author: austinjohnson_snhu
@proffessor: Mr. Ling
@class: CS340
@date: 07/30/25
"""

from pymongo import MongoClient
from pymongo.errors import PyMongoError



class AnimalShelter:
    
    
    def __init__(self, username, password):
        
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33588
        DB = 'AAC'
        COL = 'animals'
        
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
        
    def create(self,data):
        if data:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except PyMongoError as e:
                print(f"Insertfailed: {e}")
                return False
        else:
            raise ValueError("No data provided to insert.")
    
    
    def read(self, query={}):
        try:
            if query is None:
                cursor = self.collection.find({})
            else:
                cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError as e:
            print(f"Query failed: {e}")
            return []
            
    def update(self, query, new_values, multiple=False):
        if query and new_values:
            try:
                if multiple:
                    result = self.collection.update_many(query, {'$set': new_values})
                else:
                    result = self.collection.update_one(query, {'$set': new_values})
                return result.modified_count
            except PyMongoError as e:
                print(f"Update failed: {e}")
                return 0
        else:
            raise ValueError("Both query and new values mustu be provided.")
            
    def delete(self, query, multiple=False):
        if query:
            try:
                if multiple:
                    result = self.collection.delete_many(query)
                else:
                    result = self.collection.delete_one(query)
                return result.deleted_count
            except PyMongoError as e:
                print(f"Delete failed: {e}")
                return 0
        else:
            raise ValueError("No query provided for deletion.")