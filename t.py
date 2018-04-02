import urllib.request
import simplejson
token='8_fNpeYcGJbX6WLCN5Je9MeEW1HD_LSVJGaXGgnWLRFdCFf5pyNnbxkED5UVtwMSb_jTdIbOM8m9C2exnPx1fWMUoo9SNbS6vQ1m3od-f3IXnrs5VpoPCykes1YvdWlue4Hpf-dypGRPEcN6lFLHSiAIAVRC'

url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token='+token
data='{"button":[{"type":"click","name":"开门","key":"TURNON"}]}'
data = simplejson.dumps(data, ensure_ascii=False)  # .encode('utf-8')

# 加上参数ensure_ascii=False 后 提交的数据中的中文就不会再被转码

print(data)
a=b'{"button":[{"type":"click","name":"\xe5\xbc\x80\xe9\x97\xa8","key":"TURNON"}]}""'
req = urllib.request.Request(url)

req.add_header('Content-Type', 'application/json')

req.add_header('encoding', 'utf-8')

response = urllib.request.urlopen(req, a)

result = response.read()

print(result)