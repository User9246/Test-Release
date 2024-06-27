import requests
import time         

LongLine = "-----------"

EnterURL = input("Enter a url: ")                
SavedURL = requests.get(EnterURL)                  
print(f"URL entered: {EnterURL}")                
                                                   
def data():
  print(LongLine)
  print(f"HTTP Status: {SavedURL}")    
  print(LongLine)
  print("About to display page...")
  print(LongLine)
  time.sleep(5)
  print(SavedURL.text)
  print(LongLine)
  print("Displaying Headers...")
  print(LongLine)
  time.sleep(3)
  print(SavedURL.headers)
  print(LongLine)
  print("Finished!")
    
data()
