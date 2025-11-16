"""Functions to automate Conda airlines ticketing system."""

import math as m

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seat = ['A','B','C','D']
    for index in range(0,number):
        yield seat[index%4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat = ['A','B','C','D']
    for index in range(1, number + 1):
        if m.ceil(index/4) < 13:
            yield str(m.ceil(index/4)) + seat[index%4 - 1]
        else:
            yield str(m.ceil(index/4) + 1) + seat[index%4 - 1]

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    number = len(passengers)
    assigned_seats = {}
    seat = ['A','B','C','D']
    for index in range(1, number + 1):
        if m.ceil(index/4) < 13:
            assigned_seats[passengers[index - 1]] = str(m.ceil(index/4)) + seat[index%4 - 1]
        else:
            assigned_seats[passengers[index - 1]] = str(m.ceil(index/4) + 1) + seat[index%4 - 1]
    
    return assigned_seats

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        new = seat + flight_id 
        yield new + '0' * (12 - len(new))
