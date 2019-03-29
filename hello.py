from flask import *
from flask import  logging


import json
import logging
import time
import base64

from decimal import *

from flask import Flask, jsonify, abort, request
from werkzeug.security import generate_password_hash, check_password_hash

movies = [
    {'name': 'My Neighbor Totoro', 'score': '1988'},
    {'name': 'Dead Poets Society', 'score': '1989'},
    {'name': 'A Perfect World', 'score': '1993'},
    {'name': 'Leon', 'score': '1994'},
    {'name': 'Mahjong', 'score': '1996'},
    {'name': 'Swallowtail Butterfly', 'score': '1996'},
    {'name': 'King of Comedy', 'score': '1999'},
    {'name': 'Devils on the Doorstep', 'score': '1999'},
    {'name': 'WALL-E', 'score': '2008'},
    {'name': 'The Pork of Music', 'score': '2012'},
]


app = Flask(__name__)


@app.route('/ranking')
def login():
    return render_template('index.html', rankList=movies) # movies 换成ranklist


@app.route('/myInformation/<string:member_name>', methods=['GET', 'POST'])
def my_information(member_name):
    if request.method == 'POST':  # 处理编辑表单的提交请求
        member_name = request.form.get('mamber_name')
    return render_template('myinformation.html', member_name=member_name)  # 返回个人信息


@app.route('/threeMeetingOneClass')
def login():
    return render_template('index.html')


@app.route('/talentShow')
def login():
    return render_template('talent.html')


if __name__ == '__main__':
    app.run()
