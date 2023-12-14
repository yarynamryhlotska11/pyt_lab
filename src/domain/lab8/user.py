"""
The User class represents a user entity with attributes such as first name, last name, company name, address, city,
country, state, ZIP code, phone numbers, and email.

Usage:
Instantiate the class by passing a list of user data.
Access user attributes using the provided getter methods (e.g., user.first_name(), user.email()).

Example:
data = ['John', 'Doe', 'ABC Company', '123 Street', 'Anytown', 'Country', 'State', '12345', '123-456-7890',
'987-654-3210', 'john@example.com']
user = User(data)
print(user.first_name())  # Output: John
print(user.email())       # Output: john@example.com
print(user)               # Output: John Doe ABC Company 123 Street Anytown Country State 12345 123-456-7890 987-654-3210 john@example.com
"""


class User:
    def __init__(self, data):
        self.__first_name = data[0]
        self.__last_name = data[1]
        self.__company_name = data[2]
        self.__address = data[3]
        self.__city = data[4]
        self.__country = data[5]
        self.__state = data[6]
        self.__zip = data[7]
        self.__phone1 = data[8]
        self.__phone2 = data[9]
        self.__email = data[10]

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def company_name(self):
        return self.__company_name

    @property
    def state(self):
        return self.__state

    @property
    def city(self):
        return self.__city

    @property
    def country(self):
        return self.__country

    @property
    def email(self):
        return self.__email

    @property
    def phone1(self):
        return self.__phone1

    @property
    def phone2(self):
        return self.__phone2

    @property
    def address(self):
        return self.__address

    @property
    def zip(self):
        return self.__zip

    def __str__(self):
        return (f"{self.__first_name} {self.__last_name} {self.__company_name} {self.__address} "
                f"{self.__city} {self.__country} {self.__state} "
                f"{self.zip} {self.__phone1} {self.__phone2} {self.__email}")

