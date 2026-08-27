import subprocess
import webview
from time import sleep

print("Attempting to install dependencies!")

subprocess.run(["pip", "install", "pywebview", "pyinstaller"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Done!")

sleep(0.45)
subprocess.run(["cls"], shell=True)

print("Welcome to WEB2app")
print("What should your app be titled?")
WindowTitle = input("> ")
print("Ok! Enter the link to the website.")
SiteURL = "https://"+input("> https://")
print("Previewing site!")
print("Close the window to continue.")

webview.create_window(WindowTitle, SiteURL)
webview.start()

print("Would you like to package this as an app? [Y/n]")
resp = input("> ")

if resp.lower() == "n":
    subprocess.run(["cls"], shell=True)
    print("Exited!")
    exit()

subprocess.run(["cls"], shell=True)
print("Preparing files!")

with open("temp.py", "a") as file:
    file.write("""    
import webview
webview.create_window('"""+WindowTitle+"""', '"""+SiteURL+"""')
webview.start()
    """)

print("Creating app!")
sleep(0.4)

subprocess.run(["cls"], shell=True)
subprocess.run(["pyinstaller", "temp.py", "--onefile", "--noconsole"])
subprocess.run(["cls"], shell=True)

print("Done building app. Cleaning up temp files!")
print("not actually gonna clean up >:)")

# subprocess.run()