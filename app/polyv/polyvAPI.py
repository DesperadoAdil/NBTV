from polyv import const
from polyv import md5
import urllib3
import time

SCENE_ALONE = "alone" # 活动拍摄
SCENE_PPT = "ppt" # 三分屏
SCENE_TOPCLASS = "topclass" # 大班课

class ChannelManager:
	def __init__(self):
		self.sender = urllib3.PoolManager()
		pass

	def getTimeMillis(self):
		t = time.time()
		return int(round(t * 1000))

	def generateSign(self, params, secret):
		ansStr = secret
		for key in sorted(params):
			ansStr += str(key) + str(params[key])
		ansStr += secret
		print("generateSign:", ansStr)
		return md5.toMD5(ansStr)
		

	def createChannel(self, name, passwd = None, sceneType = SCENE_ALONE):
		'''返回API 返回内容'''
		params = {"appId": const.AppID, "channelPasswd": passwd, "name": name, "timestamp": str(self.getTimeMillis()), "userId": const.UserID, "scene": sceneType}

		sign = self.generateSign(params, const.AppSecret)
		params["sign"] = sign

		data = self.sender.request("POST", const.CreateChannelUrl, fields= params)
		return data


	def getChannelInfo(self, channelId):
		url = const.GetChannelInfoUrl % channelId
		timestamp = str(self.getTimeMillis())
		params = {"appId": const.AppID, "timestamp": timestamp}
		sign = self.generateSign(params, const.AppSecret)

		url = url + "?appId=%s&sign=%s&timestamp=%s" % (const.AppID, sign, timestamp)
		data = self.sender.request("GET", url)
		return data
