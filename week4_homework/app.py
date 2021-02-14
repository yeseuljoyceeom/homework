from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():

    #클라이언트가 준 데이터 가져오기
    name_receive=request.form['name_give']
    amt_receive=request.form['amt_give']
    adrs_receive=request.form['adrs_give']
    pnum_receive=request.form['pnum_give']

    #db에 데이터 입력
    doc={
        'name':name_receive,
        'amt':amt_receive,
        'adrs':adrs_receive,
        'pnum':pnum_receive
    }

    db.megatonBar.insert_one(doc)
    return jsonify({'result': 'success', 'msg':'주문 완료!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders=list(db.megatonBar.find({},{'_id':False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)