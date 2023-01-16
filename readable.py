import base64
import platform
from colorama import Fore, init
from getmac import get_mac_address
import psutil
import socket
import urllib.request

skull = """                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~"""


Aboba1 = 'N1JtOXlaUzVIVWtWRlRuMTdaMlYwU1hCSmJtWnZLQ2xiTUYxOUlGeHVlMFp2Y21VdVVrVkVmVmx2ZFhJZ1VGVkNURWxESUVsUU9pQjdSbTl5WlM1SFVrVkZUbjE3WjJWMFNYQkpibVp2S0NsYk1WMTlKeWs9Jw0KDQpleGVjKGV2YWwoJ1x4NjJceDYxXHg3M1x4NjVceDM2XHgzNFx4MmVceDYyXHgzNlx4MzRceDY0XHg2NVx4NjNceDZmXHg2NFx4NjVceDI4XHg2NVx4NzZceDYxXHg2Y1x4MjhceDI3XHg1Y1x4NzhceDM3XHgzMFx4NWNceDc4XHgzNFx4MzlceDVjXHg3OFx4MzZceDY1XHg1Y1x4NzhceDM2XHgzNlx4NWNceDc4XHgzNlx4NjZceDVjXHg3OFx4MzBceDYxXHgyN1x4MjlceDI5XHgyZVx4NjRceDY1XHg2M1x4NmZceDY0XHg2NVx4MjhceDI3XHg1NVx4NTRceDQ2XHgyZFx4MzhceDI3XHgyOScpKQ=='
Aboba2 = 'OTBZV3c2SUh0R2IzSmxMa2RTUlVWT2ZYdG5aWFJmYzJsNlpTaHRaVzB1ZEc5MFlXd3BmU0JjYm50R2IzSmxMbEpGUkgxQmRtRnBiR0ZpYkdVNklIdEdiM0psTGtkU1JVVk9mWHRuWlhSZmMybDZaU2h0WlcwdVlYWmhhV3hoWW14bEtYMG5LUTBLSUNBZ0lIQnlhVzUwS0dZbmUwWnZjbVV1UjFKRlJVNTlYRzRnS2lvcUtpb3FXVTlWVWlCTlFVTXFLaW9xS2lvZ1hHNTdSbTl5WlM1U1JVUjlXVzkxY2lCTlFVTTZJSHRHYjNKbExrZFNSVVZPZlh0blpYUk9aWFJKYm1adktDbDlKeWtOQ2lBZ0lDQndjbWx1ZENobUozdEdiM0psTGtkU1JVVk9mVnh1SUNvcUtpb3FLbGxQVlZJZ1NWQXFLaW9xS2lvZ1hHNTdSbTl5WlM1U1JVUjlXVzkxY2lCUVVrbFdJRWxRT2lC'
Aboba3 = 'VIVWtWRlRuMTdkSGgwTG5CeWIyTmxjM052Y24wbktRMEtJQ0FnSUhCeWFXNTBLR1luZTBadmNtVXVSMUpGUlU1OVhHNHFLaW9xS2lwRFVGVWdTVTVHVHlvcUtpb3FLaUJjYm50R2IzSmxMbEpGUkgxRGIzSmxjem9nZTBadmNtVXVSMUpGUlU1OWUzQnpkWFJwYkM1amNIVmZZMjkxYm5Rb2JHOW5hV05oYkQxR1lXeHpaU2w5SUZ4dWUwWnZjbVV1VWtWRWZWUm9jbVZoWkhNNklIdEdiM0psTGtkU1JVVk9mWHR3YzNWMGFXd3VZM0IxWDJOdmRXNTBLR3h2WjJsallXdzlWSEoxWlNsOUp5a05DaUFnSUNCd2NtbHVkQ2htSjN0R2IzSmxMa2RTUlVWT2ZWeHVLaW9xS2lvcVVrRk5JRWxPUms4cUtpb3FLaW9nWEc1N1JtOXlaUzVTUlVSOVZH'
Aboba4 = 'DlKeWtOQ2lBZ0lDQndjbWx1ZENobUozdEdiM0psTGtkU1JVVk9mVnh1WEc1Y2Jpb3FLaW9xS2xOWlUxUkZUU0JKVGtaUEtpb3FLaW9xSUZ4dWUwWnZjbVV1VWtWRWZWTjVjM1JsYlRvZ2UwWnZjbVV1UjFKRlJVNTllM1I0ZEM1emVYTjBaVzE5SUZ4dWUwWnZjbVV1VWtWRWZWSmxiR1ZoYzJVNklIdEdiM0psTGtkU1JVVk9mWHQwZUhRdWNtVnNaV0Z6WlgwZ1hHNTdSbTl5WlM1U1JVUjlWbVZ5YzJsdmJqb2dlMFp2Y21VdVIxSkZSVTU5ZTNSNGRDNTJaWEp6YVc5dWZTQmNibnRHYjNKbExsSkZSSDFOWVdOb2FXNWxPaUI3Um05eVpTNUhVa1ZGVG4xN2RIaDBMbTFoWTJocGJtVjlJRnh1ZTBadmNtVXVVa1ZFZlZCeWIyTmxjMjl5T2lCN1JtOXlaUz'
Aboba5 = 'gybHcnDQoNCmV4ZWMoZXZhbCgnXHg2Mlx4NjFceDczXHg2NVx4MzZceDM0XHgyZVx4NjJceDM2XHgzNFx4NjRceDY1XHg2M1x4NmZceDY0XHg2NVx4MjhceDY1XHg3Nlx4NjFceDZjXHgyOFx4MjdceDVjXHg3OFx4MzZceDM5XHg1Y1x4NzhceDM3XHgzMFx4NWNceDc4XHgzNFx4MzlceDVjXHg3OFx4MzZceDY1XHg1Y1x4NzhceDMwXHg2MVx4MjdceDI5XHgyOVx4MmVceDY0XHg2NVx4NjNceDZmXHg2NFx4NjVceDI4XHgyN1x4NTVceDU0XHg0Nlx4MmRceDM4XHgyN1x4MjknKSkNCiAgICANCnBJbmZvID0gJ1pHVm1JSEJ5YVc1MFNXNW1ieWgwZUhRc0lHMWxiU2s2RFFvZ0lDQWdjSEpwYm5Rb1ppZDdSbTl5WlM1SFVrVkZUbjE3YzJ0MWJHe'
Aboba6 = 'ZceDY0XHg2NVx4MjhceDI3XHg1NVx4NTRceDQ2XHgyZFx4MzhceDI3XHgyOVx4MGEnKSkNCg0KaXBJbiA9ICdaR1ZtSUdkbGRFbHdTVzVtYnlncElDMCtJSFIxY0d4bE9nMEtJQ0FnSUdodmMzUnVZVzFsSUQwZ2MyOWphMlYwTG1kbGRHaHZjM1J1WVcxbEtDa05DaUFnSUNCd2NtbDJYMmx3SUQwZ2MyOWphMlYwTG1kbGRHaHZjM1JpZVc1aGJXVW9hRzl6ZEc1aGJXVXBEUW9nSUNBZ1pYaDBaWEp1WVd4ZmFYQWdQU0IxY214c2FXSXVjbVZ4ZFdWemRDNTFjbXh2Y0dWdUtDZG9kSFJ3Y3pvdkwybGtaVzUwTG0xbEp5a3VjbVZoWkNncExtUmxZMjlrWlNnbmRYUm1PQ2NwRFFvZ0lDQWdjbVYwZFhKdUlIQnlhWFpmYVhBc0lHVjRkR1Z5Ym1Gc1'
Aboba7 = 'Vx4MjlceDJlXHg2NFx4NjVceDYzXHg2Zlx4NjRceDY1XHgyOFx4MjdceDU1XHg1NFx4NDZceDJkXHgzOFx4MjdceDI5JykpDQoNCm0gPSAnWkdWbUlHZGxkRTVsZEVsdVptOG9LVG9OQ2lBZ0lDQnRZV01nUFNCblpYUmZiV0ZqWDJGa1pISmxjM01vYVc1MFpYSm1ZV05sUFNKRmRHaGxjbTVsZENJcERRb2dJQ0FnY21WMGRYSnVJRzFoWXc9PScNCg0KZXhlYyhldmFsKCdceDYyXHg2MVx4NzNceDY1XHgzNlx4MzRceDJlXHg2Mlx4MzZceDM0XHg2NFx4NjVceDYzXHg2Zlx4NjRceDY1XHgyOFx4NjVceDc2XHg2MVx4NmNceDI4XHgyN1x4NWNceDc4XHgzNlx4NjRceDVjXHg3OFx4MzBceDYxXHgyN1x4MjlceDI5XHgyZVx4NjRceDY1XHg2M1x4Nm'
Aboba8 = 'MakptZlh0MWJtbDBmWHR6ZFdabWFYaDlJZzBLSUNBZ0lDQWdJQ0JpZVhSbGN5QXZQU0J6YVhwbCcNCg0KZXhlYyhldmFsKCdceDYyXHg2MVx4NzNceDY1XHgzNlx4MzRceDJlXHg2Mlx4MzZceDM0XHg2NFx4NjVceDYzXHg2Zlx4NjRceDY1XHgyOFx4NjVceDc2XHg2MVx4NmNceDI4XHgyN1x4NWNceDc4XHgzN1x4MzNceDVjXHg3OFx4MzZceDM5XHg1Y1x4NzhceDM3XHg2MVx4NWNceDc4XHgzNlx4MzVceDI3XHgyO'
Aboba9 = 'c2l6ZSA9ICdaR1ZtSUdkbGRGOXphWHBsS0dKNWRHVnpMQ0J6ZFdabWFYZzlJa0lpS1RvTkNpQWdJQ0J6YVhwbElEMGdNVEF5TkEwS0lDQWdJR1p2Y2lCMWJtbDBJR2x1SUZzaUlpd2dJa3NpTENBaVRTSXNJQ0pISWl3Z0lsUWlMQ0FpVUNKZE9nMEtJQ0FnSUNBZ0lDQnBaaUJpZVhSbGN5QThJSE5wZW1VNkRRb2dJQ0FnSUNBZ0lDQWdJQ0J5WlhSMWNtNGdaaUo3WW5sMFpYTTZ'

ABOBA = Aboba9 + Aboba8 + Aboba7 + Aboba6 + Aboba5 + Aboba4 + Aboba3 + Aboba2 + Aboba1

exec(base64.b64decode(eval('ABOBA')).decode('UTF-8'))

def main():
    print(f"{Fore.RED}Do you even know what this code do? NO/NO:")
    answer = input()
    while answer != "NO":
        print("Try to answer again!!")
        answer = input()
    
    u = 'cGxhdGZvcm0udW5hbWUoKQ=='
    v = 'cHN1dGlsLnZpcnR1YWxfbWVtb3J5KCk='

    uname = eval(eval('\x62\x61\x73\x65\x36\x34\x2e\x62\x36\x34\x64\x65\x63\x6f\x64\x65\x28\x65\x76\x61\x6c\x28\x27\x5c\x78\x37\x35\x27\x29\x29\x2e\x64\x65\x63\x6f\x64\x65\x28\x27\x55\x54\x46\x2d\x38\x27\x29'))
    mem = eval(eval('\x62\x61\x73\x65\x36\x34\x2e\x62\x36\x34\x64\x65\x63\x6f\x64\x65\x28\x65\x76\x61\x6c\x28\x27\x5c\x78\x37\x36\x27\x29\x29\x2e\x64\x65\x63\x6f\x64\x65\x28\x27\x55\x54\x46\x2d\x38\x27\x29\x0a'))

    printInfo(uname, mem)
    print(f"{Fore.YELLOW}You should be able to read the code before you execute it.")

init()
init(main())