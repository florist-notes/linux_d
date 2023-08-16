'''
Script: Preprocess wfs data for lane segmentation | utm to (lat, lon); zip
#!pip install geopandas, OWSLib, utm


'''

import utm
import json
import random
import string
import geopy
from io import BytesIO, TextIOWrapper
import geopandas as gpd
from geopy.geocoders import Nominatim
from owslib.wfs import WebFeatureService
from shapely.geometry import Point, Polygon

wfs = WebFeatureService(url='https://geodienste.hamburg.de/HH_WFS_Feinkartierung_Strasse?REQUEST=GetCapabilities&SERVICE=WFS', version='2.0.0')

for layerID in list(sorted(wfs.contents.keys()))[0:len(wfs.contents.keys())]:
    layer = wfs[layerID]
    print('Layer ID:', layerID)
    print('Title:', layer.title)
    print('Boundaries:', layer.boundingBoxWGS84, '\n')

response = wfs.getfeature(typename='de.hh.up:b_mitte_mr_feinkartierung_flaechen', outputFormat='application/geo+json')
geodata = json.load(TextIOWrapper(response, encoding='utf-8'))
geodata2 = geodata
geodata_test = geodata

print('WFS data fetched!')

#convet utm to (lat, lon)
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
    
print('utm to (lat, lon) conversion done!')

#return zip code for each streetname
def find_zip_lsbg(place, geolocator, lent):
  location = geolocator.reverse("{}, {}".format(place[0], place[1]))
  try:
      return location.raw['address']['postcode']
  except KeyError:
      NoneType = type(None)
      place_name = geodata['features'][lent]['properties']['strassenname'] + ', '+ geodata['features'][lent]['properties']['stadtteil']
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
letters = string.ascii_lowercase
#for lent in range(len(geodata2['features'])):
for lent in range(500):
  user = ''.join(random.choice(letters) for i in range(10))
  geolocator = geopy.Nominatim(user_agent=user)
  latlong = geodata2['features'][lent]['geometry']['coordinates'][0][0][0]
  zip_place = find_zip_lsbg(latlong, geolocator, lent) 
  print('Zip : ' + str(zip_place) + ', Street Name : ' + geodata['features'][lent]['properties']['strassenname'] + ', '+ geodata['features'][lent]['properties']['stadtteil'] + ' ; feature number is : '+str(lent)+'\n')
  geodata2['features'][lent]['properties']['zip'] = zip_place


with open('test2_processed_de.hh.up:b_mitte_mr_feinkartierung_flaechen.geojson', 'w') as fp:
    json.dump(geodata2, fp)

