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
"""
from datetime import datetime


from configuration.logger_config import logger


class DateProcessor:
    """
        DateProcessor class for handling date-related operations.
    """

    @staticmethod
    def parse_dateformat(date_value: str, date_format: str) -> datetime:
        """
        Parses the input date string using the specified format and returns a datetime object.
        """
        if not isinstance(date_value, str):
            logger.error("Wrong data type: %s. It has to be string!", type(date_value))
            raise ValueError("Wrong data type!")
        return datetime.strptime(date_value, date_format)
