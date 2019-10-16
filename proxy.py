import requests

def GET(url, params=None):
    proxies = {
        'http': "socks5://127.0.0.1:1080",
        'https': "socks5://127.0.0.1:9150"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko'
    }
    req = requests.get(url, params=params, proxies=proxies, headers=headers)
    return req


def POST(url, data, files=None):
    proxies = {
        'http': "socks5://127.0.0.1:1080",
        'https': "socks5://127.0.0.1:9150"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko'
    }
    req = requests.post(url, data = data, proxies=proxies, headers=headers, files=files)
    return req
