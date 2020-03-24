#!/usr/bin/python3  


import os
import sys
import pip  #  require  pip  on your system ` sudo apt install python3-pip`   
import json 
import subprocess
import logging as log 


assert   sys.platform == "linux"   # Raise Assertion Error  if  the os  is not linux  

try  :
    import  requests 
except  : 
    pip.main(["install" , "requests"])  

main_api , secdn_api =("https://corona.lmao.ninja/","https://coronavirus-tracker-api.herokuapp.com/all")

default_query  = lambda  url_args : main_api+url_args   
make_request   = lambda  url_args = "countries":  requests.get(default_query(url_args)).json()  

essential_data_for_country =["cases"  , "deaths" , "recovered"  , "country", "active","critical", "todayCases"]
essential_data_for_world        = essential_data_for_country[0:3]  

# collect all list  of   countries  
countries_list = [  c["country"]  for  c in make_request() if c["country"]]

data=None  

if   len(sys.argv)  ==  0x002 : 
    by_country  =  sys.argv[0x001].capitalize()  
    if  by_country  in countries_list:
        country_pos=countries_list.index(by_country)
        data = make_request()[country_pos]
    else : 
        log.warning("No country found ... ") 
        sys.exit(2) 



if  data  is not None :  
    for es_data  in essential_data_for_country : 
        print("{} -------> {}".format(es_data, data[es_data]))
