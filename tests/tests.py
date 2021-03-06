#!/usr/bin/env python
# encoding: utf-8

import unittest
from geolocation.google_maps import GoogleMaps

TEST_API_KEY = 'AIzaSyBm0PtaxCuo7iy1KVAnKrl7h8dtA61DXz8'


class GeolocationTest(unittest.TestCase):
    def setUp(self):
        self.google_maps = GoogleMaps(api_key=TEST_API_KEY)

    def test_query(self):
        address = "New York City Wall Street 12"

        location = self.google_maps.search(address)

        self.assertIsNotNone(location.all())

    def test_city(self):
        address = "New York City Wall Street 12"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual('New York', my_location.city.decode('utf-8'))

    def test_route(self):
        address = "New York City Wall Street 12"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual('Wall Street', my_location.route.decode('utf-8'))

    def test_country(self):
        address = "New York City Wall Street 12"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual('United States', my_location.country.decode('utf-8'))

    def test_country_shortcut(self):
        address = "New York City Wall Street 12"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual('US', my_location.country_shortcut.decode('utf-8'))

    def test_lat(self):
        address = "New York City Wall Street 12"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual(40.7060008, my_location.lat)

    def test_lng(self):
        address = "New York City Wall Street 12"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual(-74.0088189, my_location.lng)

    def test_formatted_address(self):
        address = "New York City Wall Street 12"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual('Wall Street, New York, NY, USA',
                         my_location.formatted_address)

    def test_administrative_area_level_1(self):
        address = "New York City Wall Street 12"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual(
            'New York',
            my_location.administrative_area[0].name.decode('utf-8'))

    def test_administrative_area_level_2(self):
        address = "New York City Wall Street 12"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual(
            'New York County',
            my_location.administrative_area[1].name.decode('utf-8'))

    def test_coding(self):
        address = "São Paulo"

        my_location = self.google_maps.search(address).first()

        self.assertEqual(u"São Paulo", my_location.city.decode('utf-8'))

    def test_latlng(self):
        lat = 37.42291810
        lng = -122.08542120

        my_location = self.google_maps.search(lat=lat, lng=lng).first()

        self.assertEqual('Mountain View', my_location.city.decode('utf-8'))

