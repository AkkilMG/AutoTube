from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

async def youtubeUploadVideo(driver, data):
    try:
        sleep(2)
        driver.get("https://studio.youtube.com/channel/UCDAylnB8oNzBBCiS8w_m3ng/videos?d=ud")
        WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
        sleep(5)
        print('+++++++++++++++ Opened YouTube Studio +++++++++++++++')
        driver.find_element(By.XPATH, "//button[@class='ytcp-button-shape-impl ytcp-button-shape-impl--filled ytcp-button-shape-impl--mono ytcp-button-shape-impl--size-m' and @aria-label='Select files']").click()
        # file_input = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "//input[@type='file']"))
        # )
        # file_input.send_keys(data.file)
        
        # # Wait until the file upload starts or completes
        # WebDriverWait(driver, 300).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'upload-complete-indicator-class')]"))
        # )

       
        # Wait until the title and description textboxes are present
        textboxes = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "textbox"))
        )
        sleep(2)
        # Set the title and description
        driver.execute_script(f"arguments[0].innerText = '{data['title']}';", textboxes[0])
        sleep(1)
        driver.execute_script("arguments[0].innerText = '"+data['description'].replace('\'', '\\\'')+"';", textboxes[1])
        sleep(1)
        print('+++++++++++++++ Title and Description updated +++++++++++++++')

        # Need to verify with phone number
        # thumbnail_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'remove-default-style style-scope ytcp-thumbnail-editor')]"))
        # )
        # thumbnail_button.click()
        # print('+++++++++++++++ Clicked thumbnail button +++++++++++++++')

        off_radio_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "offRadio"))
        )
        off_radio_buttons[1].click()
        print('+++++++++++++++ Clicked the second offRadio button +++++++++++++++')
        
        sleep(1)
        next_button = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, 'ytcp-button-shape-impl ytcp-button-shape-impl--filled ytcp-button-shape-impl--mono ytcp-button-shape-impl--size-m')]"))
        )
        next_button[0].click()

        sleep(1)
        next_button = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, 'ytcp-button-shape-impl ytcp-button-shape-impl--filled ytcp-button-shape-impl--mono ytcp-button-shape-impl--size-m')]"))
        )
        next_button[0].click()
        print('+++++++++++++++ Clicked the next button +++++++++++++++')

        sleep(1)
        off_radio_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "offRadio"))
        )
        off_radio_buttons[0].click()
        print('+++++++++++++++ Make video private +++++++++++++++')

        sleep(1)
        save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, 'ytcp-button-shape-impl ytcp-button-shape-impl--filled ytcp-button-shape-impl--mono ytcp-button-shape-impl--size-m')]"))
        )
        save_button[1].click()
        print('+++++++++++++++ Clicked the save button +++++++++++++++')

        sleep(20)
        return { 'success': True, 'driver': driver }
    except Exception as e:
        print(f"Exception occurred (youtubeUploadVideo): {e}")
        return { 'success': False }
