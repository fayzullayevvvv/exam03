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
        self.seat.is_taken = True


class CinemaSession:

    def __init__(self, movie_title: str, total_seats: int):
        if not movie_title or movie_title.strip() == "":
            raise ValueError()
        if total_seats <= 0:
            raise ValueError()
        
        self.movie_title = movie_title
        self.total_seats = total_seats
        self.seats = [Seat(i) for i in range(1, total_seats + 1)]
        self.bookings = []

    def available_seats(self) -> list[int]:
        result = [seat.number for seat in self.seats if not seat.is_taken]
        return result

    def book_seat(self, seat_number: int, user: str) -> Ticket:
        if not 1 <= seat_number <= self.total_seats:
            raise ValueError()
        
        seat = self.seats[seat_number - 1]

        if seat.is_taken:
            raise RuntimeError()

        ticket = Ticket(seat, user)
        self.bookings.append(ticket)

        return ticket
    
    def __str__(self) -> str:
        return f"CinemaSession: {self.movie_title} ({self.total_seats} seats)"