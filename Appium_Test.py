from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
desired_cap = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "appPackage": "org.mkcl.eralive",
    "appActivity": ".SplashScreenActivity caller=com.miui.home",
    "noReset": 'true'
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(10)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[1]/android.widget.EditText")
el1.send_keys("pratiksha06506")
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.widget.EditText")
el2.send_keys("pratiksha")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[4]/android.view.View[3]/android.widget.Button")
el3.click()
driver.implicitly_wait(30)
print('ok1-id password enterd')
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[3]/android.view.View[3]/android.widget.Button")
el4.click()
print('ok2- continue to the course')
el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.Button")
el5.click()
print('ok3-content viewer')
el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.view.View")
el6.click()
print('ok4-opening session 1')
el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.ListView/android.view.View/android.widget.ListView/android.view.View[1]/android.view.View[2]")
el7.click()
print('ok5-opening session 1- parichay')
el8 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[1]/android.widget.Button")
el8.click()
el9 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
el9.click()
el10 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
el10.click()
el11 = driver.find_element_by_xpath("//android.view.View[@content-desc=\"learnerhome\"]/android.view.View/android.view.View")
el11.click()
print('ok6- Homepage')
TouchAction(driver).tap(x=649, y=146).perform()
TouchAction(driver).tap(x=637, y=293).perform()
el12 = driver.find_element_by_xpath("//android.view.View[@content-desc=\"Log Out\"]/android.widget.TextView")
el12.click()
print('ok7-Logout')
el13 = driver.find_element_by_xpath("//android.view.View[@content-desc=\"BACK TO LOGIN\"]/android.widget.TextView")
el13.click()
print('ok8-Back to login Page')

print('Appium test is passed')

'''
driver.implicitly_wait(5)
TouchAction(driver).tap(x=56, y=215).perform()
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.widget.ListView/android.view.View/android.widget.ListView/android.view.View[2]/android.widget.ListView/android.view.View[3]/android.view.View[2]")
el1.click()
print('complete sequencial first')
'''
