#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 23:19:18 2020

@author: abhisekkumar
"""

#%%
from flask import Flask, request

app = Flask(__name__)
#this only for get method

@app.route('/')
def add():
    a= request.args.get('a') #this is a string
    b= request.args.get('b')
    return str(int(a)+int(b))#correct parsing is required

if __name__ == '__main__':
    
    app.run()