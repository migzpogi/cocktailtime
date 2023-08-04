import requests


class Station(object):
    def __init__(self, station):
        self.uiccode = station['UICCode']
        self.stationtype = station['stationType']
        self.long_name = station['namen']['lang']

    def __str__(self):
        return f"{self.uiccode} {self.long_name}"


class Stations(object):
    def __init__(self, response):
        self.response = response['payload']
        self.list_of_stations = []
        self.__process_stations()

    def __process_stations(self):
        for r in self.response:
            self.add_station(Station(r))

    def add_station(self, station):
        self.list_of_stations.append(station)

    def print_stations(self):
        for i in self.list_of_stations:
            print(i)

    def number_of_stations(self):
        return len(self.list_of_stations)

    def find_station_by_name(self, name):
        for i in self.list_of_stations:
            if name.lower() == i.long_name.lower():
                return(i)


api_key = 'some-random-key'
headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}


def get_stations():

    limit = 1
    url = f"https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/stations?countryCodes=nl&limit={limit}"
    stations = Stations(requests.get(url, headers=headers).json())
    print(stations.find_station_by_name("Bloemendaal"))
    print(stations.find_station_by_name("Amsterdam Centraal"))



get_stations()