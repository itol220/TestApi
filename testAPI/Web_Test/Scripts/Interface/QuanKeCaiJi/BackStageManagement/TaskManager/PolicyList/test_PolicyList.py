# -*- coding:UTF-8 -*-
'''
Created on 2018年4月8日 17:35:20

@author: 孙留平
'''
import copy
import unittest

from Interface.QuanKeCaiJi.HouTaiGuanLi21200.TaskManager.PolicyList import PolicyPara, \
    PolicyListIntf


class PolicyList( unittest.TestCase ):

    def setUp( self ):
        ret = PolicyListIntf.clear_policy_list( "true" ) 
        self.assertTrue( ret, "清空策略列表失败" )
        pass
    
    '''
    @功能：添加策略
    @孙留平  2018年4月8日 17:35:38
    ''' 
    def testPolicy_01AddNormal( self ):
        '''策略管理-新增策略-正常新增'''
        
        toAddNormalPolicy = copy.deepcopy( PolicyPara.addPolicyDict )
        toAddNormalPolicy['cname'] = '自动化测试策略'
        toAddNormalPolicy['ename'] = 'autotestPolicy'
        toAddNormalPolicy['code'] = 'String ss = new String ();'
        toAddNormalPolicy['description'] = "test desc"
        
        result = PolicyListIntf.add_policy( toAddNormalPolicy )
        
        self.assertTrue( result, "添加策略失败" )
        pass
    
    '''
    @功能：单个删除策略
    @孙留平  2018年4月8日 17:35:38
    ''' 
    def testPolicy_02DeleteSingle( self ):
        '''策略管理-删除策略-单条删除'''
        
        # 添加策略
        ename = 'autotestPolicyToDelete'
        toAddNormalPolicy = copy.deepcopy( PolicyPara.addPolicyDict )
        toAddNormalPolicy['cname'] = '自动化测试策略'
        toAddNormalPolicy['ename'] = ename
        toAddNormalPolicy['code'] = 'String ss = new String ();'
        toAddNormalPolicy['description'] = "test desc"
        
        resultAdd = PolicyListIntf.add_policy( toAddNormalPolicy )
        
        self.assertTrue( resultAdd, "=====添加策略失败=====" )
        
        # 添加完成之后检查
        toCheckPolicyDict = copy.deepcopy( PolicyPara.toCheckPolicyInfoDict )
        toCheckPolicyDict['ename'] = toAddNormalPolicy['ename']
        toCheckPolicyDict['description'] = None
        
        resultCheck = PolicyListIntf.check_policy_in_list( toCheckPolicyDict )
        
        self.assertTrue( resultCheck, "=====添加策略之后在列表中没有检查到=====" )
        
        resultDelete = PolicyListIntf.delete_policy_single_by_name( ename )
        
        # 检查完之后删除
        self.assertTrue( resultDelete , "=====删除策略【%s】失败=====" % ename )
        
        
        resultCheck = PolicyListIntf.check_policy_in_list( toCheckPolicyDict )
        # 删除之后检查
        self.assertFalse( resultCheck, "=====删除策略【%s】之后，列表中仍然存在=====" % ename )
        pass
        
    '''
    @功能：批量删除策略
    @孙留平  2018年4月8日 17:35:38
    ''' 
    def testPolicy_03DeleteBatch( self ):
        '''策略管理-删除策略-批量删除'''
        # 添加策略
        ename1 = 'autotestPolicyToDelete1'
        toAddNormalPolicy1 = copy.deepcopy( PolicyPara.addPolicyDict )
        toAddNormalPolicy1['cname'] = '自动化测试策略1'
        toAddNormalPolicy1['ename'] = ename1
        toAddNormalPolicy1['code'] = 'String ss = new String ();'
        toAddNormalPolicy1['description'] = "test desc1"
        
        # 添加策略
        ename2 = 'autotestPolicyToDelete2'
        toAddNormalPolicy2 = copy.deepcopy( PolicyPara.addPolicyDict )
        toAddNormalPolicy2['cname'] = '自动化测试策略2'
        toAddNormalPolicy2['ename'] = ename2
        toAddNormalPolicy2['code'] = 'String ss = new String ();'
        toAddNormalPolicy2['description'] = "test desc2"
        
        resultAdd1 = PolicyListIntf.add_policy( toAddNormalPolicy1 )
        resultAdd2 = PolicyListIntf.add_policy( toAddNormalPolicy2 )
        self.assertTrue( resultAdd1, "=====添加策略1失败=====" )
        self.assertTrue( resultAdd2, "=====添加策略2失败=====" )
        
        # 添加完成之后检查
        toCheckPolicyDict1 = copy.deepcopy( PolicyPara.toCheckPolicyInfoDict )
        toCheckPolicyDict1['ename'] = toAddNormalPolicy1['ename']
        toCheckPolicyDict1['description'] = None
        
        toCheckPolicyDict2 = copy.deepcopy( PolicyPara.toCheckPolicyInfoDict )
        toCheckPolicyDict2['ename'] = toAddNormalPolicy2['ename']
        toCheckPolicyDict2['description'] = None
        
        
        resultCheck1 = PolicyListIntf.check_policy_in_list( toCheckPolicyDict1 )
        resultCheck2 = PolicyListIntf.check_policy_in_list( toCheckPolicyDict2 )
        self.assertTrue( resultCheck1 and resultCheck2, "=====添加策略之后在列表中没有检查到=====" )
        
        toDeleteNames = [ename1, ename2]
        resultDelete = PolicyListIntf.delete_policy_batch_by_name( toDeleteNames )
        # 检查完之后删除
        self.assertTrue( resultDelete , "=====删除策略【%s】失败=====" % toDeleteNames )
        
        resultCheck1 = PolicyListIntf.check_policy_in_list( toCheckPolicyDict1 )
        resultCheck2 = PolicyListIntf.check_policy_in_list( toCheckPolicyDict2 )
        # 删除之后检查
        self.assertFalse( resultCheck1 and resultCheck2, "=====删除策略【%s】之后，列表中仍然存在=====" % toDeleteNames )
        pass
    
    '''
    @功能：搜索策略
    @孙留平  2018年4月12日 12:20:55
    ''' 
    def testPolicy_04SearchPolicy( self ):
        '''策略管理-搜索策略'''
        
        # 添加策略
        ename_04SearchPolicy_1 = 'autotestPolicyToDeleteFourOne'
        toAddNormalPolicy_04_1 = copy.deepcopy( PolicyPara.addPolicyDict )
        toAddNormalPolicy_04_1['cname'] = '自动化测试策略0401'
        toAddNormalPolicy_04_1['ename'] = ename_04SearchPolicy_1
        toAddNormalPolicy_04_1['code'] = 'String ss = new String ();'
        toAddNormalPolicy_04_1['description'] = "test desc04_1"
        
        # 添加策略
        ename_04SearchPolicy_2 = 'autotestPolicyToDeleteFourTwo'
        toAddNormalPolicy_04_2 = copy.deepcopy( PolicyPara.addPolicyDict )
        toAddNormalPolicy_04_2['cname'] = '自动化测试策略0402'
        toAddNormalPolicy_04_2['ename'] = ename_04SearchPolicy_2
        toAddNormalPolicy_04_2['code'] = 'String ss = new String ();'
        toAddNormalPolicy_04_2['description'] = "test desc 0402"
        
        resultAdd0401 = PolicyListIntf.add_policy( toAddNormalPolicy_04_1 )
        resultAdd0402 = PolicyListIntf.add_policy( toAddNormalPolicy_04_2 )
        self.assertTrue( resultAdd0401, "=====添加策略1失败=====" )
        self.assertTrue( resultAdd0402, "=====添加策略2失败=====" )
        
        # 添加完成之后检查
        toCheckPolicyDict0401 = copy.deepcopy( PolicyPara.toCheckPolicyInfoDict )
        toCheckPolicyDict0401['ename'] = toAddNormalPolicy_04_1['ename']
        toCheckPolicyDict0401['description'] = None
        
        toCheckPolicyDict0402 = copy.deepcopy( PolicyPara.toCheckPolicyInfoDict )
        toCheckPolicyDict0402['ename'] = toAddNormalPolicy_04_2['ename']
        toCheckPolicyDict0402['description'] = None
        
        # 检查成功，证明新增成功了
        resultCheck1 = PolicyListIntf.check_policy_in_list( toCheckPolicyDict0401 )
        resultCheck2 = PolicyListIntf.check_policy_in_list( toCheckPolicyDict0402 )
        self.assertTrue( resultCheck1 and resultCheck2, "=====添加策略之后在列表中没有检查到=====" )
        
        # 执行搜索条件 ename_04SearchPolicy_1,应当搜索出来policy1 不应该搜索出来2
        existListDict = PolicyListIntf.search_policy_by_ename( ename_04SearchPolicy_1 )
        
        # 应该是true
        resultCheckExistsPolicy1 = PolicyListIntf.check_policy_in_list( toCheckPolicyDict0401, existListDict )
        # 应该是false
        resultCheckExistsPolicy2 = PolicyListIntf.check_policy_in_list( toCheckPolicyDict0402, existListDict )
        
        self.assertTrue( resultCheckExistsPolicy1, "用policy1的ename执行搜索，没有搜索到policy1" )
        
        self.assertFalse( resultCheckExistsPolicy2, "用policy1的ename执行搜索，搜索到policy2了！" )
        pass
    
    '''
    @功能：刷新策略列表
    @孙留平  2018年4月12日 13:52:33
    ''' 
    def testPolicy_05RefreshPolicyList( self ):
        '''策略管理-刷新策略'''
        # 添加策略
        ename_05RefreshPolicy_1 = 'autotestPolicyToRefresh'
        toAddNormalPolicy_05_1 = copy.deepcopy( PolicyPara.addPolicyDict )
        toAddNormalPolicy_05_1['cname'] = '自动化测试策略0501'
        toAddNormalPolicy_05_1['ename'] = ename_05RefreshPolicy_1
        toAddNormalPolicy_05_1['code'] = 'String ss = new String ();'
        toAddNormalPolicy_05_1['description'] = "test desc05_1"
        
        resultAdd0501 = PolicyListIntf.add_policy( toAddNormalPolicy_05_1 )
        self.assertTrue( resultAdd0501, "=====添加策略1失败=====" )
        
        # 添加完成之后检查
        toCheckPolicyDict0501 = copy.deepcopy( PolicyPara.toCheckPolicyInfoDict )
        toCheckPolicyDict0501['ename'] = toAddNormalPolicy_05_1['ename']
        toCheckPolicyDict0501['description'] = None
        # 检查成功，证明新增成功了
        resultCheck1 = PolicyListIntf.check_policy_in_list( toCheckPolicyDict0501 )
        self.assertTrue( resultCheck1, "=====添加策略之后在列表中没有检查到=====" )
        
        result = PolicyListIntf.refresh_policy_list()
        resultRefreshCheck = PolicyListIntf.check_policy_in_list( toCheckPolicyDict0501, result )
        
        self.assertTrue( resultRefreshCheck, "新增的策略在刷新之后，没有在列表中找到" )
        pass
    '''
    @功能：修改策略
    @孙留平  2018年4月12日 14:00:08
    ''' 
    def testPolicy_06UpdatePolicy( self ):
        '''策略管理-刷新策略'''
        # 添加策略
        ename_06UpdatePolicy_1 = 'autotestPolicyToUpdate'
        ename_06UpdatePolicy_1_new = "%sNew" % ename_06UpdatePolicy_1
        
        toAddNormalPolicy_06_1 = copy.deepcopy( PolicyPara.addPolicyDict )
        toAddNormalPolicy_06_1['cname'] = '自动化测试策略0601'
        toAddNormalPolicy_06_1['ename'] = ename_06UpdatePolicy_1
        toAddNormalPolicy_06_1['code'] = 'String ss = new String ();'
        toAddNormalPolicy_06_1['description'] = "test desc06_1"
        
        resultAdd0501 = PolicyListIntf.add_policy( toAddNormalPolicy_06_1 )
        self.assertTrue( resultAdd0501, "=====添加策略1失败=====" )
        
        # 添加完成之后检查
        toCheckPolicyDict0601 = copy.deepcopy( PolicyPara.toCheckPolicyInfoDict )
        toCheckPolicyDict0601['ename'] = toAddNormalPolicy_06_1['ename']
        toCheckPolicyDict0601['description'] = None
        
        # 检查成功，证明新增成功了
        resultCheck1 = PolicyListIntf.check_policy_in_list( toCheckPolicyDict0601 )
        self.assertTrue( resultCheck1, "=====添加策略之后在列表中没有检查到=====" )
        
        # 修改一下策略
        updatePolicyListDict = copy.deepcopy( toAddNormalPolicy_06_1 )
        updatePolicyListDict['oldEname'] = ename_06UpdatePolicy_1
        updatePolicyListDict['ename'] = ename_06UpdatePolicy_1_new
        
        resultUpdate = PolicyListIntf.update_policy( updatePolicyListDict )
        
        self.assertTrue( resultUpdate, "修改策略失败" )
        
        toCheckPolicyDict0601_afterUpdate = copy.deepcopy( PolicyPara.toCheckPolicyInfoDict )
        toCheckPolicyDict0601_afterUpdate['ename'] = ename_06UpdatePolicy_1_new
        toCheckPolicyDict0601_afterUpdate['description'] = None
        
        # 修改之后检查，新策略存在，旧策略不存在
        # 修改后的，存在
        resultCheckUpdate = PolicyListIntf.check_policy_in_list( toCheckPolicyDict0601_afterUpdate )
        # 修改前的，。不存在
        resultCheckOld = PolicyListIntf.check_policy_in_list( toCheckPolicyDict0601 )
        self.assertTrue( resultCheckUpdate, "策略修改之后，没有查询到新的策略信息" )
        self.assertFalse( resultCheckOld, "策略修改之后，旧的策略信息查询到了" )
        pass
        
    '''
    @see:结尾清空策略列表
    @since: 2018年4月9日 09:24:54
    '''
    def tearDown( self ):
        ret = PolicyListIntf.clear_policy_list( "true" ) 
        self.assertTrue( ret, "清空策略列表失败" )
        pass
        
if __name__ == "__main__":
    unittest.main()
    pass
    
