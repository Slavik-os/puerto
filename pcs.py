#!/usr/bin/env python3
from tkinter import *
import requests
import json
import threading
import time
import os
from pprint import pprint
import base64
from distutils.dir_util import copy_tree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
url = 'https://app.tangermedpcs.ma/'
class Program :
	def __init__(self,master):
		self.master = master

		s_y_label = Label(self.master,text='Début-années :').grid(row=1)
		s_y_entry = Entry(self.master,text='')
		s_y_entry.grid(row=1,column=1,ipadx=2,padx=10, pady=10)



		s_m_label = Label(self.master,text='Début-mois : ').grid(row=2)
		s_m_entry = Entry(self.master,text='')
		s_m_entry.grid(row=2,column=1,ipadx=2,padx=10, pady=10)
		
		s_d_label = Label(self.master,text='Début-jour : ').grid(row=3)
		s_d_entry = Entry(self.master,text='')
		s_d_entry.grid(row=3,column=1,ipadx=2,padx=10, pady=10)

		Label(self.master,text='--------------------------------------------------------').grid(row=4,column=1)

		e_y_label = Label(self.master,text='fin-années :').grid(row=5)
		e_y_entry = Entry(self.master,text='')
		e_y_entry.grid(row=5,column=1,ipadx=2,padx=10, pady=10)



		e_m_label = Label(self.master,text='fin-mois : ').grid(row=6)
		e_m_entry = Entry(self.master,text='')
		e_m_entry.grid(row=6,column=1,ipadx=2,padx=10, pady=10)
		
		e_d_label = Label(self.master,text='fin-jour : ').grid(row=7)
		e_d_entry = Entry(self.master,text='')
		e_d_entry.grid(row=7,column=1,ipadx=2,padx=10, pady=10)

		submit = Button(self.master,text='Submit',command=lambda:getJson(s_y_entry.get(),s_m_entry.get(),s_d_entry.get(),e_y_entry.get(),e_m_entry.get(),e_d_entry.get()))
		submit.grid(row=8,column=1,ipadx=2,padx=10,pady=10)


		def auto_login(self,url,start_date,end_date):
			driver = webdriver.Chrome(executable_path='chromedriver.exe') # Full Path for The Driver
			driver.set_window_position(-10000,0) # hide browser
			driver.get('https://app.tangermedpcs.ma/')

			time.sleep(2)
			username = driver.find_element_by_name('user')
			username.send_keys(base64.b64decode('dXNlcm5hbWVfaGVyZQ==').decode('utf-8'))
			time.sleep(1)
			password = driver.find_element_by_name('password')
			password.send_keys(base64.b64decode('cGFzc3dvcmRfaGVyZQ==').decode('utf-8'))
			time.sleep(2)
			driver.find_element_by_css_selector('.buttonRipples').click()
			# end login

			#get json
			time.sleep(1)

			driver.get(f'https://app.tangermedpcs.ma/api/fatourati/factures/search?devise=MAD&num-unite=&type=FACTURE&num-rows=ALL&date-debut={start_date}&date-fin={end_date}&numRows=ALL&dateDebut=2021-10-12&dateFin=2021-10-14')
			js = driver.find_element_by_tag_name('body').text
			driver.close()
			with open ('file.json','w') as js_file :
				js_file.write(js)

			with open ('file.json','r') as js_file :
				data = json.load(js_file)['result']['factures']
				os.chdir('test_folder')
				l = []
				n = []
				for d in data :
					l.append(d['invoiceNumber'])
					n.append(d['numService'])

		
					
			z = []
			for file in os.listdir(): # get files inside test_Folder 
				if file in n :		# if file in list of names 
					z.append(file)

			for i in range(len(z)) :
				f = os.path.join(os.getcwd(),z[i])	# get full path of file
				r= r'C:\Users\a.elkalkha\Desktop\PCS\founds' # copy folder
				b = r'C:\Users\a.elkalkha\Desktop\PCS\test_folder' # test folder
				file_name = os.listdir(f)[0]
					
				copy_folder = os.path.join(r,n[i])
				print(copy_folder)
				if os.path.exists(copy_folder):
					pprint('Duplicated !')
					continue
				else :
					os.mkdir(copy_folder)
					os.chdir(copy_folder)
					copy_tree(f,copy_folder)
					os.chdir(b)
					pprint(os.getcwd())	
			time.sleep(30)
			
		


		def getJson(yyyy,mm,dd,yyyyE,mmE,ddE):
			start_date = f'{yyyy}-{mm}-{dd}'
			print(start_date)
			end_date = f'{yyyyE}-{mmE}-{ddE}'
			print(end_date)
			auto_login(True,'https://app.tangermedpcs.ma/',start_date,end_date)
		







root = Tk()
program = Program(root)
root.mainloop()