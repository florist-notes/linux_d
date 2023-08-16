'''
Script: Preprocess wfs data for lane segmentation | utm to (lat, lon); zip
#!pip install geopandas, OWSLib, utm


'''

import utm
import json
import geopy
import random
import string
from io import BytesIO, TextIOWrapper
import geopandas as gpd
from geopy.geocoders import Nominatim
from owslib.wfs import WebFeatureService
from shapely.geometry import Point, Polygon

''' #Layer Information from WFS
for layerID in list(sorted(wfs.contents.keys()))[0:len(wfs.contents.keys())]:
    layer = wfs[layerID]
    print('Layer ID:', layerID)
    print('Title:', layer.title)
    print('Boundaries:', layer.boundingBoxWGS84, '\n')
'''
#fetch data from WFS
def fetch_data(url, version, typename):
  wfs = WebFeatureService(url, version)
  response = wfs.getfeature(typename, outputFormat='application/geo+json')
  geodata = json.load(TextIOWrapper(response, encoding='utf-8'))
  return geodata

#convet utm to (lat, lon)
def utm2latlon(geodata2):
  for lent in range(len(geodata2['features'])):
    print('This is the '+ str(lent+1)+'th feature:')
    count_lentx = 0
    for lentx in geodata2['features'][lent]['geometry']['coordinates'][0]:
      count_lent3 = 0
      for lent3 in lentx:
        print(utm.to_latlon(lent3[0], lent3[1], 32, 'N'))
        converted = utm.to_latlon(lent3[0], lent3[1], 32, 'N')
        geodata2['features'][lent]['geometry']['coordinates'][0][count_lentx][count_lent3] = (converted[1], converted[0])
        count_lent3 += 1
      count_lentx += 1
  return geodata2


#return zip code for each feature
def find_zip_lsbg(place, geolocator, lent, data):
  location = geolocator.reverse("{}, {}".format(place[1], place[0]))
  try:
      return location.raw['address']['postcode']
  except KeyError:
      NoneType = type(None)
      place_name = data['features'][lent]['properties']['strassenname'] + ', '+ data['features'][lent]['properties']['stadtteil']
      location = geolocator.geocode(place_name)
      if type(location) != NoneType:
          data = location.raw
          loc_data = data['display_name'].split()
          zip = loc_data[-2].replace(',', '')
          if zip.isnumeric() == True:
              return int(zip)
          else:
              return 0
      else:
          return 0

#get zip code from nominatim api
def zip_processed(geodata2):
  letters = string.ascii_lowercase
  for lent in range(len(geodata2['features'])):
    user = ''.join(random.choice(letters) for i in range(10))
    geolocator = geopy.Nominatim(user_agent=user)
    longlat = geodata2['features'][lent]['geometry']['coordinates'][0][0][0]
    zipp = find_zip_lsbg(longlat, geolocator, lent, geodata2) 
    geodata2['features'][lent]['properties']['zip'] = zipp
    print('Zip : ' + str(zipp) + ', Street Name : ' + geodata2['features'][lent]['properties']['strassenname'] + ', '+ geodata2['features'][lent]['properties']['stadtteil'] + ' ; feature number is : '+str(lent)+'\n')
  return geodata2

# save json file
def save_geojson(geodata2):
  with open('processed_de.hh.up:b_mitte_mr_feinkartierung_flaechen.geojson', 'w') as fp:
      json.dump(geodata2, fp)

if __name__ == "__main__":
  url='https://geodienste.hamburg.de/HH_WFS_Feinkartierung_Strasse?REQUEST=GetCapabilities&SERVICE=WFS'
  version='2.0.0'
  typename='de.hh.up:b_mitte_mr_feinkartierung_flaechen'
  data = fetch_data(url, version, typename)
  latlon_processed = utm2latlon(data)
  latlonzip_processed = zip_processed(latlon_processed)
  save_geojson(latlonzip_processed)



