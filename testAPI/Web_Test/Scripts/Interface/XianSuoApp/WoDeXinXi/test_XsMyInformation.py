# -*- coding:UTF-8 -*-
'''
Created on 2015-11-24

@author: N-133
'''
from __future__ import unicode_literals
from COMMON import CommonUtil, Log, Time
from COMMON.CommonUtil import createRandomString
from CONFIG import Global
from CONFIG.Global import XianSuoDftMobile, XianSuoDftPassword
from CONFIG.InitDefaultPara import clueUserInit
from Interface.PingAnJianShe.Common.CommonIntf import getDbQueryResult
from Interface.PingAnJianShe.ShiJianChuLi.ShiJianChuLiIntf import exeDbQuery
from Interface.XianSuoApp.BaoLiao import XsBaoLiaoPara, XsBaoLiaoIntf
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoIntf import addXianSuo, viewSchedule
from Interface.XianSuoApp.BaoLiao.XsBaoLiaoPara import xinZeng2
from Interface.XianSuoApp.GongZuoTai import XsGongZuoTaiIntf
from Interface.XianSuoApp.WoDeXinXi import XsMyInformationIntf, \
    XsMyInformationPara
from Interface.XianSuoApp.WoDeXinXi.XsMyInformationIntf import updateUserInfo, \
    encodeToMd5, addUserPosition, systemUserCertified, delSystemUserCertified
from Interface.XianSuoApp.WoDeXinXi.XsMyInformationPara import updUserPara
from Interface.XianSuoApp.XinXiGuangChang.XsInformationSquareIntf import \
    addConcern, checkInConcernList, addPraise, checkInMyPraiseList, addComment, \
    checkInMyCommentList, checkInCommentList, getUserInfo, checkDictInUserInfoDict, \
    checkDictInClueList, getClueList, setClueShowState
from Interface.XianSuoApp.XinXiGuangChang.XsInformationSquarePara import \
    addPraisePara, praiseListPara, addCommentPara, listCommentPara, \
    informationSquareListPara
from Interface.XianSuoApp.xianSuoHttpCommon import xiansuo_login
from Interface.YunWeiPingTai.XiTongPeiZhi import XiTongPeiZhiIntf, \
    XiTongPeiZhiPara
from Interface.YunWeiPingTai.XinXiGuanLi import XinXiGuanLiIntf
from Interface.YunWeiPingTai.YunWeiCommon import YunWeiCommonIntf
from Interface.YunWeiPingTai.YunWeiCommon.YunWeiCommonIntf import \
    getDbQueryResultYunWei
import copy
import json
import unittest



class XsWoDeXinXi(unittest.TestCase):

    def setUp(self):
        XsGongZuoTaiIntf.initUser()
#         SystemMgrIntf.initEnv()''
        #清空自动化测试用户的点赞、关注
        if Global.simulationEnvironment is False:
            exeDbQuery(dbCommand ="delete from concerns c where c.concernuserid=(select id from users u where u.mobile='%s')"%XianSuoDftMobile,dbUser=Global.XianSuoYunWeiInfo['DbUser'],dbPass=Global.XianSuoYunWeiInfo['DbPass'])
            exeDbQuery(dbCommand ="delete from praises p where p.praiseuserid=(select id from users u where u.mobile='%s')"%XianSuoDftMobile,dbUser=Global.XianSuoYunWeiInfo['DbUser'],dbPass=Global.XianSuoYunWeiInfo['DbPass'])
        XinXiGuanLiIntf.deleteyunwei()
        pass
    def test_user_grade_02(self):
        '''用户等级测试-853'''
        #先删除后台所有的等级配置并将默认账号的爆料数置为0
        if Global.simulationEnvironment is False:
            YunWeiCommonIntf.exeDbQueryYunWei(dbCommand='delete from GRADES')
            YunWeiCommonIntf.exeDbQueryYunWei(dbCommand="update USERINFOS t set t.informationnum=0 where t.userid=(select r.id from USERS r where r.mobile='%s')" % Global.XianSuoDftMobile)
            #后台配置发布两条爆料后等级上升
            addGrade0ConfigDict = XiTongPeiZhiPara.addGradePara
            addGrade0ConfigDict['grade.gradeDemand'] = 1
            addGrade0ConfigDict['grade.gradeIntroduce'] = "0级爆料数1个"
            ret = XiTongPeiZhiIntf.add_grade(addGrade0ConfigDict)
            self.assertTrue(ret, '配置0级等级失败')
             
            addGrade1ConfigDict = XiTongPeiZhiPara.addGradePara
            addGrade1ConfigDict['grade.gradeDemand'] = 2
            addGrade1ConfigDict['grade.gradeIntroduce'] = "1级爆料数2个"        
            ret = XiTongPeiZhiIntf.add_grade(addGrade1ConfigDict)
            self.assertTrue(ret, '配置1级等级失败')
            #根据等级获取所需爆料数
            num=XiTongPeiZhiIntf.get_clue_demand_by_grade(grade=1)
            #前台发布3条爆料
            for count in range(num):
                #使用新手机爆料一条爆料
                newClueByNewUser = copy.deepcopy(XsBaoLiaoPara.XinZeng) 
                newClueByNewUser['information']['contentText'] = '事件描述%s' % CommonUtil.createRandomString()
                newClueByNewUser['information']['baiduX'] = '120.4989885463861'
                newClueByNewUser['information']['baiduY'] = '30.27759299562879'
                newClueByNewUser['information']['x'] = '120.488114380334'
                newClueByNewUser['information']['y'] = '30.27759299562879'         
                newClueByNewUser['information']['address'] = 'addres%s'%CommonUtil.createRandomString()
                responseDict = XsBaoLiaoIntf.addXianSuo(newClueByNewUser)
                self.assertTrue(responseDict.result, '新增线索失败')
                
            #手机端检查用户等级
            userId = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from USERS t where t.mobile='%s'" % Global.XianSuoDftMobile)
            checkUserDict = copy.deepcopy(XsMyInformationPara.checkUserInfoPara)
            checkUserDict['grade'] = 1
            ret = XsMyInformationIntf.check_personal_info(userId, checkUserDict)
            self.assertTrue(ret, '配置1级等级失败')
             
            #删除所有爆料
            XsBaoLiaoIntf.deleteAllClues()
             
            #再次检查等级是否降为0
            checkUserDict = copy.deepcopy(XsMyInformationPara.checkUserInfoPara)
            checkUserDict['grade'] = 0
            ret = XsMyInformationIntf.check_personal_info(userId, checkUserDict)
            self.assertTrue(ret, '删除爆料后，等级未降为0级')
        
            #检查等级介绍是否正确
            checkGradeIntroduceDict = copy.deepcopy(XsMyInformationPara.checkGradeConfigPara)
            checkGradeIntroduceDict['grade'] = 1
            checkGradeIntroduceDict['gradeIntroduce'] = addGrade1ConfigDict['grade.gradeIntroduce']
            ret =XsMyInformationIntf.check_user_grade_config(checkGradeIntroduceDict)
            self.assertTrue(ret, '检查等级介绍失败')
        
            #等级介绍更新
            grade1Id = YunWeiCommonIntf.getDbQueryResultYunWei(dbCommand = "select t.id from GRADES t where t.gradeintroduce='%s'" % addGrade1ConfigDict['grade.gradeIntroduce'])
            updateGradeDict = copy.deepcopy(XiTongPeiZhiPara.updGradePara)
            updateGradeDict['grade.id'] = grade1Id
            updateGradeDict['grade.gradeIntroduce'] = "1级介绍更新"
            ret = XiTongPeiZhiIntf.upd_grade(updateGradeDict)
        
            #重新检查等级介绍
            checkGradeIntroduceDict = copy.deepcopy(XsMyInformationPara.checkGradeConfigPara)
            checkGradeIntroduceDict['grade'] = 1
            checkGradeIntroduceDict['gradeIntroduce'] = updateGradeDict['grade.gradeIntroduce']
            ret =XsMyInformationIntf.check_user_grade_config(checkGradeIntroduceDict)
            self.assertTrue(ret, '检查等级介绍失败')
        else:
            Log.LogOutput( message='仿真环境，跳过测试')
        pass
    #当前用户个人信息
    def test_XsMyInformation_01(self):
        '''查看当前用户个人信息'''
        #新增三条线索
        addPara=copy.deepcopy(xinZeng2)
        addXianSuo(addPara)
        addXianSuo(addPara)
        addXianSuo(addPara)
        listPara={
                'tqmobile':'true',
                'page':'1',
                'rows':'100'
                  }
        lsr=viewSchedule(para=listPara)
        #查看进度列表结果字典项
        lsrDict=json.loads(lsr.text)
        #新增关注
        addConPara={
                'tqmobile':'true',
                'informationId':'',#lsrDict['module']['rows'][0]['information']['id'],
                'concernUserId':lsrDict['response']['module']['rows'][0]['information']['publishUserId'],
                'concernDate':Time.getCurrentDate()
                    }
        #新增三条关注
        i=0
        for item in lsrDict['response']['module']['rows']:
            if i==3:
                break
            addConPara['informationId']=item['information']['id']
            result0=addConcern(para=addConPara)
            self.assertTrue(result0.result, '新增关注失败')
            i=i+1
        #验证我的关注
        listConPara={
                'tqmobile':'true',
                'sidx':"id",
                'sord':"desc",
                'page':1,
                'rows':200
                     }
        checkConPara={
                      'id':'',#lsrDict['module']['rows'][0]['information']['id'],
                      'concernNum':1
                      }
        #只检查三条
        i=0
        for item in lsrDict['response']['module']['rows']:
            if i==3:
                break
            checkConPara['id']=item['information']['id']
            result1=checkInConcernList(checkPara=checkConPara,listPara=listConPara)
            self.assertTrue(result1, '关注列表验证失败')
            i=i+1
        #对三条线索进行点赞
        addpara=copy.deepcopy(addPraisePara)
        addpara['praiseUserId']=lsrDict['response']['module']['rows'][0]['information']['publishUserId']
        for item in lsrDict['response']['module']['rows']:
            addpara['informationId']=item['information']['id']
            addPraise(para=addpara)
        #验证点赞是否在我的点赞列表中显示
        checkPara2={
                   'nickName':lsrDict['response']['module']['rows'][0]['information']['nickName'],
                    'id':'',
                   'praiseNum':1
                   }
        listPara2=copy.deepcopy(praiseListPara)
        listPara2['userId']=lsrDict['response']['module']['rows'][0]['information']['publishUserId']
        #只检测三条
        i=0
        for item in lsrDict['response']['module']['rows']:
            if i==3:
                break
            checkPara2['id']=item['information']['id']
            result=checkInMyPraiseList(checkPara=checkPara2,listPara=listPara2)
            self.assertTrue(result, '我的点赞列表验证失败')
            i=i+1
        Log.LogOutput(message='我的点赞列表验证成功')
        #评论其中一条线索
        addcompara=copy.deepcopy(addCommentPara)
        addcompara['informationId']=lsrDict['response']['module']['rows'][0]['information']['id']
        addcompara['commentUserId']=lsrDict['response']['module']['rows'][0]['information']['publishUserId']
        addcompara['commentType']=0
        result3=addComment(para=addcompara)
        self.assertTrue(result3.text, '新增评论失败')
        checkComPara={
                      'contentText':addcompara['contentText'],
                      'informationId':addcompara['informationId'],
                      'commentUserId':addcompara['commentUserId'],
                      'commentType':addcompara['commentType']
                      }
        listComPara=copy.deepcopy(listCommentPara)
        result4=checkInMyCommentList(checkPara=checkComPara,listPara=listComPara)
        self.assertTrue(result4, '我的评论列表验证失败')
        #修改密码
        userPara={
                  'tqmobile':'true',
                  'id':lsrDict['response']['module']['rows'][0]['information']['publishUserId']
                  }
        userRes=getUserInfo(para=userPara)
        userDict=json.loads(userRes.text)
        updPwPara=copy.deepcopy(updUserPara)
        updPwPara['id']=userDict['response']['module']['id']
        password='222222'
        updPwPara['password']=encodeToMd5(password)
        updateUserInfo(userUpdatePara=updPwPara)
        try:
            res1=xiansuo_login(mobile=XianSuoDftMobile, password=XianSuoDftPassword)
            self.assertFalse(res1, '修改密码失败')
            res2=xiansuo_login(mobile=XianSuoDftMobile, password=password)
            self.assertTrue(res2, '修改密码失败')
        finally:
            #将密码改回默认值
            updPwPara['password']=encodeToMd5(XianSuoDftPassword)
            updateUserInfo(userUpdatePara=updPwPara,password=password)
            Log.LogOutput(message='密码恢复原始状态')
        #定位签到
        #首先在社管-系统管理中进行线索用户认证
        ucpara={
                'clueMobile':XianSuoDftMobile,
                'userName':clueUserInit['DftJieDaoUser'],
                'userId':getDbQueryResult(dbCommand = "select id from users  where username='%s'"%clueUserInit['DftJieDaoUser'])
                }
        systemUserCertified(para=ucpara)
        
        positionPara={
                'tqmobile':'true',
                'userId':userDict['response']['module']['id'],
                'mobile':XianSuoDftMobile,
                'address':'定位签到地址',
                'baiduX':'120.4989885463861',
                'baiduY':'30.27759299562879',
                'x':'120.488114380334',
                'y':'30.27759299562879',
                'pcUserId':ucpara['userId']
                      }
        res=addUserPosition(para=positionPara)
        self.assertTrue(res.result, '定位签到失败')
        Log.LogOutput(message='取消认证')
        para={
              'clueMobile':XianSuoDftMobile,
              'userId':getDbQueryResultYunWei(dbCommand="select pcuserid from users where mobile='%s'"%XianSuoDftMobile)
              }
        #首先通过手机号查找线索users表的pcuserid,然后去社管user的id中查找出账号，再取消认证
        res=delSystemUserCertified(para=para)
        self.assertTrue(res.result, '取消认证成功')
        pass
    
    def test_XsMyInformation_03(self):
        '''个人资料信息修改'''
        addPara=copy.deepcopy(xinZeng2)
        r=addXianSuo(addPara)
        self.assertTrue(r.result,'新增失败')
        listPara={
                'tqmobile':'true',
                'page':'1',
                'rows':'100'
                  }
        lsr=viewSchedule(para=listPara)
        #查看进度列表结果字典项
        lsrDict=json.loads(lsr.text)
        userPara={
                  'tqmobile':'true',
                  'id':lsrDict['response']['module']['rows'][0]['information']['publishUserId']
                  }
        userRes=getUserInfo(para=userPara)
        userDict=json.loads(userRes.text)
        updPwPara=copy.deepcopy(updUserPara)
        updPwPara['id']=userDict['response']['module']['id']
        updPwPara['nickName']='user001'+createRandomString()
        updPwPara['gender']='男'
        updPwPara['address']='测试地址'+createRandomString()
        res=updateUserInfo(userUpdatePara=updPwPara)
        self.assertTrue(res.result, '修改个人信息失败')
        #验证修改结果;
        checkPara={
            'nickName': updPwPara['nickName'],
            'address':updPwPara['address'],  
            'gender':updPwPara['gender']
                   }
        result1=checkDictInUserInfoDict(checkPara=checkPara,userpara=userPara)
        self.assertTrue(result1, '修改个人信息验证失败')
        #后台将该线索公开
        showStatePara={
                       'ids':lsrDict['response']['module']['rows'][0]['information']['id'],
                       'showState':1
                       }
        r=setClueShowState(para=showStatePara)
        self.assertTrue(r.result, '设置线索分享状态失败！')
        
        #验证昵称在我的进度中是否修改成功
        Log.LogOutput(message='验证昵称在我的进度中是否修改成功')
        checkNickNamePara={'nickName':updPwPara['nickName']}
        listPara2=copy.deepcopy(informationSquareListPara)
        listPara2['userId']=userDict['response']['module']['id']
        #获取信息广场列表
        response=getClueList(para=listPara2)
        responseDict=json.loads(response.text)
        
        result2=checkDictInClueList(checkPara=checkNickNamePara,listPara=listPara2)
        self.assertTrue(result2, '我的进度中昵称修改验证失败')
        #验证昵称在我的关注中是否修改成功
        #新增关注
        addConPara={
                'tqmobile':'true',
                'informationId':responseDict['response']['module']['rows'][0]['information']['id'],
                'concernUserId':userDict['response']['module']['id'],
                'concernDate':Time.getCurrentDate()
                    }
        result=addConcern(para=addConPara)
        self.assertTrue(result.result, '新增关注失败')
        Log.LogOutput(message='验证昵称在我的关注中是否修改成功')
        listPara3={
                'tqmobile':'true',
                'sidx':"id",
                'sord':"desc",
                'page':1,
                'rows':200                   
                   }
        result3=checkInConcernList(checkPara=checkNickNamePara,listPara=listPara3)
        self.assertTrue(result3, '关注列表昵称验证失败')
        #验证昵称在我的点赞中是否修改成功
        Log.LogOutput(message='验证昵称在我的点赞中是否修改成功')
        #新增点赞
        addpara=copy.deepcopy(addPraisePara)
        addpara['informationId']=responseDict['response']['module']['rows'][0]['information']['id']
        addpara['praiseUserId']=userDict['response']['module']['id']
        addPraise(para=addpara)
        listPara4=copy.deepcopy(praiseListPara)
        listPara4['userId']=userDict['response']['module']['id']
        result4=checkInMyPraiseList(checkPara=checkNickNamePara,listPara=listPara4)
        self.assertTrue(result4, '我的点赞列表验证失败')
        Log.LogOutput(message='昵称在我的点赞中修改成功')        
        #验证昵称在我的评论中是否修改成功
        Log.LogOutput(message='验证昵称在我的评论中是否修改成功')
        #新增评论
        addcompara=copy.deepcopy(addCommentPara)
        addcompara['informationId']=responseDict['response']['module']['rows'][0]['information']['id']
        addcompara['commentUserId']=userDict['response']['module']['id']
        addcompara['commentType']=0
        result=addComment(para=addcompara)
        self.assertTrue(result.text, '新增评论失败')
        Log.LogOutput(message='验证昵称在评论列表中是否修改成功')
        listPara5=copy.deepcopy(listCommentPara)
        checkPara5={
                    'commentNickName':updPwPara['nickName']
                    }
        result5=checkInMyCommentList(checkPara=checkPara5,listPara=listPara5)
        self.assertTrue(result5, '我的评论列表验证失败')
        listPara5['informationId']=addcompara['informationId']
        result52=checkInCommentList(checkPara=checkPara5,listPara=listPara5)
        self.assertTrue(result52, '评论列表验证失败')   
        pass
    
    def tearDown(self):
        pass    
    
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
#     suite.addTest(XsWoDeXinXi("test_XsMyInformation_01"))
    suite.addTest(XsWoDeXinXi("test_user_grade_02"))
#     suite.addTest(XsWoDeXinXi("test_XsMyInformation_03"))
    results = unittest.TextTestRunner().run(suite)
    pass    