import urllib3

if __name__ == '__main__':
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://www.baidu.com')
    f = open('abc.html', 'w')
    # bytes to str, str to bytes use str.encode('utf-8')
    f.write(r.data.decode('utf-8')) 
    f.close()