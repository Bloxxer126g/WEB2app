import shutil, os, platform, subprocess
from tkinter import messagebox, filedialog
from time import sleep

HTMLCONT = ""

Clear_CMD = "clear"
if platform.system() == "Windows":
    Clear_CMD = "cls"

def ShowAndVerifyChoices():
    global HTMLCONT

    Name = appName.get()
    URL = appURL.get()

    app.iconify()
    messagebox.showinfo("Verify that this is right", "We will display a preview of the app. Please close it to continue.")
    if HTMLCONT == "":
        webview.create_window(Name, URL)
    else:
        webview.create_window(Name, html=HTMLCONT)
    webview.start()
    res = messagebox.askyesno("Verify that this is right", "Was everything correct?")
    if res == True:
        print("Continue")
        messagebox.showinfo("WEB2app GUI","The app will now be built!")
        with open("app.py", "a") as file:
            if HTMLCONT == "":
                file.write("""    
import webview
webview.create_window('"""+Name+"""', '"""+URL+"""')
webview.start()
                """)
            else:
                file.write("""    
import webview
webview.create_window('"""+Name+"""', html='''"""+HTMLCONT+"""''')
webview.start()
                """)
        subprocess.run([Clear_CMD], shell=True)
        subprocess.run(["pyinstaller", "app.py", "--onefile", "--noconsole"])
        messagebox.showinfo("WEB2app GUI", "The app has been built! Quickly cleaning up files.")
        os.remove("app.py")
        os.remove("app.spec")
        shutil.rmtree("build")
        messagebox.showinfo("WEB2app GUI", "Done! The build is available in /dist directory")
        app.destroy()
        exit()
    else:
        app.deiconify()

def PickHTMLfile():
    global HTMLCONT
    filetypes = (
        ("html files", "*.html")
    )

    Response = filedialog.askopenfilename(
        title="Pick a HTML file"
    )
    if Response == "":
        print("Quitting File Dialog")
        return

    print(Response)

    with open(Response, "r") as f:
        HTMLCONT = f.read()
        htmlbutton.configure(text="Uploaded HTML")
        htmlbutton.configure(fg_color="green")

print("Attempting to install dependencies!")
messagebox.showinfo("WEB2app GUI", "Updating all dependencies!")

subprocess.run(["pip", "install", "pywebview", "pyinstaller", "customtkinter"])
print("Done!")

import webview
from customtkinter import *

sleep(0.45)
subprocess.run([Clear_CMD], shell=True)

app = CTk()
app.title("WEB2app Converter")
app.geometry("400x280")

label = CTkLabel(app, text="WEB2app")
label.grid(row=0, column=1, padx=0, pady=0)

appName = CTkEntry(app, placeholder_text="Input the title for your app here!")
appName.grid(row=1, column=1, sticky="ew", padx=20, pady=5)

label2 = CTkLabel(app, text="----------")
label2.grid(row=2, column=1, padx=0, pady=0)

appURL = CTkEntry(app, placeholder_text="Enter the URL here! (MUST start with https://)")
appURL.grid(row=3, column=1, sticky="ew", padx=20, pady=5)

label3 = CTkLabel(app, text="----or----")
label3.grid(row=4, column=1, padx=0, pady=0)

htmlbutton = CTkButton(app, text="Upload HTML file", command=PickHTMLfile)
htmlbutton.grid(row=5, column=1, padx=20, pady=5)

label4 = CTkLabel(app, text="----------")
label4.grid(row=6, column=1, padx=0, pady=0)

button = CTkButton(app, text="Next", command=ShowAndVerifyChoices)
button.grid(row=7, column=1, padx=20, pady=5)


app.columnconfigure(1, weight=1)

app.mainloop()