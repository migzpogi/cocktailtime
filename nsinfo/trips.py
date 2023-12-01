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


api_key = '0b5f530464684a33a9ffc0594b3a5bcd'
headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}


def flask_landing():
    return "nsinfo landing"


def get_stations():
    url = f"https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/stations?countryCodes=nl"
    stations = Stations(requests.get(url, headers=headers).json())
    print(stations.find_station_by_name("Bloemendaal"))
    print(stations.find_station_by_name("Amsterdam Centraal"))
    print(stations.find_station_by_name("Zandvoort aan Zee"))


def get_trips(from_uic, to_uic):
    url = f"https://gateway.apiportal.ns.nl/reisinformatie-api/api/v3/trips?originUicCode=8400058&destinationUicCode=8400733&originWalk=false&originBike=false&originCar=false&destinationWalk=false&destinationBike=false&destinationCar=false&dateTime=2023-08-01T16:00:00%2B0200&shorterChange=false&travelAssistance=false&searchForAccessibleTrip=false&localTrainsOnly=false&excludeHighSpeedTrains=false&excludeTrainsWithReservationRequired=false&product=GEEN&discount=NO_DISCOUNT&travelClass=2&passing=false&travelRequestType=DEFAULT"
    r = requests.get(url, headers=headers)
    print(r.json())


def get_departures(uic_from):
    url = f"https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/departures?uicCode={uic_from}&dateTime=2023-08-01T16:00:00%2B0200"
    # url = f"https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/departures?uicCode={uic_from}&dateTime=2023-08-01T00:00:00+0000"
    r = requests.get(url, headers=headers)
    print(r.json())


# 8400118 Bloemendaal
# 8400058 Amsterdam Centraal
# 8400733 Zandvoort aan Zee


# get_stations()
# get_trips('8400058', '8400733')
# get_departures(8400118)


def scrape():
    r = requests.get("https://www.rijdendetreinen.nl/en/train-archive/2023-08-01/5469")
    print(r.text)

scrape()