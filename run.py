#@project:  ayla_ui_project
#@author: heyeping
#@file: run.py.py
#@ide: PyCharm
#@time: 2021/5/25 11:26 AM

import pytest,os

if __name__ == "__main__":
    base_url = os.getcwd()
    #print(base_url)
    runTestFile = os.path.join(base_url, 'Projects/AndroidConstructionAPP', 'Cases/Test_Smoke.py::TestSmoke::test_05_changeDeviceName')
    #print(runTestFile)
    reportFile = os.path.join(base_url, 'Report')
    pytest.main(["-vs", runTestFile, f'--alluredir={reportFile}/data'])
    # 本地生成报告
    os.system(f'allure generate {reportFile}/data -o {reportFile}/html --clean')