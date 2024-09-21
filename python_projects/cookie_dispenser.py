from time import sleep
# Imported sleep for 1 second delays
# 🍪 Dispenser Program
# Variables & Lists
counter = 0
cookies_amount = 0
accept = ['yes', 'sure', 'fine', 'ok', 'cookies']
reject = ['no', 'stop', 'im good']
# Start
print('-- WELCOME TO 🍪 --')
sleep(0.5)
# Cookies Incremental Functon
def cookie_start(cookies_goal):
    # Access cookies_amount from outside
    global cookies_amount
    cookies_copy = cookies_amount
    while cookies_amount <= (cookies_copy + cookies_goal):
        sleep(1)
        print(f'You now have {cookies_amount} cookies.')
        cookies_amount += 1
    print('--🍪 COOKIES DISPENSED--')

# Main Loop
while True:
    match counter >= 1:
        case True:
            start = input("Want some more cookies?: ").lower()
        case _:
            start = input("Want some cookies?: ").lower()
    # Switch case instead of if statements, checks corresponding strings from start input
    if start in accept:
            counter += 1
            cookies_goal = int(input("How many cookies do you want?: "))
            print('--🍪 INITIALIZED--')
            # Calls cookies_start function with cookies_goal as limit
            cookie_start(cookies_goal)
    elif start in reject:
        print("Fine, get outta here")
        sleep(0.5)
        print('--🍪 ENDING--')
        break
    else:
        print("I don't understand, but...")
    continue

sleep(0.5)
print('--🍪 TERMINATED--')