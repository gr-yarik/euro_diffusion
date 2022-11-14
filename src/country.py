from typing import List
from .city import City


class Country:
    def __init__(self, name: str):
        self.name = name
        self.cities: List[City] = []
        self.full = False
        self.day_of_full = -1

    def __eq__(self, other):
        return self.day_of_full == other.day_of_full

    def __lt__(self, other):
        return self.day_of_full < other.day_of_full

    def append_city(self, city: City) -> None:
        self.cities.append(city)

    def check_fullness(self, day) -> None:
        if self.full:
            return
        for city in self.cities:
            if city.full is False:
                return
        self.full = True
        self.day_of_full = day

    def has_foreign_neighbours(self) -> bool:
        for city in self.cities:
            for neighbour in city.neighbours:
                if neighbour.country_name != self.name:
                    return True

    def only_country_mode(self) -> None:
        self.full = True
        self.day_of_full = 0

        
class City:
    def __init__(self, country_name: str, countries_list: list, x: int, y: int):
        self.country_name = country_name
        self.x = x
        self.y = y
        self.balance = {city_data["name"]: 0 for city_data in countries_list}
        self.balance[country_name] = initial_city_balance
        self.balance_per_day = {city_data["name"]: 0 for city_data in countries_list}
        self.neighbours: List['City'] = []
        self.full = False

    def set_neighbours(self, neighbours: List['City']) -> None:
        self.neighbours = neighbours

    def transfer_to_neighbours(self) -> None:
        for motif in self.balance:
            balance_of_motif = self.balance[motif]
            amount_to_transfer = balance_of_motif // representative_portion
            if amount_to_transfer > 0:
                for neighbour in self.neighbours:
                    self.balance[motif] -= amount_to_transfer
                    neighbour.add_balance_in_motif(motif, amount_to_transfer)

    def add_balance_in_motif(self, motif: str, amount: int) -> None:
        self.balance_per_day[motif] += amount

    def finalize_balance_per_day(self) -> None:
        for motif in self.balance_per_day:
            self.balance[motif] += self.balance_per_day[motif]
            self.balance_per_day[motif] = 0

        if not self.full:
            for motif in self.balance_per_day:
                if self.balance[motif] == 0:
                    return
            self.full = True
