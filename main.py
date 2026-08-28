import subprocess
from time import sleep
from tkinter import messagebox
import shutil
import os

def ShowAndVerifyChoices():
    messagebox.showinfo("Verify that this is right", "We will display a preview of the app. Please close it to continue.")
    webview.create_window(appName.get(), appURL.get())
    webview.start()
    res = messagebox.askyesno("Verify that this is right", "Was everything correct?")
    if res == True:
        print("Continue")
        messagebox.showinfo("WEB2app GUI","The app will now be built!")
        with open("app.py", "a") as file:
            file.write("""    
import webview
webview.create_window('"""+appName.get()+"""', '"""+appURL.get()+"""')
webview.start()
            """)
        subprocess.run(["cls"], shell=True)
        subprocess.run(["pyinstaller", "app.py", "--onefile", "--noconsole"])
        messagebox.showinfo("WEB2app GUI", "The app has been built! Quickly cleaning up files.")
        os.remove("app.py")
        os.remove("app.spec")
        shutil.rmtree("build")
        messagebox.showinfo("WEB2app GUI", "Done! The build is available in /dist directory")

        


import sys
if sys.stdin is None or not sys.stdin.readable():
    print("No console available — this build can't take input.")
    print("Please run the executable from Command Prompt!")
    exit()

print("Attempting to install dependencies!")
messagebox.showinfo("WEB2app GUI", "Updating all dependencies!")

subprocess.run(["pip", "install", "pywebview", "pyinstaller", "customtkinter"])
print("Done!")

import webview
from customtkinter import *

sleep(0.45)
subprocess.run(["cls"], shell=True)

app = CTk()
app.title("WEB2app Converter")
app.geometry("400x170")

label = CTkLabel(app, text="WEB2app")
label.grid(row=0, column=1, padx=0, pady=0)

appName = CTkEntry(app, placeholder_text="Input the title for your app here!")
appName.grid(row=1, column=1, sticky="ew", padx=20, pady=5)

appURL = CTkEntry(app, placeholder_text="Enter the URL here! (MUST start with https://)")
appURL.grid(row=2, column=1, sticky="ew", padx=20, pady=5)

button = CTkButton(app, text="Next", command=ShowAndVerifyChoices)
button.grid(row=3, column=1, padx=20, pady=20)

app.columnconfigure(1, weight=1)

app.mainloop()

# print("Welcome to WEB2app")
# print("What should your app be titled?")
# WindowTitle = input("> ")
# print("Ok! Enter the link to the website.")
# SiteURL = "https://"+input("> https://")
# print("Previewing site!")
# print("Close the window to continue.")

# webview.create_window(WindowTitle, SiteURL)
# webview.start()

# print("Would you like to package this as an app? [Y/n]")
# resp = input("> ")

# if resp.lower() == "n":
#     subprocess.run(["cls"], shell=True)
#     print("Exited!")
#     exit()

# subprocess.run(["cls"], shell=True)
# print("Preparing files!")

# with open("temp.py", "a") as file:
#     file.write("""    
# import webview
# webview.create_window('"""+WindowTitle+"""', '"""+SiteURL+"""')
# webview.start()
#     """)

# print("Creating app!")
# sleep(0.4)

# subprocess.run(["cls"], shell=True)
# subprocess.run(["pyinstaller", "temp.py", "--onefile", "--noconsole"])
# subprocess.run(["cls"], shell=True)

# print("Done building app. Cleaning up temp files!")
# print("not actually gonna clean up >:)")

# # subprocess.run()