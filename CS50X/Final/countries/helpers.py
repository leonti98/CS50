from restcountries import RestCountryApiV2 as rapi
from flask import Flask, flash, jsonify, redirect, render_template, request, session
import requests
import json

name = "Georgia"


# def main():

#     url = "https://api.dev.me/v1-get-ip-details"

#     headers = {
#         "Accept": "application/json",
#         "x-api-key": "660492a40a6cdafddcf87990-603d950abc0a",
#     }

#     response = requests.request("GET", url, headers=headers)

#     # print(response.text)
#     print(type(response.text))
#     data_dict = json.loads(response.text)

#     print(data_dict)


# def country_info(name):
#     url = "https://api.dev.me/v1-get-country-details?code=string"

#     headers = {
#         "Accept": "application/json",
#         "x-api-key": "660492a40a6cdafddcf87990-603d950abc0a",
#     }

#     response = requests.request("GET", url, headers=headers)

#     data_dict = json.loads(response.text)

#     print(response.text)
#     print(data_dict)


# def countries(name):
#     country_list = rapi.get_countries_by_name(name)
#     # print(country_list)
#     # print(type(country_list[0]))
#     if country_list[0] and type(country_list == list):
#         country = country_list[0]
#         print(country.name)
#         print(country.capital)
#         print(country.top_level_domain)
#         print(country.currencies[0]["name"])
#         print(country.calling_codes)
#         print(country.alt_spellings)
#         print(country.alpha2_code)
#         print(country.translations)
#         print(country.latlng)
#         print(country.native_name)
#         print(country.languages)
#         print(country.flag)
#         print(country.borders)
#         print(country.cioc)
#         print(country.unMember)

url = "https://local-business-data.p.rapidapi.com/search"

querystring = {
    "query": "Hotels in Tbilisi, Gerogia",
    "limit": "5",
    "lat": "37.359428",
    "lng": "-121.925337",
    "zoom": "5",
    "language": "en",
    "region": "us",
}

headers = {
    "X-RapidAPI-Key": "077b50fb84mshd8a1b574cbe81c4p17d808jsn2bc4b65dbb36",
    "X-RapidAPI-Host": "local-business-data.p.rapidapi.com",
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

# if __name__ == "__main__":
#     # countries(name)
#     # main()
#     country_info(name)
