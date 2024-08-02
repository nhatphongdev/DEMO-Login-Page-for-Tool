from colorama import Fore,init  # Import Style for color reset

import os
import time
import webbrowser

gr = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
black = Fore.BLACK
mg = Fore.MAGENTA
w = Fore.WHITE

init(autoreset=True)
# KEY DEMO
key = "abcd-efgh-ik09"
keyvip = "keyvip-abcd-efgh"
loadingtext = f"{Fore.LIGHTBLUE_EX}Vui Lòng Chờ Vài Giây Để Tải Tool..."
errorkeytext = f"{Fore.RED}Key Không Chính Xác!"

logotext = f"""{Fore.LIGHTMAGENTA_EX}
░██████╗░███╗░░██╗░█████╗░███████╗
██╔════╝░████╗░██║██╔══██╗██╔════╝
██║░░██╗░██╔██╗██║██║░░██║█████╗░░
██║░░╚██╗██║╚████║██║░░██║██╔══╝░░
╚██████╔╝██║░╚███║╚█████╔╝██║░░░░░
░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░░░░ source by nhatphong.dev"""

print(logotext)
print(f"""{gr}
                CHỌN SỐ
    {w}[{blue}1{w}] {mg}Đăng Nhập Key Thường
    {w}[{blue}2{w}] {mg}Đăng Nhập Key VIP
    {w}[{blue}3{w}] {mg}Trợ Giúp

""")
novip = False
vip = False
choose = input(f"{mg}$ {red}> ")

if choose == '1':
    print(f"{blue}Vui Lòng Nhập Key!")
    inputkey = input(f"{mg}$ {red}> ")
    if inputkey == key:
        print(f"{gr}Đăng Nhập Thành Công")
        novip = True
        time.sleep(1)
        print(f"{blue}{loadingtext}")
        time.sleep(3)
        os.system("cls")
    else:
        print(f"{errorkeytext}")
        time.sleep(3)

elif choose == '2':
    print(f"{blue}Vui Lòng Nhập Key!")
    inputkey = input(f"{mg}$ {red}> ")
    if inputkey == keyvip:
        print(f"{gr}Đăng Nhập Thành Công")
        vip = True
        time.sleep(1)
        print(f"{blue}{loadingtext}")
        time.sleep(3)
        os.system("cls")
    else:
        print(f"{errorkeytext}")
        time.sleep(3)

elif choose == '3':
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUJcmljayByb2xs")

if novip == True:
    print(f"{blue}Chào mừng người dùng thường!")
    input("Bấm Enter để thoát...")
elif vip == True:
    print(f"{blue}Chào mừng người dùng VIP!")
    input("Bấm Enter để thoát...")