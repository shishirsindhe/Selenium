from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
chrome_options=Options()
chrome_options.add_experimental_option(name="detach",value=True)
driver=Chrome(chrome_options)
driver.maximize_window()

# Slider Actions
# driver.get("https://snapdeal.com/")
# driver.find_element("xpath","//input[@class='col-xs-20 searchformInput keyword']").send_keys("mobiles")
# sleep(5)
# driver.find_element("xpath","//span[@class='searchTextSpan']").click()
# element=driver.find_element("xpath","//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
# action=ActionChains(driver)
# action.click_and_hold(element).pause(2).move_by_offset(-50,0).perform()

########################################################################################################################

# Scroll to element using ActionChains
# driver.find_element("xpath","//input[@class='col-xs-20 searchformInput keyword']").send_keys("Kitchen Product")
# sleep(5)
# driver.find_element("xpath","//span[@class='searchTextSpan']").click()
# element=driver.find_element("xpath","//div[@data-filtername='BodyMaterial_s']")
# action.scroll_to_element(element).perform()

########################################################################################################################

# Script Execution Scroll (without in-built methods)
# loc=element.location
# driver.execute_script(f"window.scrollBy({loc['x']},{loc['y']})")

########################################################################################################################
# driver.get("https://www.google.co.in/search?q=shishir+sindhe&sca_esv=f4efe242ec4104b1&sca_upv=1&sxsrf=ADLYWIJqKZOol_k-tErl0Yxaalh4kxrY6A%3A1723194627072&source=hp&ei=A921ZtMJu4C-vQ-AyuvYDw&iflsig=AL9hbdgAAAAAZrXrEzd_oRRgp1zOAa2dOwsaD95P_wp9&ved=0ahUKEwiTl_ycyOeHAxU7gK8BHQDlGvsQ4dUDCBk&uact=5&oq=shishir+sindhe&gs_lp=Egdnd3Mtd2l6Ig5zaGlzaGlyIHNpbmRoZTIHEC4YgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIGEAAYDRgeMgYQABgNGB4yBhAAGA0YHjIGEAAYDRgeSOJpUKUSWK1kcAt4AJABAJgBpgGgAZoWqgEEMi4yMrgBA8gBAPgBAZgCI6ACwBeoAgrCAgcQIxgnGOoCwgIHEC4YJxjqAsICDRAuGNEDGMcBGCcY6gLCAgoQIxiABBgnGIoFwgILEAAYgAQYkQIYigXCAg4QLhiABBixAxiDARiKBcICCxAAGIAEGLEDGIMBwgIREC4YgAQYsQMY0QMYgwEYxwHCAgoQLhiABBgnGIoFwgIQEC4YgAQY0QMYQxjHARiKBcICEBAAGIAEGLEDGEMYgwEYigXCAhEQLhiABBixAxiDARjUAhiKBcICChAAGIAEGEMYigXCAgoQLhiABBhDGIoFwgINEC4YgAQYsQMYQxiKBcICERAuGIAEGMcBGJgFGI4FGK8BwgIFEAAYgATCAggQLhiABBixA8ICDRAAGIAEGLEDGEMYigXCAhAQABiABBixAxhDGMkDGIoFwgILEAAYgAQYkgMYigXCAgsQLhiABBixAxjUAsICChAAGIAEGAIYywHCAgsQLhiABBixAxiDAcICCBAAGIAEGLEDwgIOEC4YgAQYxwEYjgUYrwHCAgsQLhiABBjHARivAcICBRAuGIAEwgILEAAYgAQYhgMYigXCAggQABiABBiiBMICBRAhGKABwgIGEAAYFhgewgIIEAAYFhgKGB7CAgUQIRifBcICBxAhGKABGAqYAwySBwUxMy4yMqAHgOsB&sclient=gws-wiz")
# names=driver.find_elements("xpath","//div[@class='s6JM6d']/..//h3")
# shishir=[]
# for name in names:
#     shishir.append(name.text)
# print(shishir)
# for ssr in shishir:
#     if "shishir" in ssr.split():
#         print(ssr)
# for ssr in shishir:
#     if "Shishir" in shishir:
#          print(ssr)

########################################################################################################################