# -*- coding: utf-8 -*-
import re


placesList=[]
def parseCsv():

    for i in places.values()[1:]:
        for j in i:
            if not j=="":
                try:
                    placesList.append(j.lower())
                except :
                    pass



def findPlaces(text):
    placesintext=[]
    for word in placesList:
        try:
            result = re.findall('\\b'+word+'\\b', text, flags=re.IGNORECASE)
            if len(result)>0:
                    placesintext.append(word)
        except :
            pass

    return set(placesintext)


