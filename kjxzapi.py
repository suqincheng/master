# 导包
import requests
null = 'null'
l_url = 'http://120.48.0.142:9060/server/user/userLogin'
l_body = {
	"userId": "000531",
	"password": "a2p4ek5qY3RAa2p4ejEyMzQ="
}
res_login = requests.post(url=l_url, json=l_body)
# print(res_login.json())
# print(type(res_login.text))
# print(res_login.status_code)
# print(eval(res_login.text)['code'])
dict_res = eval(res_login.text)
# print(eval(res_login.text)['data']['kjxzToken'])
token_res = dict_res['data']['kjxzToken']
print(token_res)

# # 创建需求
# addDemand_url = 'http://120.48.0.142:9060/server/demandsub/addDemandsub'
# addDemand_body = {
# 	"summary": "test_996",
# 	"businessDirector": "000531",
# 	"priority": "P3",
# 	"wishDate": "2021-11-30",
# 	"subdivisionType": "1561086029373RAXSX",
# 	"importantDemand": "0",
# 	"groupId": "1",
# 	"isService": "0",
# 	"description": "<h3><strong><span style=\"font-size:16px\"><span style=\"line-height:1.2\">一、需求背景</span></span></strong></h3><p><em><span style=\"letter-spacing:2px\"><span style=\"font-size:12px\"><span style=\"line-height:1.2\">【填写需求背景:需求背景有助于各方了解需求的真实意图,可以填写例如:用户反馈截图,业务分析数据等】</span></span></span></em></p><h3><strong><span style=\"font-size:16px\"><span style=\"line-height:1.2\">二、需求内容</span></span></strong></h3><p><em><span style=\"letter-spacing:2px\"><span style=\"font-size:12px\"><span style=\"line-height:1.2\">【填写需求背描述:例如需求逻辑描述,流程图,线框图,页面实例等。需要描述清楚需求内容，经ＢＡ分析后可供开发评估可行性及大致开发难度及时间.需求的讨论逐渐补充完整】</span></span></span></em></p><h3><strong><span style=\"font-size:16px\"><span style=\"line-height:1.2\">三、技术实现</span></span></strong></h3><p><em><span style=\"letter-spacing:2px\"><span style=\"font-size:12px\"><span style=\"line-height:1.2\">【技术实现:技术实现方案包括内部和外部的依赖接口,由开发补充】</span></span></span></em></p><h3><strong><span style=\"font-size:16px\"><span style=\"line-height:1.2\">四、需求评审</span></span></strong></h3><p><span style=\"letter-spacing:2px\"><em><span style=\"font-size:12px\"><span style=\"line-height:1.2\">【补充是否需要评审,如果需要评审,这里需要补充评审会议纪要的链接】</span></span></em></span></p>",
# 	"gmId": "000533",
# 	"gmName": "任测试",
# 	"gmDeptId": "0212",
# 	"imageList": [],
# 	"fileList": [],
# 	"deptName": "信息技术部",
# 	"demandTypeName": "标准需求",
# 	"deptId": "0212",
# 	"demandId": "",
# 	"cacheType": "0",
# 	"userId": "014118",
# 	"userName": "测试699254",
# 	"demandTypeId": "4",
# 	"templateId": "101"
# }
# addDemand_res = requests.post(url=addDemand_url, json=addDemand_body)
# print(addDemand_res.text)
# 讨论中
# '''R2204180147'''
# tl_url = 'http://120.48.0.142:9060/server/discussNeed/updateDemandsubStatus'
# tl_body = {
# 	"boardId": "1",
# 	"demandId": "R2204180161",
# 	"userId": "000531",
# 	"userName": "测试504517"
# }
# token_headers = {"Token":'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NDg1MzQ5MzcsImV4cCI6MTY1MTEyNjkzNywidXNlcklkIjoiMDAwNTMxIiwiaXNzIjoia2p4eiJ9.JQrth7EFI4BpSUrg_VnVIeIHEq_4nQdON0VkN_8riVY'}
# tl_res = requests.post(url=tl_url, json=tl_body, headers=token_headers)
# print(tl_res.text)
# #待拆分
# dcf_url = 'http://120.48.0.142:9060/server/discussNeed/updateDemandsubStatus'
# dcf_body= {
# 	"boardId": "3",
# 	"demandId": "R2204180161",
# 	"userId": "000531",
# 	"userName": "测试504517"
# }
# token_headers = {"Token":'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NDg1MzQ5MzcsImV4cCI6MTY1MTEyNjkzNywidXNlcklkIjoiMDAwNTMxIiwiaXNzIjoia2p4eiJ9.JQrth7EFI4BpSUrg_VnVIeIHEq_4nQdON0VkN_8riVY'}
# dcf_res= requests.post(url=dcf_url, json=dcf_body, headers=token_headers)
# print(dcf_res.text)
# 新建story
story_url = 'http://120.48.0.142:9060/server/demandsub/addDemandsubJira'
story_body = {
	"summary": "test_996",
	"productId": null,
	"bindVersionId": null,
	"moduleId": [],
	"deptName": "信息技术部",
	"tId": "13887408591786H7NJ",
	"projectId": "1558332722467QOIDU",
	"systemId": "1428915206773G2OFG",
	"bchildTypeCode": "1000021",
	"priority": "P3",
	"itDuedate": "2022-01-31",
	"developDate": "1",
	"testDate": "0.3",
	"fieldName_816": null,
	"systemModuleId": "2",
	"tName": "移动平台组",
	"description": "<p>1</p>",
	"imageList": [],
	"fileList": [],
	"deptId": "0212",
	"systemModuleName": "行情",
	"itpmProjectId": "1558332722467QOIDU",
	"projectName": "移动平台组虚拟项目",
	"systemName": "君弘",
	"userId": "000531",
	"userName": "测试504517",
	"sonUserId": "000531",
	"sonUserName": "测试504517",
	"oaCode": "qiujing",
	"demandId": "R2204180147",
	"templateId": "101",
	"isSplit": "0"
}
token_headers = {"Token":'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NDg1MzQ5MzcsImV4cCI6MTY1MTEyNjkzNywidXNlcklkIjoiMDAwNTMxIiwiaXNzIjoia2p4eiJ9.JQrth7EFI4BpSUrg_VnVIeIHEq_4nQdON0VkN_8riVY'}
story_res = requests.post(url=story_url, json=story_body, headers=token_headers)
dict_story_res = eval(story_res.text)
story_id = dict_story_res['data']
print(story_res.text)
print(story_id)