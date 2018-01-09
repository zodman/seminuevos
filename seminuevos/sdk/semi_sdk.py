#!/usr/bin/env python
# -*- coding: utf-8 -*-
# made by Sergio Dzul
from ConfigParser import SafeConfigParser
from urllib import urlencode
import json
import os
import re
import ssl
import requests
from .ssl_helper import SSLAdapter
from django.conf import settings
import logging

log = logging.getLogger('core')


class SDK(object):

    def __init__(self, client_id='testAccount', client_secret='testPass123'):
        self.client_id = client_id
        self.client_secret = client_secret

        parser = SafeConfigParser()
        parser.read(os.path.dirname(os.path.abspath(__file__))+'/config.ini')

        self._requests = requests.Session()
        try:
            self.SSL_VERSION = parser.get('config', 'ssl_version')
            self._requests.mount('https://', SSLAdapter(ssl_version=getattr(ssl, self.SSL_VERSION)))
        except Exception:
            self._requests = requests

        self.API_ROOT_URL = getattr(
            settings,
            'SEMINUEVOS_API_ROOT_URL',
            parser.get('config', 'api_root_url')
        )

        self.headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
        #self.headers = {'Content-Type': 'text/xml', 'Expect': ''}
        self._access_token = self.get_access_token()

    #AUTH METHODS
    def auth_url(self):
        # tmp ((optimizar))
        # params = {'grant_type': 'client_credentials', 'client_id': self.client_id,
        #           'client_secret': self.client_secret, 'scope': 'publish,catalog'}
        # url = '/ptx/oauth' + '?' + urlencode(params)
        url = '/oauth/access_token?grant_type=client_credentials' \
              '&client_id=%s&client_secret=%s&scope=publish,catalog' % (self.client_id, self.client_secret)
        return url

    def get_access_token(self):
        uri = self.API_ROOT_URL+self.auth_url()
        log.debug('url: %s' % uri)
        response = self._requests.post(uri, params=urlencode({}), headers=self.headers)

        if response.ok:
            response_info = response.json()
            return response_info['access_token']
        else:
            # response code isn't a 200; raise an exception
            response.raise_for_status()

    # REQUEST METHODS
    def get(self, path, params=False, headers=None):
        if not params:
            params = {'access_token': self._access_token}
        uri = self.make_path(path)
        if not headers:
            response = self._requests.get(uri, params=urlencode(params), headers=self.headers)
        else:
            response = self._requests.get(uri, params=urlencode(params), headers=headers)
        return response

    def post(self, path, body=False, params={}):
        # if not params:
        #     params = {'access_token': self._access_token}
        headers = self.headers.copy()
        headers.update({'Authorization': self._access_token})
        uri = self.make_path(path)
        if body:
            body = json.dumps(body)
        response = self._requests.post(uri, params=params, data=body, headers=headers)
        log.debug('\nSeminuevos Post Request\nuri: %s\nbody: %s\nheaders: %s\
            \nparams: %s\n\nresponse: %s' % (uri, body, headers, params, response.json()))
        return response

    def put(self, path, body=False, params={}):
        uri = self.make_path(path)
        if body:
            body = json.dumps(body)

        response = self._requests.put(uri, data=body, params=urlencode(params), headers=self.headers)
        return response

    def delete(self, path, params={}):
        uri = self.make_path(path)
        response = self._requests.delete(uri, params=params, headers=self.headers)
        return response

    def make_path(self, path, params={}):
        # Making Path and add a leading / if not exist
        if not (re.search("^http", path)):
            if not (re.search("^\/", path)):
                path = "/" + path
            path = self.API_ROOT_URL + '/api/secure' +path
        if params:
            path = path + "?" + urlencode(params)
        return path

    def provinces(self ):
        _url = '/catalog/search-provinces'
        return self.get(_url)

    def currencies(self):
        _url = '/catalog/search-currencies'
        return self.get(_url)

    def special_extras(self):
        _url = '/catalog/search-special-extras'
        return self.get(_url)

    def mileage_types(self):
        _url = '/catalog/search-mileage-types'
        return self.get(_url)

    def steerings(self):
        _url = '/catalog/search-steerings'
        return self.get(_url)

    def transmissions(self):
        _url = '/catalog/search-transmissions'
        return self.get(_url)

    def fuels(self):
        _url = '/catalog/search-fuels'
        return self.get(_url)

    def heating_system(self):
        _url = '/catalog/search-heating-systems'
        return self.get(_url)

    def windows(self):
        _url = '/catalog/search-windows'
        return self.get(_url)

    def drives(self):
        _url = '/catalog/search-drives'
        return self.get(_url)

    def interiors(self):
        _url = '/catalog/search-interiors'
        return self.get(_url)

    def colors(self):
        _url = '/catalog/search-colors'
        return self.get(_url)

    def cities(self,country, province):
        _url = '/catalog/search-cities?idCountry={}&idProvince={}'.format(country, province)
        return self.get(_url)

    def extras(self):
        _url = '/catalog/search-extras'
        return self.get(_url)

    def types(self):
        _url = '/search/vehicle-search/type'
        return self.get(_url)

    def subtypes(self, type_id):
        _url = '/search/vehicle-search/subtype/%s' % type_id
        return self.get(_url)

    def brands(self, type_id, subtype_id):
        _url = '/search/vehicle-search/brand/%s?subtype=%s' % (type_id, subtype_id)
        return self.get(_url)

    def models(self, brand_id):
        _url = '/search/vehicle-search/all-models/%s' % brand_id
        return self.get(_url)

    def catalog(self, type_search):
        _url = '/catalog/search-%s' % type_search
        return self.get(_url)

    def find_dealer(self, dealer_id):
        _url = '/catalog/search-dealer-by-id/%s' % dealer_id
        return self.get(_url)

    def post_vehicle(self, data):
        _url = '/vehicle/publish/publishSicop'
        return self.post(_url, body=data)

    def post_vehicle_pictures(self, id, order, files={}, params={}):
        path = '/vehicle/upload-image/%s/%s' % (id, order)
        headers = {'Authorization': self._access_token}
        uri = self.make_path(path)
        response = self._requests.post(url=uri, data={},
                                       files=files, headers=headers, params=params)
        log.debug('\nSEMINUEVOS Image Post Request\nuri: %s\
            \nheaders: %s\nparams: %s\n\nResponse: %s' % (uri, headers, params, response.json()))
        return response

    def change_vehicle_status(self, vehicle_id, dealer_id, status_id='1'):
        path = '/vehicle/publish/changeVehicleStatus'
        data = {
            'vehicleId': vehicle_id,
            'dealerId': dealer_id,
            'statusId': status_id
            }
        return self.post(path=path, body=data)
