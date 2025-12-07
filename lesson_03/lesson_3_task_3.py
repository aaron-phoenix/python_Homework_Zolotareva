from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "Ленина", "15", "25")
from_addr = Address("456321", "СПб", "Невский", "10", "5")

mail = Mailing(
    to_addr=to_addr,
    from_addr=from_addr,
    cost=250,
    track="RB123456789CN"
)
print(f"{mail.track}, из {mail.to_addr}, - в {mail.from_addr}")
