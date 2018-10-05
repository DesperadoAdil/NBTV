import sys
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.http import method_type as MT
from aliyunsdkcore.http import format_type as FT
from textMessage import const

VERIFICATION = 1
SIGNNAME = "激流山庄"

class TextMessage:
	def __init__(self):

		# 注意：不要更改
		REGION = "cn-hangzhou"
		PRODUCT_NAME = "Dysmsapi"
		DOMAIN = "dysmsapi.aliyuncs.com"
		
		self.acs_client = AcsClient(const.AccessKeyID, const.AccessKeySecret, REGION)
		region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)


	def sendSMS(self, businessID, phoneNumber, templatePara = None, signName = SIGNNAME, messageType = VERIFICATION):
		'''
			templatePara: dict

			used to send text message to phoneNumber
			if messageType == VERIFICATION, templatePara must contain key 'code'
		'''
		smsRequest = SendSmsRequest.SendSmsRequest()
		# 申请的短信模板编码,必填
		if (messageType == VERIFICATION):
			smsRequest.set_TemplateCode(const.Verification)

		# 短信模板变量参数
		if templatePara is not None:
			smsRequest.set_TemplateParam(templatePara)
		else:
			raise ValueError("you must give a paramter to send message")

		# 设置业务请求流水号，必填。
		smsRequest.set_OutId(businessID)

		# 短信签名
		smsRequest.set_SignName(signName)
		
		# 数据提交方式
		# smsRequest.set_method(MT.POST)
		
		# 数据提交格式
		# smsRequest.set_accept_format(FT.JSON)
		
		# 短信发送的号码列表，必填。
		smsRequest.set_PhoneNumbers(phoneNumber)

		# 调用短信发送接口，返回json
		smsResponse = self.acs_client.do_action_with_exception(smsRequest)

		# TODO 业务处理

		return smsResponse

