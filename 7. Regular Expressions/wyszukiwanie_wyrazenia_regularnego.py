import re, os

#phone number regex
phoneNumRegex = re.compile(r'''
(\+\d{2}\s?)?
(\d{3})
(\s|-|\.)?
(\d{3})
(\s|-|\.)?
(\d{3})
''', re.VERBOSE | re.DOTALL)

#e-mail regex
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.I | re.VERBOSE | re.DOTALL)

matches = []
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for osFilename in filenames:
        _Filename, _Extension = os.path.splitext(osFilename)
        if _Extension == '.txt':
            os.chdir(dirpath)
            with open(osFilename, encoding='utf-8') as file:
                fileContent = file.read()
                for groups in phoneNumRegex.findall(fileContent):
                    phoneNum = ' '.join([groups[0], groups[1], groups[3], groups[5]])
                    matches.append(phoneNum)
                for groups in emailRegex.findall(fileContent):
                    matches.append(groups[0])
                    for match in matches:
                        print(osFilename, match)