import requests
from urllib.parse import urljoin


class NOAA(object):

    def __init__(self, key):
        self._api_header = {
            'token': key
        }
        self._host = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'

    def datasets(self, dataset_id=None, data_type_id=None, location_id=None, station_id=None, start_date=None,
                 end_date=None, sort_field=None, sort_order='asc', limit=25, offset=0):

        endpoint = 'datasets'

        if dataset_id is not None:
            endpoint = endpoint + '/{dataset_id}'.format(dataset_id=
                                                         dataset_id)

        data = {
            'datatypeid': data_type_id,
            'locationid': location_id,
            'stationid': station_id,
            'startdate': start_date,
            'enddate': end_date,
            'sortfield': sort_field,
            'sortorder': sort_order,
            'limit': limit,
            'offset': offset
        }

        r = requests.get(urljoin(self._host, endpoint),
                         data=data,
                         headers=self._api_header)

        return r.json()

    def data_categories(self, category_id=None, dataset_id=None, location_id=None, station_id=None,
                        start_date=None, end_date=None, sort_field=None, sort_order='asc', limit=25, offset=0):

        endpoint = 'datacategories'

        if category_id is not None:
            endpoint = endpoint + '/{category_id}'.format(category_id=
                                                          category_id)

        data = {
            'datasetid': dataset_id,
            'locationid': location_id,
            'stationid': station_id,
            'startdate': start_date,
            'enddate': end_date,
            'sortfield': sort_field,
            'sortorder': sort_order,
            'limit': limit,
            'offset': offset
        }

        r = requests.get(urljoin(self._host, endpoint),
                         data=data,
                         headers=self._api_header)

        return r.json()

    def data_types(self, type_id=None, dataset_id=None, location_id=None, station_id=None, category_id=None,
                   start_date=None, end_date=None, sort_field=None, sort_order='asc', limit=25, offset=0):

        endpoint = 'datatypes'

        if type_id is not None:
            endpoint = endpoint + '/{type_id}'.format(type_id=
                                                      type_id)

        data = {
            'datasetid': dataset_id,
            'locationid': location_id,
            'stationid': station_id,
            'datacategoryid': category_id,
            'startdate': start_date,
            'enddate': end_date,
            'sortfield': sort_field,
            'sortorder': sort_order,
            'limit': limit,
            'offset': offset
        }

        r = requests.get(urljoin(self._host, endpoint),
                         data=data,
                         headers=self._api_header)

        return r.json()

    def location_categories(self, category_id=None, dataset_id=None, start_date=None, end_date=None,
                            sort_field=None, sort_order='asc', limit=25, offset=0):

        endpoint = 'locationcategories'

        if category_id is not None:
            endpoint = endpoint + '/{type_id}'.format(category_id=
                                                      category_id)

        data = {
            'datasetid': dataset_id,
            'startdate': start_date,
            'enddate': end_date,
            'sortfield': sort_field,
            'sort_order': sort_order,
            'limit': limit,
            'offset': offset
        }

        r = requests.get(urljoin(self._host, endpoint),
                         data=data,
                         headers=self._api_header)

        return r.json()

    def locations(self, location_id=None, dataset_id=None, location_category_id=None, data_category_id=None,
                  start_date=None, end_date=None, sort_field=None, sort_order='asc', limit=25, offset=0):

        endpoint = 'locations'

        if location_id is not None:
            endpoint = endpoint + '/{location_id}'.format(location_id=
                                                          location_id)

        data = {
            'datasetid': dataset_id,
            'locationcategoryid': location_category_id,
            'datacategoryid': data_category_id,
            'startdate': start_date,
            'enddate': end_date,
            'sortfield': sort_field,
            'sortorder': sort_order,
            'limit': limit,
            'offset': offset
        }

        r = requests.get(urljoin(self._host, endpoint),
                         data=data,
                         headers=self._api_header)

        return r.json()
