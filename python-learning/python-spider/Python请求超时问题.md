
## 问题阐述

```bash
使用requests库请求API接口时，时不时会报requests.exceptions.ReadTimeout: HTTPConnectionPool(host='beta.service.xiaolabot.com', port=80): Read timed out. (read timeout=5)
```

```bash
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/connectionpool.py", line 386, in _make_request
six.raise_from(e, None)
File "", line 2, in raise_from
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/connectionpool.py", line 382, in _make_request
httplib_response = conn.getresponse()
File "/usr/local/python3.6/lib/python3.6/http/client.py", line 1331, in getresponse
response.begin()
File "/usr/local/python3.6/lib/python3.6/http/client.py", line 297, in begin
version, status, reason = self._read_status()
File "/usr/local/python3.6/lib/python3.6/http/client.py", line 258, in _read_status
line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
File "/usr/local/python3.6/lib/python3.6/socket.py", line 586, in readinto
return self._sock.recv_into(b)
socket.timeout: timed out

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/requests/adapters.py", line 440, in send
timeout=timeout
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/connectionpool.py", line 649, in urlopen
_stacktrace=sys.exc_info()[2])
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/util/retry.py", line 357, in increment
raise six.reraise(type(error), error, _stacktrace)
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/packages/six.py", line 686, in reraise
raise value
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/connectionpool.py", line 600, in urlopen
chunked=chunked)
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/connectionpool.py", line 388, in _make_request
self._raise_timeout(err=e, url=url, timeout_value=read_timeout)
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/connectionpool.py", line 308, in _raise_timeout
raise ReadTimeoutError(self, url, "Read timed out. (read timeout=%s)" % timeout_value)
urllib3.exceptions.ReadTimeoutError: HTTPConnectionPool(host='beta.service.xiaolabot.com', port=80): Read timed out. (read timeout=5)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
File "/data/python_server/code/xiaolabot/library/utils/rpc.py", line 42, in rpc
timeout=timeout
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/requests/api.py", line 112, in post
return request('post', url, data=data, json=json, **kwargs)
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/requests/api.py", line 58, in request
return session.request(method=method, url=url, **kwargs)
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/requests/sessions.py", line 502, in request
resp = self.send(prep, **send_kwargs)
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/requests/sessions.py", line 612, in send
r = adapter.send(request, **kwargs)
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/requests/adapters.py", line 516, in send
raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: HTTPConnectionPool(host='beta.service.xiaolabot.com', port=80): Read timed out. (read timeout=5)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
File "/data/python_server/code/xiaolabot/service/application/jobs/wechat.py", line 101, in update_wechat_keywords
response = rpc('service/wechat/get_authorizer_info', {'appid': appid})
File "/data/python_server/code/xiaolabot/library/utils/rpc.py", line 50, in rpc
raise Exception(traceback.format_exc())
Exception: Traceback (most recent call last):
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/connectionpool.py", line 386, in _make_request
six.raise_from(e, None)
File "", line 2, in raise_from
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/connectionpool.py", line 382, in _make_request
httplib_response = conn.getresponse()
File "/usr/local/python3.6/lib/python3.6/http/client.py", line 1331, in getresponse
response.begin()
File "/usr/local/python3.6/lib/python3.6/http/client.py", line 297, in begin
version, status, reason = self._read_status()
File "/usr/local/python3.6/lib/python3.6/http/client.py", line 258, in _read_status
line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
File "/usr/local/python3.6/lib/python3.6/socket.py", line 586, in readinto
return self._sock.recv_into(b)
socket.timeout: timed out

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/requests/adapters.py", line 440, in send
timeout=timeout
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/connectionpool.py", line 649, in urlopen
_stacktrace=sys.exc_info()[2])
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/util/retry.py", line 357, in increment
raise six.reraise(type(error), error, _stacktrace)
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/packages/six.py", line 686, in reraise
raise value
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/connectionpool.py", line 600, in urlopen
chunked=chunked)
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/connectionpool.py", line 388, in _make_request
self._raise_timeout(err=e, url=url, timeout_value=read_timeout)
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/urllib3/connectionpool.py", line 308, in _raise_timeout
raise ReadTimeoutError(self, url, "Read timed out. (read timeout=%s)" % timeout_value)
urllib3.exceptions.ReadTimeoutError: HTTPConnectionPool(host='beta.service.xiaolabot.com', port=80): Read timed out. (read timeout=5)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
File "/data/python_server/code/xiaolabot/library/utils/rpc.py", line 42, in rpc
timeout=timeout
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/requests/api.py", line 112, in post
return request('post', url, data=data, json=json, **kwargs)
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/requests/api.py", line 58, in request
return session.request(method=method, url=url, **kwargs)
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/requests/sessions.py", line 502, in request
resp = self.send(prep, **send_kwargs)
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/requests/sessions.py", line 612, in send
r = adapter.send(request, **kwargs)
File "/home/lmb_ai/.virtualenvs/pyenv3.6/lib/python3.6/site-packages/requests/adapters.py", line 516, in send
raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: HTTPConnectionPool(host='beta.service.xiaolabot.com', port=80): Read timed out. (read timeout=5)
```

## 问题出现原因

```bash
http连接太多没有关闭导致的
```

## 如何解决

>增加重试连接次数

```bash
requests.adapters.DEFAULT_RETRIES = 5
```

>关闭多余的连接

requests使用了urllib3库，默认的http connection是keep-alive的，requests设置False关闭

```bash
s = requests.session()
s.keep_alive = False
```

## 使用grequests实现异步请求

```bash
pip install grequests
```

```bash
import grequests

urls = [
    'http://www.url1.com',
    'http://www.url2.com',
    'http://www.url3.com',
    'http://www.url4.com',
    'http://www.url5.com',
    'http://www.url6.com',
]

resp = (grequests.get(u) for u in urls)
grequests.map(resp)
```

```bash
[<Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>]
```
