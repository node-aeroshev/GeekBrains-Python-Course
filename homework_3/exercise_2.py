
def foo(name: str,
        surname: str,
        birthday: str,
        city: str,
        email: str,
        phone: str
        ) -> None:
    print(f"name: {name}\n"
          f"surname: {surname}\n"
          f"birthday: {birthday}\n"
          f"city: {city}\n"
          f"email: {email}\n"
          f"phone: {phone}\n")


# Test case
foo(phone='88005535',
    name='John',
    email='sample@mail.com',
    birthday='01.01.1990',
    city='Los Angeles',
    surname='Lebovski')

foo(name='sample',
    city='sample',
    email='sample',
    surname='mock',
    birthday='mock',
    phone='empty')
