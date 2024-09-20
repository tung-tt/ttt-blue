from time import sleep
# Cookie Program
cookies_amount = 0

def cookie_start(cookies_goal):
    global cookies_amount
    while cookies_amount <= cookies_goal:
        sleep(1)
        print(f'You now have {cookies_amount} cookies.')
        cookies_amount += 1
    print('--🍪 COOKIES DISPENSED--')

# Main Loop
while True:
    print('-- WELCOME TO 🍪 --')
    start = input("Want some cookies?: ").lower()
    if start == "yes" or start =="go":
        cookies_goal = int(input("How many cookies do you want?: "))
        print('--🍪 INITIALIZED--')
        cookie_start(cookies_goal)
        break
    continue

