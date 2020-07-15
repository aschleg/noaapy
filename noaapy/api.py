import requests
from urllib.parse import urljoin


class NOAA(object):

    def __init__(self, key):
        self.key = key
        self._api_header = {
            'token': self.key
        }
        self._host = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'

    def datasets(self,
                 dataset_id=None,
                 data_type_id=None,
                 location_id=None,
                 station_id=None,
                 start_date=None,
                 end_date=None,
                 sort_field=None,
                 sort_order='asc',
                 limit=25,
                 offset=0):

        endpoint = 'datasets'

        if dataset_id is not None:
            endpoint = endpoint + '/{dataset_id}'.format(dataset_id=
                                                         dataset_id)

        r = self._call_api(endpoint=endpoint,
                           data_type_id=data_type_id,
                           location_id=location_id,
                           station_id=station_id,
                           start_date=start_date,
                           end_date=end_date,
                           sort_field=sort_field,
                           sort_order=sort_order,
                           limit=limit,
                           offset=offset)

        return r

    def data_categories(self,
                        category_id=None,
                        dataset_id=None,
                        location_id=None,
                        station_id=None,
                        start_date=None,
                        end_date=None,
                        sort_field=None,
                        sort_order='asc',
                        limit=25,
                        offset=0):

        endpoint = 'datacategories'

        if category_id is not None:
            endpoint = endpoint + '/{category_id}'.format(category_id=
                                                          category_id)

        r = self._call_api(endpoint=endpoint,
                           dataset_id=dataset_id,
                           location_id=location_id,
                           station_id=station_id,
                           start_date=start_date,
                           end_date=end_date,
                           sort_field=sort_field,
                           sort_order=sort_order,
                           limit=limit,
                           offset=offset)

        return r

    def data_types(self,
                   type_id=None,
                   dataset_id=None,
                   location_id=None,
                   station_id=None,
                   category_id=None,
                   start_date=None,
                   end_date=None,
                   sort_field=None,
                   sort_order='asc',
                   limit=25,
                   offset=0):

        endpoint = 'datatypes'

        if type_id is not None:
            endpoint = endpoint + '/{type_id}'.format(type_id=
                                                      type_id)

        r = self._call_api(endpoint=endpoint,
                           dataset_id=dataset_id,
                           location_id=location_id,
                           station_id=station_id,
                           start_date=start_date,
                           end_date=end_date,
                           sort_field=sort_field,
                           sort_order=sort_order,
                           limit=limit,
                           offset=offset)

        return r

    def location_categories(self,
                            category_id=None,
                            dataset_id=None,
                            start_date=None,
                            end_date=None,
                            sort_field=None,
                            sort_order='asc',
                            limit=25,
                            offset=0):

        endpoint = 'locationcategories'

        if category_id is not None:
            endpoint = endpoint + '/{category_id}'.format(category_id=
                                                          category_id)

        r = self._call_api(endpoint=endpoint,
                           dataset_id=dataset_id,
                           start_date=start_date,
                           end_date=end_date,
                           sort_field=sort_field,
                           sort_order=sort_order,
                           limit=limit,
                           offset=offset)

        return r

    def locations(self,
                  location_id=None,
                  dataset_id=None,
                  location_category_id=None,
                  data_category_id=None,
                  start_date=None,
                  end_date=None,
                  sort_field=None,
                  sort_order='asc',
                  limit=25,
                  pages=0,
                  offset=0):

        endpoint = 'locations'

        if location_id is not None:
            endpoint = endpoint + '/{location_id}'.format(location_id=
                                                          location_id)

        r = self._call_api(endpoint=endpoint,
                           dataset_id=dataset_id,
                           start_date=start_date,
                           end_date=end_date,
                           location_category_id=location_category_id,
                           data_category_id=data_category_id,
                           sort_field=sort_field,
                           sort_order=sort_order,
                           limit=limit,
                           offset=offset)

        return r

    def stations(self,
                 station_id=None,
                 dataset_id=None,
                 location_id=None,
                 data_category_id=None,
                 data_type_id=None,
                 extent=None,
                 start_date=None,
                 end_date=None,
                 sort_field=None,
                 sort_order='asc',
                 limit=25,
                 pages=None,
                 offset=0):

        endpoint = 'stations'

        if station_id is not None:
            endpoint = endpoint + '/{station_id}'.format(station_id=
                                                         station_id)

        #if pages is not None:
        #    for i in range(0, pages + 1):

        r = self._call_api(endpoint=endpoint,
                           dataset_id=dataset_id,
                           start_date=start_date,
                           end_date=end_date,
                           location_id=location_id,
                           data_category_id=data_category_id,
                           data_type_id=data_type_id,
                           extent=extent,
                           sort_field=sort_field,
                           sort_order=sort_order,
                           limit=limit,
                           offset=offset)

        return r

    def get_data(self,
                 dataset_id,
                 data_type_id=None,
                 location_id=None,
                 station_id=None,
                 start_date=None,
                 end_date=None,
                 units='metric',
                 sort_field=None,
                 sort_order='asc',
                 limit=25,
                 pages=0,
                 offset=0,
                 include_metadata=True):

        endpoint = 'data'

        r = self._call_api(endpoint=endpoint,
                           dataset_id=dataset_id,
                           start_date=start_date,
                           end_date=end_date,
                           location_id=location_id,
                           station_id=station_id,
                           data_type_id=data_type_id,
                           units=units,
                           sort_field=sort_field,
                           sort_order=sort_order,
                           limit=limit,
                           offset=offset,
                           include_metadata=include_metadata)

        return r

    def _call_api(self,
                  endpoint,
                  dataset_id=None,
                  data_type_id=None,
                  location_id=None,
                  station_id=None,
                  location_category_id=None,
                  data_category_id=None,
                  start_date=None,
                  end_date=None,
                  sort_field=None,
                  sort_order=None,
                  limit=None,
                  offset=None,
                  units=None,
                  extent=None,
                  include_metadata=None):

        data = {
            'datasetid': dataset_id,
            'datatypeid': data_type_id,
            'locationid': location_id,
            'stationid': station_id,
            'datacategoryid': data_category_id,
            'locationcategoryid': location_category_id,
            'startdate': start_date,
            'enddate': end_date,
            'units': units,
            'extent': extent,
            'sortfield': sort_field,
            'sortorder': sort_order,
            'limit': limit,
            'offset': offset,
            'includemetadata': include_metadata
        }

        data = {key: val for key, val in data.items() if val is not None}

        r = requests.get(urljoin(self._host, endpoint),
                         params=data,
                         headers=self._api_header)

        return r.json()
