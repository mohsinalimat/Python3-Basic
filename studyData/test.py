ff_driver = webdriver.chrome()
ff_driver.get("https://www.google.co.kr/")

query = ff_driver.find_element_by_id("lst-ib")
query.send_keys(" ")

ff_driver.find_element_by_name("btnK").click()
ff_driver.implicitly_wait(10)
