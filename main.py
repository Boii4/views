import sys
import os
import threading
import random
from colorama import Fore, Style
from time import strftime, gmtime, time, sleep

def logo():
    try:
        print(Fore.LIGHTBLUE_EX)
        msg = f"""
        ████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗    ██╗   ██╗██╗███████╗██╗    ██╗██████╗  ██████╗ ████████╗
        ╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝    ██║   ██║██║██╔════╝██║    ██║██╔══██╗██╔═══██╗╚══██╔══╝
           ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝     ██║   ██║██║█████╗  ██║ █╗ ██║██████╔╝██║   ██║   ██║   
           ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗     ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║██╔══██╗██║   ██║   ██║   
           ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗     ╚████╔╝ ██║███████╗╚███╔███╔╝██████╔╝╚██████╔╝   ██║   
           ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝      ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═════╝  ╚═════╝    ╚═╝   \n
        """
        for l in msg:
            print(l, end="")
        print(Fore.RESET)

    except KeyboardInterrupt:
        sys.exit()

class TikTok:
    def __init__(self):
        self.added = 0
        self.lock = threading.Lock()

        try:
            self.amount = int(input('> Enter how many views you want to be sent: '))
        except ValueError:
            self.close('Integer expected.')

        try:
            self.video_id = input('> TikTok Video URL: ').split('/')[5]
        except IndexError:
            self.close(
                'Invalid TikTok URL format.\nFormat expected: https://www.tiktok.com/@username/vide'
                'o/1234567891234567891'
            )
        else:
            if not self.video_id.isdigit():
                self.close(
                    'Invalid TikTok URL format.\nFormat expected: https://www.tiktok.com/@username/'
                    'video/1234567891234567891'
                )
            else:
                print()

    def close(self, message):
        print(f'\n{message}')
        os.system('title TikTok Viewbotter By Tqkn - Restart required')
        os.system('pause >NUL')
        os.system('title TikTok Viewbotter By Tqkn - Exiting...')
        sleep(3)
        os._exit(0)  

    def counter(self):
        self.added += 1


    def bot(self):
        print(Fore.LIGHTMAGENTA_EX, f"{self.added} Views have been sent!")
        self.counter()

    def update_title(self):
        # Avoid ZeroDivisionError
        while self.added == 0:
            sleep(0.2)

        while self.added < self.amount:
            # Elapsed Time / Added * Remaining
            time_remaining = strftime(
                '%H:%M:%S', gmtime(
                    (time() - self.start_time) / self.added * (self.amount - self.added)
                )
            )
            os.system(
                f'title TikTok Viewbotter By Tqkn - Added: {self.added}/{self.amount} '
                f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
                f'{threading.active_count()} ^| Time Remaining: {time_remaining}'
            )
            sleep(0.2)
        os.system(
            f'title TikTok Viewbotter By Tqkn - Added: {self.added}/{self.amount} '
            f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
            f'{threading.active_count()} ^| Time Remaining: 00:00:00'
        )

    def start(self):
        self.start_time = time()
        threading.Thread(target=self.update_title).start()

        for _ in range(self.amount):
            if self.added % 2 == 0:
                sleep(0.01)
            else:
                pass
            while True:
                if threading.active_count() <= 300:
                    threading.Thread(target=self.bot).start()
                    break
                
        os.system('pause >NUL')
        os.system('title TikTok Viewbotter By Tqkn - Closing...')
        sleep(3)

            

if __name__ == "__main__":
    os.system('cls && title TikTok Viewbotter By Tqkn')
    logo()
    main = TikTok()
    main.start()