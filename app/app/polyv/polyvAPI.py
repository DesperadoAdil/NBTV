from . import const
from . import md5
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
		return str(int(round(t * 1000)))

	def generateSign(self, params, secret):
		ansStr = secret
		for key in sorted(params):
			ansStr += str(key) + str(params[key])
		ansStr += secret
		print("generateSign:", ansStr)
		return md5.toMD5(ansStr)
		

	def createChannel(self, name, passwd = "", sceneType = SCENE_ALONE):
		'''返回API 返回内容'''
		params = {"appId": const.AppID, "channelPasswd": passwd, "name": name, "timestamp": str(self.getTimeMillis()), "userId": const.UserID, "scene": sceneType}

		sign = self.generateSign(params, const.AppSecret)
		params["sign"] = sign

		data = self.sender.request("POST", const.CreateChannelUrl, fields= params)
		return data


	def getChannelInfo(self, channelId):
		url = const.GetChannelInfoUrl % str(channelId)
		timestamp = str(self.getTimeMillis())
		params = {"appId": const.AppID, "timestamp": timestamp}
		sign = self.generateSign(params, const.AppSecret)

		url = url + "?appId=%s&sign=%s&timestamp=%s" % (const.AppID, sign, timestamp)
		data = self.sender.request("GET", url)
		return data


	def deleteChannel(self, channelId):
		url = const.DeleteChannelUrl % str(channelId)
		timestamp = self.getTimeMillis()
		params = {"appId": const.AppID, "timestamp": timestamp, "userId": const.UserID}
		sign = self.generateSign(params, const.AppSecret)

		params["sign"] = sign
		data = self.sender.request("POST", url, fields = params)
		return data

	def changeChannelName(self, name, channelId):
		url = const.ChangeChannelNameUrl % channelId
		timestamp = self.getTimeMillis()
		params = {"appId": const.AppID, "timestamp": timestamp, "name": name}
		sign = self.generateSign(params, const.AppSecret)

		params["sign"] = sign
		data = self.sender.request("POST", url, fields = params)
		return data

	def changeChannelAuthor(self, channelId, author):
		url = const.ChangeChannelAuthorUrl % const.UserID

		timestamp = self.getTimeMillis()
		params = {"appId": const.AppID, "timestamp": timestamp, "publisher": author, "channelId": channelId}
		sign = self.generateSign(params, const.AppSecret)

		params["sign"] = sign
		data = self.sender.request("POST", url, fields = params)
		return data
