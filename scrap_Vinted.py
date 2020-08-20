#APRENDER EXPORTAR OBJETOS A BASE DATOS
#IMPRIMIR OBJETOS POR CONSOLA
#EXPORTAR A CSV

import sys, time, os, pickle
from helium import *
import csv
from itertools import islice
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
timeout=3
credentials = str(sys.argv[1])
#credentials is a txt file that in the first line is your mail
# and the second one is the password.

file = open(credentials)
lines = (file.readlines())

email = lines[0]
password = lines[1]
#need to improve this code... keep ON in https://twitch.tv/javix64
class Object1:
    def __init__(self, price, like, size, brand):
        #self.user=user
        self.price=price
        self.like=like
        self.size=size
        self.brand=brand
    
    def __repr__(self):
        return str(self.__dict__)

    def print_all(self):
        print(self.price)
        print(self.like)
        print(self.brand)
        print(self.size)

def login():
    #ir a la web
    driver.get('https://www.vinted.es/member/general/login?ref_url=')
    #esperar a un elemento
    #element_present0 = EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div/div[2]/div[1]/div[3]/div/a[1]'))
    #WebDriverWait(driver, timeout).until(element_present0)
    user= driver.find_element_by_name('login')
    contrase= driver.find_element_by_name('password')
    user.send_keys(email)
    contrase.send_keys(password)
    boton_Login = driver.find_element_by_xpath('/html/body/div[4]/div/section/div/div[2]/section/div/div[2]/div/div/div/form/div[3]/div/div/button')
    boton_Login.click()

def scrap_vinted_simple():
    time.sleep(2)
    for num in range(1, 417):
        driver.get('https://www.vinted.es/vetements?catalog[]=1&page='+str(num))
        #esperamos hasta que cargue el sidebar
        element_present0 = EC.presence_of_element_located((By.ID,'sidebar'))
        WebDriverWait(driver, timeout).until(element_present0)
        time.sleep(2)
        
        array_objeto=[]
        for i in range(0,3):
            patata=Object1()
            patata.brand='brabd'+str(i)
            patata.like='like'+str(i)
            patata.size='size'+str(i)
            patata.price='price'+str(i)
            #patata.print_all()
            
            array_objeto.append(patata.print_all())
            print(array_objeto[i])        
        print('00000000000000000000000000000000')
        html_card= []
        """
            EJEMPLO HTML_CARD:
                user=""
                like=""
                talla=""
                marca=""
        """    
        precios = driver.find_elements_by_xpath('//span[@class="Text_text__QBn4- Text_subtitle__1I9iB Text_left__3s3CR Text_amplified__2ccjx Text_bold__1scEZ"]')
            #talla = driver.find_elements_by_xpath('//div[@class="c-box__subtitle"]/span')
            #marca = driver.find_elements_by_xpath('//div[@class="c-box__details"]/span')
        likes = driver.find_elements_by_xpath('//div[@class="Cell_suffix__1Yku3"]/div/div[3]')
        for like in likes:
            html_card.append({'like='+like.text})
        for precio in precios:
            html_card.append({'price='+precio.text})
        """
        for bloque in bloques:
            
            for like in likes:
                html_card.append(like.text)
            #html_card.append(likes)
        """
        print(html_card)
        #para objetos
        #dict = {'name' : 'John Smith', 'company' : 'SalesForce'}
        #usuario = driver.find_element_by_xpath('//*[@class="Cell_link__1q9hy"]')
        
        
        
        #talla = driver.find_elements_by_xpath('//div[@class="c-box__subtitle"]/span').text
        #marca = driver.find_elements_by_xpath('//div[@class="c-box__details"]/span').text
        #print(precio)
        
        #print(talla)
        #print(marca)
        time.sleep(1)
        

login()
scrap_vinted_simple()