# description: 从url中抽取域名
# author: C.v.
# href: https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1
# date: 2019-1-3


# def domain_name(url):
#     temp = url.split('/')[2].split(".") if url.startswith("http") else url.split(".")
#     return temp[1] if temp[0] == "www" else temp[0]


def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


print(domain_name("http://aaa.com"))
print(domain_name("www.xakep.ru"))

