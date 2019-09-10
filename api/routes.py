'''
Routing code
'''
from flask import Blueprint, render_template, redirect, request, url_for
import datetime
import requests
from .models import add_database
import pandas as pd

# from flask import jsonify

blueprint = Blueprint('main', __name__)


# first argument inside Blueprint() is name of our blueprint which here is 'main'


# import time
# from timeloop import Timeloop
# from datetime import timedelta
# tl=Timeloop()


def convert_add_into_db(apiResponse):
    # apiResponse=jsonify(apiResponse.json())
    df = pd.DataFrame.from_records(apiResponse.json())
    df.columns = ["Open_time", "Open", "High", "Low", "Close", "Volume", "Close_time", "Quote_asset_volume",
                  "Number_of_trades", "Buy_base_asset", "Buy_quote_asset", "Ignore"]
    df_dict = df.to_dict('records')
    l = len(df_dict)
    for i in range(l):
        df_dict[i]['Close_time'] = datetime.datetime.fromtimestamp((df_dict[i]['Close_time']) / 1000)
        df_dict[i]['Open_time'] = datetime.datetime.fromtimestamp((df_dict[i]['Open_time']) / 1000)
    for p in range(l):
        add_database(df_dict[p])
    # return apiResponse


def add_new_sample(coinSymbol, klineInterval):
    params = {'symbol': coinSymbol, 'interval': klineInterval, 'limit': 1}
    apiResponse = requests.get('https://api.binance.com/api/v1/klines', params)
    convert_add_into_db(apiResponse)


@blueprint.route('/api/binance/', methods=["get", "post"])
def apipage():
    if request.form:
        apiEndpoint = request.form.get("endpoints")
        coinSymbol = request.form.get("coins")
        klineNumber = request.form.get("number")
        klineTimedelta = request.form.get("timedelta")
        klineInterval = str(klineNumber + klineTimedelta)

        if apiEndpoint == 'klines':
            params = {'symbol': coinSymbol, 'interval': klineInterval, 'limit': 1000}
            apiResponse = requests.get('https://api.binance.com/api/v1/klines', params)

        elif apiEndpoint == 'exchangeInfo' or apiEndpoint == 'ticker/24hr':
            apiResponse = requests.get('https://api.binance.com/api/v1/' + apiEndpoint)

        else:
            params = {'symbol': coinSymbol}
            apiResponse = requests.get('https://api.binance.com/api/v1/' + apiEndpoint, params)
        convert_add_into_db(apiResponse)

        if request.form.get('keepGettingData'):
            add_new_sample(coinSymbol, klineInterval)
        return redirect(url_for('.homepage'))
        # return render_template("ack.html")

    return render_template("api.html")


# request.endpoint=main.apipage
# request.url_rule.rule=/api/binance
# request.url_rule.endpoint=main.apipage

@blueprint.route('/home/')
def homepage():
    try:
        return render_template("layout.html")
    except Exception as e:
        return e


@blueprint.route('/about/')
def aboutpage():
    try:
        return render_template('about.html')
    except Exception as e:
        return e


@blueprint.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", error=str(e))

# request.endpoint=main.homepage
# request.url_rule.rule=/home
# request.url_rule.endpoint=main.homepage

# @blueprint.route('/adddata/<name>')
# def home(name):
#     return find_email(name)

# @blueprint.route('/adduser',methods=["Get", "POST"])
# def home2():
#     if (request.form):
#         dict={'username': request.form.get("username"),
#               'email': request.form.get("email")}
#         x=add_user(dict)
#         return str(x.id)
#     return render_template("layout.html")


# apiResponse=apiResponse.json()
# for row in apiResponse:
# df=pd.DataFrame.from_records(apiRespon---> 41                     Portfolio.updatepf(0,Main.money/t[dfcol].iloc[i],'buy')se.json())
# df.columns=["Open_time", "Open", "High","Low","Close", "Volume","Close_time","Quote_asset_volume","Number_of_trades","Buy_base_asset","Buy_quote_asset","Ignore"]
# df['Open_time']=datetime.datetime.fromtimestamp(int(df['Open_time'])/1000)
# df['Close_time']=datetime.datetime.fromtimestamp(int(df['Close_time'])/1000)
# df_dict=df.to_dict('records')
# count=len(df_dict)
# data=list()
# for i in range(count):
# data[i]=**(df_dict[i])
# add_database(df_dict[i])
# x=add_database(data)

# server {
#         listen 80;
#
#       server_name ;
#
#       root /var/www/example.com;
#       index index.html;
#
#       location / {
#               try_files $uri $uri/ =404;
#       }
