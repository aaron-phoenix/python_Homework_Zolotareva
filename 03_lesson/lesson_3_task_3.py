from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "15", "25")
from_address = Address("456321", "СПб", "Невский", "10", "5")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=250,
    track="RB123456789CN"
)

print(f"{mailing.track}, из {mailing.to_address}, - в {mailing.from_address}")
