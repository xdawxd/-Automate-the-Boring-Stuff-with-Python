# SpaceFill.py - wypelnia przerwy pomiedzy nazwami plikow np. spam001.txt i spam003.txt
# tak aby byly w poprawniej kolejnosci tzn. spam001.txt ... spam002.txt

def space_fill(path, extension):
    import os
    import re
    import shutil

    filename_pattern = re.compile(r'(.*?)(\d+)(.*?)')

    num_of_files = 0
    zeros = []
    before_part, after_part = [], []
    sources, destinations = [], []

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(extension):
                mo = filename_pattern.search(filename)
                if mo is not None:
                    num_of_files += 1
                    before_part, after_part = mo.group(1), mo.group(3)
                    zeros.append(len([num for num in mo.group(2) if int(num) == 0]))
                    sources.append(os.path.join(dirpath, filename))

    for number in range(1, num_of_files + 1):
        des = before_part + '0' * max(zeros) + str(number) +\
                      after_part + '.' + extension
        destinations.append(os.path.join(path, des))

    for i in range(num_of_files):
        print(f'Zmieniam nazwe pliku z {sources[i]} na {destinations[i]} ...')
        shutil.move(sources[i], destinations[i])

    return '\nGotowe!'

print(space_fill('.', 'txt'))