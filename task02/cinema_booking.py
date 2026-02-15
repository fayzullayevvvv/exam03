class Seat:

    def __init__(self, number: int):
        if number <= 0:
            raise ValueError()
        
        self.number = number
        self.is_taken = False


class Ticket:

    def __init__(self, seat: Seat, owner: str):
        if not owner or owner.strip() == "":
            raise ValueError()
        if seat.is_taken:
            raise ValueError()
        
        self.seat = seat
        self.owner = owner


class CinemaSession:

    def __init__(self, movie_title: str, total_seats: int):
        if movie_title is None:
            raise ValueError()
        if total_seats < 0:
            raise ValueError()
        
        self.movie_title = movie_title,
        self.total_seats = total_seats
        self.seats = []
        self.bookings = []