from datetime import datetime
from numpy import double, string_
from constants import *

class ParkingTicket:
    def __init__(self, ticketNumber: string_, issuedAt: datetime, payedAt: datetime, payedAmount: double, status: ParkingTicketStatus):
        self.ticketNumber = ticketNumber
        self.issuedAt = issuedAt
        self.payedAt = payedAt
        self.payedAmount = payedAmount
        self.status = status