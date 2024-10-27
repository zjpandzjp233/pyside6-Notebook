#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# 机器翻译 WebAPI 接口调用示例
# 运行前：请先填写Appid、APIKey、APISecret
# 运行方法：直接运行 main 即可 
# 结果： 控制台输出结果信息
# 
# 1.接口文档（必看）：https://www.xfyun.cn/doc/nlp/xftrans/API.html
# 2.错误码链接：https://www.xfyun.cn/document/error-code （错误码code为5位数字）
#
import requests
import datetime
import hashlib
import base64
import hmac
import json

class get_result(object):
    def __init__(self,host):
        # 应用ID（到控制台获取）
        self.APPID = "fc3ef622"
        # 接口APISercet（到控制台机器翻译服务页面获取）
        self.Secret = "NmY3YTU2MTU4MjYwNjQwYTBlMWFlNmU4"
        # 接口APIKey（到控制台机器翻译服务页面获取）
        self.APIKey= "905d16f27407a70920dd5da4798a167b"
        
        
        # 以下为POST请求
        self.Host = host
        self.RequestUri = "/v2/its"
        # 设置url
        # print(host)
        self.url="https://"+host+self.RequestUri
        self.HttpMethod = "POST"
        self.Algorithm = "hmac-sha256"
        self.HttpProto = "HTTP/1.1"

        # 设置当前时间
        curTime_utc = datetime.datetime.utcnow()
        self.Date = self.httpdate(curTime_utc)
        # 设置业务参数
        # 语种列表参数值请参照接口文档：https://www.xfyun.cn/doc/nlp/xftrans/API.html
        self.Text="自然语言处理"
        self.BusinessArgs={
                "from": "cn",
                "to": "en",
            }

    def hashlib_256(self, res):
        m = hashlib.sha256(bytes(res.encode(encoding='utf-8'))).digest()
        result = "SHA-256=" + base64.b64encode(m).decode(encoding='utf-8')
        return result

    def httpdate(self, dt):
        """
        Return a string representation of a date according to RFC 1123
        (HTTP/1.1).

        The supplied date must be in UTC.

        """
        weekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][dt.weekday()]
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
                 "Oct", "Nov", "Dec"][dt.month - 1]
        return "%s, %02d %s %04d %02d:%02d:%02d GMT" % (weekday, dt.day, month,
                                                        dt.year, dt.hour, dt.minute, dt.second)

    def generateSignature(self, digest):
        signatureStr = "host: " + self.Host + "\n"
        signatureStr += "date: " + self.Date + "\n"
        signatureStr += self.HttpMethod + " " + self.RequestUri \
                        + " " + self.HttpProto + "\n"
        signatureStr += "digest: " + digest
        signature = hmac.new(bytes(self.Secret.encode(encoding='utf-8')),
                             bytes(signatureStr.encode(encoding='utf-8')),
                             digestmod=hashlib.sha256).digest()
        result = base64.b64encode(signature)
        return result.decode(encoding='utf-8')

    def init_header(self, data):
        digest = self.hashlib_256(data)
        #print(digest)
        sign = self.generateSignature(digest)
        authHeader = 'api_key="%s", algorithm="%s", ' \
                     'headers="host date request-line digest", ' \
                     'signature="%s"' \
                     % (self.APIKey, self.Algorithm, sign)
        #print(authHeader)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Method": "POST",
            "Host": self.Host,
            "Date": self.Date,
            "Digest": digest,
            "Authorization": authHeader
        }
        return headers

    def get_body(self):
        content = str(base64.b64encode(self.Text.encode('utf-8')), 'utf-8')
        postdata = {
            "common": {"app_id": self.APPID},
            "business": self.BusinessArgs,
            "data": {
                "text": content,
            }
        }
        body = json.dumps(postdata)
        #print(body)
        return body
    def call_url(self):
        if self.APPID == '' or self.APIKey == '' or self.Secret == '':
            print('Appid 或APIKey 或APISecret 为空！请打开demo代码，填写相关信息。')
        else:
            code = 0
            body=self.get_body()
            headers=self.init_header(body)
            #print(self.url)
            response = requests.post(self.url, data=body, headers=headers,timeout=8)
            status_code = response.status_code
            #print(response.content)
            if status_code!=200:
                # 鉴权失败
                print("Http请求失败，状态码：" + str(status_code) + "，错误信息：" + response.text)
                print("请根据错误信息检查代码，接口文档：https://www.xfyun.cn/doc/nlp/xftrans/API.html")
            else:
                # 鉴权成功
                respData = json.loads(response.text)
                print(respData)
                # 以下仅用于调试
                code = str(respData["code"])
                if code!='0':
                    print("请前往https://www.xfyun.cn/document/error-code?code=" + code + "查询解决办法")
                return respData

if __name__ == '__main__':
    ##示例:  host="itrans.xfyun.cn"域名形式
    host = "itrans.xfyun.cn"
    #初始化类
    gClass=get_result(host)
    gClass.call_url()


"""
汉语普通话	cn	波斯语	fa	僧伽罗语	si
英语	en	芬兰语	fi	斯洛伐克语	sk
彝语	ii	希伯来语	he	斯洛文尼亚语	sl
广东话	yue	印地语	hi	塞尔维亚语	sr
日语	ja	克罗地亚语	hr	巽他语	su
俄语	ru	匈牙利语	hu	瑞典语	sv
法语	fr	亚美尼亚语	hy	斯瓦希里语	sw
西班牙语	es	印尼语	id	泰米尔语	ta
阿拉伯语	ar	冰岛语	is	泰卢固语	te
意大利语	it	塔加路语（菲律宾）	tl	爪哇语	jv
土耳其语	tr	罗马尼亚语	ro	马来语	ms
越南语	vi	格鲁吉亚语	ka	乌克兰语	uk
泰语	th	高棉语	km	乌尔都语	ur
韩语	ko	老挝语	lo	南非祖鲁语	zu
德语	de	立陶宛语	lt	内蒙语	mn
哈萨克语	kka	拉脱维亚语	lv	缅甸语	my
南非荷兰语	af	马拉雅拉姆语	ml	外蒙语	nm
阿姆哈拉语	am	马拉地语	mr	普什图语	ps
阿塞拜疆语	az	博克马尔挪威语	nb	豪萨语	ha
孟加拉语	bn	尼泊尔语	ne	乌兹别克语	uz
加泰罗尼亚语	ca	荷兰语	nl	土库曼语	tk
捷克语	cs	波兰语	pl	塔吉克语	tg
丹麦语	da	葡萄牙语	pt	保加利亚语	bg
希腊语	el				
#常见问题
"""