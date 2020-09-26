# coding=utf-8

import pyutils

import time
import datetime


class TimeUtil:

    # 1.把字符串转成时间戳形式
    @staticmethod
    def str_toStamp(strTime, fmt="%Y-%m-%d %H:%M:%S"):
        timeArray = time.strptime(strTime, fmt)
        timestamp = time.mktime(timeArray)
        timestamp = int(timestamp)
        return timestamp
    # 方法2
    # @staticmethod
    # def str_toTimestamp(strTime):
    #     timestamp = time.mktime(TimeUtil.string_toDatetime(strTime).timetuple())
    #     print(timestamp)
    #     return timestamp

    # 2.把字符串转成datetime

    @staticmethod
    def str_toDt(strTime, fmt="%Y-%m-%d %H:%M:%S"):
        dt = datetime.datetime.strptime(strTime, fmt)
        return dt

    # #把字符串转成datetime
    # @staticmethod
    # def strtoDt(string):
    #     dt = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    #     dt = dt.strftime("%Y-%m-%d %H")
    #     print(dt)
    #     return dt

    # 3.把时间戳转成字符串形式

    @staticmethod
    def stamp_toStr(stamp, fmt="%Y-%m-%d %H:%M:%S"):
        # 转换成localtime
        time_local = time.localtime(stamp)
        # 转换成新的时间格式(2017-09-16 11:28:54)
        strTime = time.strftime(fmt, time_local)
        return strTime

    # 4.把datetime类型转成时间戳形式

    @staticmethod
    def dt_toStamp(dt):
        stamp = time.mktime(dt.timetuple())
        stamp = int(stamp)
        return stamp

    # 5.把datetime类型转成字符串

    @staticmethod
    def dt_toStr(dt, fmt="%Y-%m-%d %H:%M:%S"):
        strTime = dt.strftime(fmt)

        return strTime

    # 字符串转时间戳带精确度
    @staticmethod
    def str_toStamp_acc(strTime, fmt="%Y-%m-%d %H"):
        dt = TimeUtil.str_toDt(strTime)
        strTime_acc = TimeUtil.dt_toStr(dt, fmt)
        stamp = TimeUtil.str_toStamp(strTime_acc, fmt)
        return stamp


if __name__ == '__main__':
    strTime = '2017-09-16 11:28:54'
    t = 1505532534
    # TimeUtil.string_toTimestamp(s)
    # TimeUtil.str_toStamp_acc(strTime)
    stamp1 = TimeUtil.str_toStamp(strTime)
    print(stamp1)
    strTime2 = '2017-09-18 11:28:54'
    stamp2 = TimeUtil.str_toStamp(strTime2)
    print(stamp2)
    print(stamp2-stamp1)
