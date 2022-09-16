# def run_alch():
#     print("Starting auto clicker")
#     time.sleep(3)

#     while True:
#         mouse.press(Button.left)
#         randomTime = random.randint(9, 27)
#         time.sleep(randomTime / 100)
#         mouse.release(Button.left)
#         randomTime = random.randint(133, 166)
#         time.sleep(randomTime / 100)

# def run_bracelet():
#     print("Starting bracelets")
#     time.sleep(3)

#     keyboard.press(Key.up)
#     time.sleep(1)
#     keyboard.release(Key.up)
#     time.sleep(.5)
#     mouse.scroll(0, 35)
#     # while True:

# def run_iron_mine():
#     def mine():
#         click(x=930, y=450, dx=12, dy=11)
#         random_sleep(4, fast=False)
#         i = 0
#         while i < 28:
#             click(x=742, y=440, dx=14, dy=16)
#             random_sleep(1.85, tick=10)
#             i+=1
#             click(x=715, y=465, dx=16, dy= 16)
#             random_sleep(1.85, tick=10)
#             i+=1
#             click(x=742, y=495, dx=14, dy= 16)
#             random_sleep(1.85, tick=10)
#             i+=1

#     def bank():
#         click(x=516, y=481, dx=24, dy=26)
#         random_sleep(5)
#         click(x=694, y=493, dx=25, dy=25)
#         random_sleep(1.6, fast=False)
#         click(x=830, y=268, dx=15, dy=15)


#     print("Starting iron mine")
#     time.sleep(3)

#     keyboard.press(Key.up)
#     time.sleep(1)
#     keyboard.release(Key.up)
#     time.sleep(1)

#     mouse.scroll(0, 40)
#     time.sleep(1)
    
    
#     click(x=745, y=410, dx=20, dy=30)
#     random_sleep(2)
#     click(x=830, y=268, dx=15, dy=15)
#     random_sleep(1.6)
#     while True:
#         mine()
#         bank()



def select_script(scripts: list):
    print('Which bot are you running?')
    for i, s in enumerate(scripts):
        print(str(i + 1) + '. ' + s)
    
    selected = input()
    return selected

if __name__ == '__main__':
    print('Shitter Bot - v1')
    print('---------------------------------')

    scripts = ['High Alch', 'Mine Iron', 'Jewlery']
    selected = get_script(scripts)
    print(selected)

   



