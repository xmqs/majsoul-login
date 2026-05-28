import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

acccounts = int(len(sys.argv[1:])/2)
print(f'Config {acccounts} accounts')
for i in range(acccounts):
    email = sys.argv[1+i]
    passwd = sys.argv[1+i+acccounts]
    print('----------------------------')

    # 1. 浏览器配置（反风控）
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1280, 720)
    driver.get("https://game.maj-soul.net/1/")
    print(f'Account {i+1} loading game...')
    sleep(10)

    # 获取canvas实际尺寸和位置
    canvas_size = driver.execute_script("""
        const c = document.querySelector('canvas');
        return {width: c.width, height: c.height, rect: c.getBoundingClientRect()};
    """)
    print(f'Canvas size: {canvas_size}')
    
    # 先保存截图看当前页面状态
    driver.save_screenshot("before_login.png")
    print('Screenshot saved: before_login.png')

    # 2. 等待游戏画布加载
    try:
        screen = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "canvas"))
        )
    except:
        driver.save_screenshot(f"error_{i+1}.png")
        driver.quit()
        raise

    ActionChains(driver)\
        .move_to_element_with_offset(screen, 740, 200)\
        .click()

    driver.save_screenshot("click.png")
    print('Screenshot saved: click.png')

    # 3. 输入账号（修复：正确的Canvas输入方式）
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 740, 200)\
        .click()\
        .send_keys(email)\
        .perform()
    sleep(1)
    print('Input email successfully')

    driver.save_screenshot("email.png")
    print('Screenshot saved: email.png')
    
    driver.quit()
