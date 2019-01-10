# description: 易读的时间段表示
# author: C.v.
# href: https://www.codewars.com/kata/human-readable-duration-format
# date: 2019-1-9


second = 1
minute = 60
hour = 3600
day = 3600 * 24
year = 3600 * 24 * 365


def format_duration(seconds):
    if seconds == 0:
        return 'now'
    dis = ["", seconds]
    screen(dis, year, "year")
    screen(dis, day, "day")
    screen(dis, hour, "hour")
    screen(dis, minute, "minute")
    screen(dis, second, "second")
    res = dis[0]
    k = res.rfind(",")
    return res if k == -1 else res[:k] + " and" + res[k+1:]


def screen(dis, option, optionStr):
    temp = dis[1] // option
    dis[1] = dis[1] % option
    if temp != 0:
        dis[0] = append(dis[0], temp, optionStr)


def append(res, number, option):
    if res != "":
        res += ", "
    res += str(number) + " " + option
    return res if number == 1 else res + "s"


print(format_duration(60))


