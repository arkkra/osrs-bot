
from scripts.high_alch import HighAlch
from scripts.range_nmz import RangeNMZ

def select_script(scripts: list):
    print('Which bot are you running?')
    for i, s in enumerate(scripts):
        print(str(i + 1) + '. ' + s['name'])
    
    selected = input()
    return selected

if __name__ == '__main__':
    print('Shitter Bot - v1')
    print('---------------------------------')

    scripts = [
        {
            'name':'High Alch',
            'script': HighAlch
        },
        {
            'name': 'Range NMZ',
            'script': RangeNMZ
        }
    ]

    selected = int(select_script(scripts))
    if selected > len(scripts) and selected <= 0:
        exit()

    script = scripts[selected - 1]['script']()
    script.run()



   



