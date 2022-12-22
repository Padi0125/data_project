from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager #크롬드라이버 자동 업데이트

import pandas as pd
from datetime import datetime

#크롬 드라이버 준비
chrome_options = Options()
chrome_options.add_argument("headless") #백그라운드에서 작업
chrome_options.add_experimental_option("detach", True)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def jobkr(text):
    save = []
    conts = 0

    #웹 페이지 백그라운드 열기
    url = f'https://www.jobkorea.co.kr/search/?stext={text}&tabType=recruit&Page_No=1'
    driver.get(url)
    
    #페이지 개수 확인
    cont = driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[1]/div/div[2]/div[1]/p/strong').text
    cont = cont.replace(',', '')
    paeg_num = (int(cont)//20)+1

    #페이지 내용 가져오기 & 페이지 넘기기
    try:
        for i in range(1,paeg_num+1):
            url = f'https://www.jobkorea.co.kr/search/?stext={text}&tabType=recruit&Page_No={i}'
            driver.get(url)

            for j in range(1,20+1):
                try:
                    title_link = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/a')
                    tag1 = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/p[1]/span[1]').text
                    tag2 = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/p[1]/span[2]').text
                    tag3 = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/p[1]/span[3]').text   
                    tag4 = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/p[1]/span[5]').text
                    tag5 = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/p[1]/span[6]').text
                    link=title_link.get_attribute('href')
                    
                except:
                    try:
                        title_link = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/a')
                        tag1 = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/p[1]/span[1]').text
                        tag2 = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/p[1]/span[2]').text
                        tag3 = "null"
                        tag4 = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/p[1]/span[4]').text
                        tag5 = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/p[1]/span[5]').text
                        link=title_link.get_attribute('href')
                        
                    except:
                        title_link = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/a')
                        tag1 = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/p[1]/span[1]').text
                        tag2 = "null"
                        tag3 = "null"
                        tag4 = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/p[1]/span[3]').text
                        tag5 = driver.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{j}]/div/div[2]/p[1]/span[4]').text
                        link=title_link.get_attribute('href')
                conts+=1  
                save.append([title_link.text,link,tag1,tag2,tag3,tag4,tag5])
                print(conts)
                if int(cont) == conts:
                    print('작업 완료')
                    break
        data_save = pd.DataFrame(save, columns = ['제목','링크','경력','학력','고용형태','지역','모집일'])        
        data_save.to_csv(str(datetime.today().strftime("%Y%m%d"))+f'{text}job_list.csv', index = False)
        print(f'{conts}개의 취업 정보가 확인 됐습니다.')  
    except:
        print('현재 지원하지 않는 형태입니다.')
jobkr('파이썬')