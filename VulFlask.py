# coding: utf-8
from RoboZap import *
from selenium import webdriver
from selenium.webdriver.common.proxy import *
import time
import sys
from selenium.webdriver import Firefox, FirefoxProfile
from selenium.common.exceptions import ElementNotVisibleException,NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from RoboZapImportScanPolicy import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
zap_handler = RoboZap('127.0.0.1:8090','8090')
context_id = ''
s = RoboZapImportScanPolicy('127.0.0.1:8090','8090')
from selenium.webdriver.firefox.options import Options
options=Options()
options.headless=True
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True

def run_zap_in_headless_mode():
    try:
        print("Initiate ZAP")
        path = "/ZAP_2.7.0/"
        zap_handler.start_headless_zap(path)
    except Exception as e:
        print(e)

fp = FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/png,")
fp.set_preference('startup.homepage_welcome_url', 'about:blank')
fp.set_preference("browser.startup.page", "0")
fp.set_preference("browser.startup.homepage", "about:blank")
fp.set_preference("browser.safebrowsing.malware.enabled", "false")
fp.set_preference("startup.homepage_welcome_url.additional", "about:blank")
fp.set_preference("network.proxy.type", 1)
fp.set_preference("network.proxy.http", 'localhost')
fp.set_preference("network.proxy.http_port", 8090)
fp.set_preference("network.proxy.ssl", 'localhost')
fp.set_preference("network.proxy.ssl_port", 8090)
fp.set_preference("network.proxy.no_proxies_on", "*.googleapis.com,*.google.com,*.gstatic.com,*.googleapis.com,*.mozilla.net,*.mozilla.com,ocsp.pki.goog")
fp.update_preferences()

def log_exception(e):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print( "[ + ]  Line no :{0} Exception {1}".format(exc_traceback.tb_lineno,e))

def get_driver():
    driver = Firefox(fp,options=options)
    print("Initialized firefox driver")
    driver.maximize_window()
    driver.implicitly_wait(120)
    return driver

firstname = "appsecengineer"
lastname = "ase"
email = "ase@appsecengineer.com"
password = "Test@1234"
remarks = "best way to learn infosec"

customername = "appsecengineer"
url = "https://appsecengineer.com"

class VulFlask(object):
    def __init__(self, proxy_host = 'localhost', proxy_port = '8090', target = sys.argv[1]):
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.target = target
    def run_script(self):
        try:
            driver = get_driver()
            driver.maximize_window()
            driver.implicitly_wait(10)
            time.sleep(20)
            print("[+] ================ Implicit Wait is Set =================")
            url = self.target
            driver.get('%s' % url)
            driver.implicitly_wait(10)
            time.sleep(20)
            print('[+] ' + driver.current_url)
            try:
                #Signup Begins
                driver.get("{0}/signup".format(sys.argv[1]))
                driver.implicitly_wait(20)
                time.sleep(5)
                
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[1]/input").clear()
                driver.implicitly_wait(20)
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[1]/input").send_keys(firstname)
                driver.implicitly_wait(20)
                time.sleep(3)
                
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[2]/input").clear()
                driver.implicitly_wait(20)
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[2]/input").send_keys(lastname)
                driver.implicitly_wait(20)
                time.sleep(3)
                
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[3]/input").clear()
                driver.implicitly_wait(20)
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[3]/input").send_keys(email)
                driver.implicitly_wait(20)
                time.sleep(3)
                
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[4]/input").clear()
                driver.implicitly_wait(20)
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[4]/input").send_keys(password)
                driver.implicitly_wait(20)
                time.sleep(3)
                
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[5]/input").clear()
                driver.implicitly_wait(20)
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[5]/input").send_keys(remarks)
                driver.implicitly_wait(20)
                time.sleep(3)
                
                #signupbutton
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/input").click()
                driver.implicitly_wait(20)
                time.sleep(5)
                print("Signup Successfull")
                
                #Login Begins
                driver.get("{0}".format(sys.argv[1]))
                driver.implicitly_wait(20)
                time.sleep(5)
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[1]/input").clear()
                driver.implicitly_wait(20)
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[1]/input").send_keys(email)
                driver.implicitly_wait(20)
                time.sleep(3)
                #password
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[2]/input").clear()
                driver.implicitly_wait(20)
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/div[2]/input").send_keys(password)
                driver.implicitly_wait(20)
                time.sleep(3)
                #loginbutton
                driver.find_element_by_xpath("/html/body/div/div/div/div/form/input").click()
                driver.implicitly_wait(20)
                time.sleep(5)
                print("Login successfull")
                driver.get("{0}/home".format(sys.argv[1]))
                driver.implicitly_wait(20)
                time.sleep(5)
                
                #CreateCustomer
                driver.get("{0}/customer".format(sys.argv[1]))
                driver.implicitly_wait(20)
                time.sleep(5)
                
                driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/form/input[1]").clear()
                driver.implicitly_wait(20)
                driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/form/input[1]").send_keys(customername)
                driver.implicitly_wait(20)
                time.sleep(3)
                
                driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/form/input[2]").clear()
                driver.implicitly_wait(20)
                driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/form/input[2]").send_keys(url)
                driver.implicitly_wait(20)
                time.sleep(3)
                
                #createcustomerbutton
                driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/form/input[3]").click()
                driver.implicitly_wait(20)
                time.sleep(5)
                
                print("Customer Added Successfull")
            except BaseException as e:
                print(e)
                pass
        except BaseException as e:
                print(e)
                pass

def context_zap_results():
    try:
        context_id = zap_handler.zap_define_context("VulFlask_context",sys.argv[1])
    except Exception as e:
        print(e)

def run_zap_active_scan():
    try:
        s = RoboZapImportScanPolicy('127.0.0.1:8090','8090')
        scanId = zap_handler.zap_start_ascan(context_id,sys.argv[1],'Default Policy')
        print('Start Active scan. Scan ID equals ' + scanId)
        while (int(s.get_scan_status(scanId)) < 100):
            print('Active Scan progress: ' + s.get_scan_status(scanId) + '%')
            time.sleep(5)
        print('Active Scan completed')
        export_zap_report_of_scan()
        get_html_report()
    except Exception as e:
        print(e)

def export_zap_report_of_scan():
    try:
        zap_handler.zap_export_report("/zap_results/VulFlask_parametrized_zap_scan.xml","xml","VulFlask_parametrized_zap_scan.xml","abhishekwe45")
        zap_handler.zap_export_report("/zap_results/VulFlask_parametrized_zap_scan.json","json","VulFlask_parametrized_zap_scan.json","abhishekwe45")
    except Exception as e:
        print(e)

def get_html_report():
    try:
        s = RoboZapImportScanPolicy('127.0.0.1:8090','8090')
        s.import_html_report("VulFlask_parametrized_zap_scan.html")
    except Exception as e:
        print(e)

def kill_zap():
    try:
        zap_handler.shutdown()
    except Exception as e:
        print(e)

run_zap_in_headless_mode()
s = VulFlask()
s.run_script()
context_zap_results()
run_zap_active_scan()
# kill_zap()
