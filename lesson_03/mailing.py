from address import Address


class Mailing:
    def __init__(self, to_addr: Address, from_addr: Address, cost: int, track: str):
        self.to_addr = to_addr
        self.from_addr = from_addr
        self.cost = cost
        self.track = track
