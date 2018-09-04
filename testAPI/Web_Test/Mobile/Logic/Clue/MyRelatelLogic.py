# -*- coding:UTF-8 -*-
'''
Created on 2016-10-18

@author: N-66
'''
from Mobile.UI.Clue import PersonalUI, AboutUsUI

'''
    @功能：在关于我们检查版本信息及免责声明内容
    @para: 
    @return: 检查版本信息及免责声明内容成功，返回True；否则返回False
    @ hongzenghui  2016-9-20
'''

def check_version_and_mianzheshengming():
    if PersonalUI.click_about_us() is False:
        return False
    if AboutUsUI.check_linkage_version() is False:
        return False
    if AboutUsUI.click_mianzheshengming() is False:
        return False
    if AboutUsUI.check_mianzheshengming() is False:
        return False
    return True
        
         
    
    