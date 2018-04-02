#coding = utf-8
import requests
import urllib.parse
import json
import urllib3.request
import urllib3
import simplejson
token='8_fNpeYcGJbX6WLCN5Je9MeEW1HD_LSVJGaXGgnWLRFdCFf5pyNnbxkED5UVtwMSb_jTdIbOM8m9C2exnPx1fWMUoo9SNbS6vQ1m3od-f3IXnrs5VpoPCykes1YvdWlue4Hpf-dypGRPEcN6lFLHSiAIAVRC'
url='https://api.weixin.qq.com/cgi-bin/menu/create?access_token='+token
t='{"button":[{"type":"click","name":"'+'开门'+'","key":"TURNON"}]}'
t = json.loads(t.encode('utf-8'))
res=requests.post(url,json=bytes(str(t),'utf-8'))
# res=requests.get('https://api.weixin.qq.com/cgi-bin/menu/delete?access_token='+token)
print(res.text)
print(t)
