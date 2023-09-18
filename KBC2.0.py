questions = [
['What is the brain of a computer','MotherBoard','CPU','SSD','RAM',2],

['What is the full form of OOPs','Object Oriented Programming','Organized Operation protocols',
    'Optical Operator Programming','Operator Order Protocol',1],

['What lets to do many things, like write book reports and stories? ','Duct Tape',
    'Email','Application Programs','Antivirus Software',3],

['What lets the computers hardware and software work together?','Monitor',
    'Operating System','Central Processing Unit(CPU)','Computer Viruses',2],

['What tells the hardware what to do and how to do it?','Software',
    'Hardware','Hard Drive(HDD)','Central Processing Unit(CPU)',1],

['What can make your computer "sick"?','Antivirus Software','Computer Viruses',
    'Influenza','Hot Temperatures',2],

['What let you explore the internet to find information,Pictures,videos,and webpages?',
    'Email','Internet Browser','Monitor','Firewall',2],

['Which of the following is a word processing program?','Microsoft Excel',
    'Google Slides','YouTube','Microsoft Word',4],

['If you use social media,you should use the following:','Well-lit photos',
    'Location Detection','High Privacy Settings','An Incognito Browser',3],
    
['What should you do if someone you know is being cyberbullied?','Fight the bully online',
    'Report it','Join the bully','Ignore it',2],

['When you are online, you should never share','Articles',
    'Comments','Ideas','Personal Information',4],

['Who can you share your password with?','Your Best Friend',
    'Your Parents','Your Sister','A Stranger',2],

['What a teenager need from their parents or teacher before they download a file or app?',
    'Permission','A signed consent form','Their password','Nothing',1],

['Which part of a computer takes the text and pictures on your screen and prints them onto paper?',
    'Monitor','Central Processing Unit(CPU)','Computer Case','Printer',4],

['What is the full form of ISRO?','International Space Research Organization',
    'Iraq Space Research Organization','Israel Space Research Organization','Indian Space Research Organization',4]
]
levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print('-'*50)
    print(f'Question for Rs. {levels[i]} ')
    print(question[0])
    print(f'1. {question[1]}            2. {question[2]}')
    print(f'3. {question[3]}            4. {question[4]}')
    reply = int(input('Enter (1-4) to choose: '))
    if reply == question[-1]:
        print(f'Your answer is correct.You won Rs. {levels[i]}')
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print('Wrong answer!!')
        break
print(f'The money you take home is {money}')

