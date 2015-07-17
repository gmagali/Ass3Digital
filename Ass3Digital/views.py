# -*- coding: utf-8 -*-
import csvparser
# Import django modules
from django.shortcuts import render_to_response
import geograpy

def index(request):

        if 'submit' in request.GET:
                text=request.GET['myText']
                csvparser.parseCsv()
                placeList=csvparser.findPlaces(text)
                print placeList
                return render_to_response('index.html', {'placeList':placeList })
        else:
                placeList=""
                return render_to_response('index.html', {'placeList':placeList })






