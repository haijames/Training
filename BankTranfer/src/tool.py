import datetime
import math
import re
import BankTranfer.Settings.config as cf


def checkNaN(row):
    """
    chekings NaN values
    :param row:
    :return:
    """
    try:
        if math.isnan(row):
            return True
    except TypeError:
        return False


def check_mail(data):
    """
    checking mail values
    :param data:
    :return: number of validated row and list of bug(index)
    """
    regex = cf.reg
    count = 0
    bug = []
    for index, row in data:
        if checkNaN(row):
            continue
        if re.fullmatch(regex, row):
            count += 1
        else:
            bug.append(index+2)
    return count, bug


def check_date(data):
    """
    checking date values
    :param data:
    :return: number of validated row and list of bug(index)
    """
    count = 0
    bug = []
    for index, row in data:
        if checkNaN(row):
            continue
        if ('/' in row) or ('-' in row):
            try:
                date_obj = datetime.datetime.strptime(row, "%d-%b-%y")
                count += 1
            except ValueError:
                try:
                    date_obj = datetime.datetime.strptime(row, "%m/%d/%Y")
                    count += 1
                except ValueError:
                    bug.append(index+2)
        else:
            bug.append(index+2)
    return count, bug


def check_num(data):
    """
    cheking number values
    :param data:
    :return: number of validated row and list of bug(index)
    """
    count = 0
    bug = []
    for index, row in data:
        if checkNaN(row):
            continue
        if row.isnumeric():
            count += 1
        else:
            bug.append(index+2)
    return count, bug
