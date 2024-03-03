print("________match case________")
x=int(input("enter age: "))
match x:
    case 0:
        print("baby")
    case 2:
        print("2 yr old")
    case _ if x<12 and x>0:
        print("child")
    case _ if x<19:
        print("teenager")
    case _ if x>18 and x<100:
        print("adult")
    case _ :
        print("error")



print("________AsyncIO________")
#allows for high-performance I/O operations in a concurrent and non-blocking manner. 
import time
import asyncio 
import requests


async def function1():
  print("func 1") 
  URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
  response = requests.get(URL)
  open("instagram.jpg", "wb").write(response.content)
   
  return "Harry"
  
async def function2():
  print("func 2") 
  URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram2.jpg", "wb").write(response.content)
  
async def function3():
  print("func 3")
  URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram3.jpg", "wb").write(response.content)

async def main():
  # await function1()     #in this method file will get download one by one 
  # await function2()
  # await function3()
  # return 3
  L = await asyncio.gather(   # this will gather all 3 function and allow them to execute concurrently . so all three file will get download at same time 
        function1(),
        function2(),
        function3(),
    )
  print(L)

asyncio.run(main())