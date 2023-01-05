# Задача №1.

# Написать метод domain_name, который вернет домен из url адреса:

# url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# url = "https://www.cnet.com"                -> domain name = "cnet"

# Основа:

def domain_name(url):
    if url.startswith("h"):
        url = url[url.find("://") + 3:]

    if url.startswith("w"):
        url = url[url.find(".") + 1:]

    while url.rfind(".") != -1:
        url = url[:url.find(".")]

    print("domain:", url)
    return url

# Для проверки:


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("https://www.cnet.com") == "cnet"
assert domain_name("https://www.w3schools.com/python/ref_string_find.asp") == "w3schools"
assert domain_name("https://hh.ru/applicant/negotiations") == "hh"
assert domain_name("https://duckduckgo.com/")
assert domain_name("https://university.ylab.io/")
