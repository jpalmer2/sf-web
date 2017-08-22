"""
Misc functions for cleaning up data and other utility functions
"""

def sf_time_to_datetime(sf_time):
    """
    sf_time_to_datetime :: str -> datetime

    Parse the date format that Salesforce returns into a standard python time tuple
    Accepts a string containing a Salesforce timestamp
    Returns a python datetime object
    """
    
    from datetime import datetime
    from dateutil import tz

    # Ugly string munging
    left, right = sf_time.split('T')
    right_left, right_right = right.split('.')
    year, month, day = left.split('-')
    hour, minute, second = right_left.split(':')
    utc_offset = right_right[3:]
    microsecond = right_right[:3]

    s_datetuple = (year, month, day, hour, minute, second, microsecond)
    datetuple = map(int, s_datetuple)

    return datetime(*datetuple).replace(tzinfo=tz.tzutc())

"""
>>> maybe_t = sf_time_to_datetime('2017-06-07T18:53:58.000+0000').tzinfo
>>> abs(datetime.datetime.now(maybe_t)  - sf_time_to_datetime('2017-06-07T18:53:58.000+0000')).total_seconds()
277039.390925
"""

def ticket_age(sf_time):
    """
    ticket_age :: str -> num
    Calculate time elapsed
    Accept a string containing a Salesforce timestamp
    Return the number of minutes elapsed
    """
    from datetime import datetime
    dt = sf_time_to_datetime(sf_time)
    elapsed_sec = abs(datetime.now(dt.tzinfo) - dt).total_seconds()
    return elapsed_sec/60

def sf_time_diff(sf_time1, sf_time2):
    """
    sf_time_diff :: str -> str -> num
    Calculate the amount of time elapsed between 2 salesforce timestamps
    Accepts two strings containing Salesforce timestamps
    Return the number of minutes elapsed
    """

    dt1 = sf_time_to_datetime(sf_time1)
    dt2 = sf_time_to_datetime(sf_time2)
    elapsed_sec = (dt1 - dt2).total_seconds()
    return elapsed_sec / 60
