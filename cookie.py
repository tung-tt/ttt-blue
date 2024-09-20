from time import sleep
# Cookie Program
cookies_amount = 0

def cookie_start():
    global cookies_amount
    while cookies_amount < 5:
        sleep(1)
        print(f'You have {cookies_amount} cookies.')
        cookies_amount += 1

# Main Loop
while True:
    start = input("Cookies, start?: ").lower()
    if start == "yes" or start =="go":
        break
    continue

cookie_start()