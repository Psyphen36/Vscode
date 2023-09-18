import demoji

# text = '😀 🥰 🤐 🤑'
swear = 'Fuck you 🖕'

interpret = demoji.findall(swear)
print(interpret)

