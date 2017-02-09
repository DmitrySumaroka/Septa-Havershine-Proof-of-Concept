# -*- coding: utf-8 -*-
# @Author: Dima Sumaroka
# @Date:   2017-01-23 13:08:19
# @Last Modified by:   Dima Sumaroka
# @Last Modified time: 2017-02-09 14:29:47

from flask import Flask, jsonify, url_for, redirect, request

app = Flask(__name__)

app.septa_transit_view = "http://www3.septa.org/hackathon/TransitViewAll/"
app.google_api_key = "AIzaSyCegvkOr5RFudtQuxrVbpMFFgHHs2ph37M"
app.trasit_url = "/transit"

if __name__ == "__main__":
    app.run(debug=True)

from app.api import septa
from app import views
