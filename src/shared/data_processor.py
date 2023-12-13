"""
Data Processor Module

This module provides a DateProcessor class for handling date-related operations.

Methods:
- parse_dateformat(date: str, date_format: str) -> datetime:
    Parses the input date string using the specified format and
    returns a datetime object.

- calculate_year_difference(dt: datetime) -> int:
    Calculates the difference in years between the input date and
    the current date.

Example:
>>> date_processor = DateProcessor()
>>> parsed_date = date_processor.parse_dateformat("2023-01-01", "%Y-%m-%d")
>>> age = date_processor.calculate_year_difference(parsed_date)
>>> print(age)
1
"""
from datetime import datetime, date

from dateutil.relativedelta import relativedelta

from configuration.logger_config import logger


class DateProcessor:

    @staticmethod
    def parse_dateformat(date_value: str, date_format: str) -> datetime:

        if not isinstance(date_value, str):
            logger.error("Wrong data type: %s. It has to be string!", type(date_value))
            raise ValueError("Wrong data type!")
        return datetime.strptime(date_value, date_format)

    @staticmethod
    def calculate_year_difference(dt: date) -> int:

        if not isinstance(dt, date):
            logger.error("Wrong data type: %s. It has to be datetime!",
                         type(dt))
            raise ValueError("Wrong data type!")
        return relativedelta(datetime.now(), dt).years
