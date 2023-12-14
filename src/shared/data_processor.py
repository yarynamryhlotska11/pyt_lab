
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
