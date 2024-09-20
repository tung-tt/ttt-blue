from time import sleep
# Imported sleep for 1 second delays
# 🍪 Dispenser Program
cookies_amount = 0
print('-- WELCOME TO 🍪 --')
sleep(0.5)
# Cookies Incremental Functon
def cookie_start(cookies_goal):
    # Access cookies_amount from outside
    global cookies_amount
    while cookies_amount <= cookies_goal:
        sleep(1)
        print(f'You now have {cookies_amount} cookies.')
        cookies_amount += 1
    print('--🍪 COOKIES DISPENSED--')

# Main Loop
while True:
    start = input("Want some cookies?: ").lower()
    # Switch case instead of if statements, checks corresponding strings from start input
    match start:
        case 'yes':
            cookies_goal = int(input("How many cookies do you want?: "))
            print('--🍪 INITIALIZED--')
            # Calls cookies_start function with cookies_goal as limit
            cookie_start(cookies_goal)
        case 'stop':
            print("Fine, get outta here")
            sleep(0.5)
            print('--🍪 ENDING--')
            break
        case _:
            print("Oh, ok... but")
    continue

sleep(0.5)
print('--🍪 TERMINATED--')