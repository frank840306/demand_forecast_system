# from flask import Flask, render_template
# app = Flask(__name__)

# # @app.route('/hello/<int:score>')
# @app.route('/why')
# def hello_name(score = 60):
#    return render_template('index.html', marks = score)

# if __name__ == '__main__':
#    app.run(debug = True)

from flask import Flask, jsonify, render_template, request
from samplePublisherData import sampleData
from subprocess import call
from utils import *
import forecastRecommender
import numpy as np
import chartkick
import os


app=Flask(__name__,static_folder=chartkick.js(), static_url_path='/src/static')
app.jinja_env.add_extension("chartkick.ext.charts")
app._static_folder = os.path.abspath("src/static/")
# print(app._static_folder)

root_dir = './'
output_dir = os.path.join(root_dir, 'output')

AUTHOR_PKL = os.path.join(output_dir, 'authorProportion.pkl')
TYPE_PKL = os.path.join(output_dir, 'typeProportion.pkl')

ratioOfBookToSellFromEachPublisher = {
	'publish_A' : {
		'book_1' : 0,
		'book_2' : 0,
		'book_3' : 0
	},
	'publish_B' : {
		'book_4' : 0,
		'book_5' : 0,
		'book_6' : 0,
		'book_7' : 0,
	},
	'publish_C' : {
		'book_8' : 0,
		'book_9' : 0,
	}
}

recommendBookToSellFromEachPublisher = {
	'publish_A' : {
		'book_1' : 0,
		'book_2' : 0,
		'book_3' : 0
	},
	'publish_B' : {
		'book_4' : 0,
		'book_5' : 0,
		'book_6' : 0,
		'book_7' : 0,
	},
	'publish_C' : {
		'book_8' : 0,
		'book_9' : 0,
	}
}

@app.route('/analysis/<int:mark>/result')
def first_graph(mark):
	
	ratioOfBookToSellFromEachPublisher = forecastRecommender.predict()
	samplePublisher = sampleData()
	author_data = readPickle(AUTHOR_PKL)
	type_data = readPickle(TYPE_PKL)
	
	print(ratioOfBookToSellFromEachPublisher)
	data = {}
	data['type'] = 3
	data['sample'] = samplePublisher
	data['author_data'] = author_data
	data['type_data'] = type_data
	data['predict'] = ratioOfBookToSellFromEachPublisher
	data['recommend'] = recommendBookToSellFromEachPublisher
	return render_template('mainPage.html', data=data)

	# return render_template('mainPage.html', data=author_data, data1=type_data, type=3, publisher=samplePublisher, forecast=ratioOfBookToSellFromEachPublisher)

@app.route('/analysis/<int:mark>')
def analysis(mark):
	# print('XDDD')
	# print(mark)
	samplePublisher = sampleData()
	author_data = readPickle(AUTHOR_PKL)
	type_data = readPickle(TYPE_PKL)
	# mark = 0
	data = {}
	data['type'] = mark
	data['sample'] = samplePublisher
	data['author_data'] = author_data
	data['type_data'] = type_data
	data['predict'] = ratioOfBookToSellFromEachPublisher
	data['recommend'] = recommendBookToSellFromEachPublisher
	return render_template('mainPage.html', data=data)
	# return render_template('mainPage.html', data=author_data, data1=type_data, type=mark, publisher=samplePublisher, forecast=None)	
# @app.route('/book/')
# def book_page()

@app.route('/analysis')
def analysis():
	
	samplePublisher = sampleData()
	author_data = readPickle(AUTHOR_PKL)
	type_data = readPickle(TYPE_PKL)
	
	data = {}
	data['type'] = 0
	data['sample'] = samplePublisher
	data['author_data'] = author_data
	data['type_data'] = type_data
	data['predict'] = ratioOfBookToSellFromEachPublisher
	data['recommend'] = recommendBookToSellFromEachPublisher
	
	return render_template('mainPage.html', data=data)
if __name__=="__main__":
	app.run(debug=True)