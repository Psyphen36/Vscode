name = input('Enter your name: ')
name2 = input('Enter your friends name: ')
print('-'*60)
print(f'Hello {name} welcome to our |choose your own story| game!!')
permit = input('Press "any key" to start the game or "q" to quit: ').lower()
print('-'*60)
ques = ''
while True:
    if permit == 'q':
        break
    print(f'There is a wonderful island named Laugh Tale where a person {name} is living who is very good at programming and love to watch anime one day he watch one piece\n anime and got hooked up with it and when he watched its last episode it makes him cry after crying a lot he got tired and get sleepy while in a sleep het had a \ndream where he is doing an adventure like luffy in one piece when he woke up from his dream he got an idea of doing an adventure by himself.')

    q1= input('do you choose to go to an adventure or just go to play a video game ("adventure"/"game"): ').lower()
    print()
    if q1 == 'adventure':
        print(f'He think it as a good idea he is trying to plan what is he need for going to an adventure while he is thinking his friend {name2} came to his house and than he \ntold his friend about going to an adventure and ask him to go with him')
#Todo: think of some story for creating adventure portion. 

    elif q1 == 'game':
        print(f'But he think in his mind who is going an adventure after watching an anime this is a stupid idea after thinking of that his friend came to his house and both of them playing video game in a playstation, i.e("jump force") and {name} is choosing his one of the favorite character luffy and zoro and then realize he got an idea of going to an adventure he told the idea with his friend. ')
        q2 = input(f'What would you choose after listening to {name}\'s  idea (agree/disagree): ').lower()
        print()
        if q2 == 'agree': 
            print(f'He agreed with {name}\'s thought and both ready to go to and adventure the thought of going by boat and but didn\'t told their parents that they are going to an adventure after some time passed they create a little boat by himself and after creating that they now ready to go to an adventure after one week they are ready they pack all the stuff they needed and just leave the are by boat they choose the isolated area so that no one can see them they successfully cross the area without seeing by someone after going somedays passed and they ate all of the food supply and then they got lost and the middle of the ocean and died from starving.')
            print('Going alone without any captain or navigator is a bad idea . You lost!!')
            break
        elif q2 == 'disagree':
            print(f'He disagree with {name}\'s thought and convince him to not go to an adventure after playing sometime they are going outside for a walk and talk about anime,programming and other chit chat and suddenly his friend {name2} tell him about a haunted place where if someone goes never came back and then suddenly {name} got excited and ask his friend to go with him to that place ')
            q3 = input('What would you choose as his friend ("go"/"don\'t go"): ').lower()
            print()
            if q3 == 'go':
                print(f'his friend {name2} also wanted to go with him so both of them go to their houses and pack the bag to go to the haunted house to explore it. When both of them get to that place {name2} get chills and a bad feeling and he told {name} that he got a bad feeling about it so let\'s head back to home don\'t go there.')
                q = input('agree and go back to home | don\'t agree ("agree/don\'t agree")').lower()
                print()
                if q == 'agree':
                    print(f'After hearing that his friend scared he also think that this is a bad idea to go that place so they came back home and then next day they hear from news that "the reason behind people get killed after going to that haunted house finally revealed there is nothing haunted there are a group of criminals who just theft, and murder people yesterday a group of police go to that house for checking why this is happening and find out there are a bunch of murderers our four police officers shot from those murderers 1 dead two injured but we caught the murderers all of them are arrested" after hearing that {name} called {name2} and tell him what is going on to that haunted house and they just got chills what if we go there and get killed by those and the relief of not going inside of that haunted house.')
                    print('Good decision of not going to that house. Congratulations!!')
                    break
                elif q == "don't agree":
                    print(f'After hearing that his friend scared he try to calm him and told there is nothing to fear we have precautions like stick,teaser sor don\'t be afraid after hearing that {name2} calm down and both of them jump the fence and go to the haunted house and forget to observe the house from outside {name} tried to open the front gate but its locked then {name2} find the window open and both of them got inside after getting inside they feel someone other than him in this house but both of them think that it\'s hallucination from fear so they tried to search the house the lights are turned off so they use torch suddenly to person from their back grab both of them and they scared and scream at the same time then 4-6 person came from inside and someone turned the lights on and then {name2} ask questions from those people he "said who are you" one of them pulled the gun from his pocket and point in his head then and said that we are criminals and push the trigger and those two were dead.') 
                    print('Bad choice. You lost both died!!')
                    break

            elif q3 == "don't go":
                print(f'{name2} told him to not go at that place but {name} is trying to convince him to go with him but he pissed of and leave.')
                q4 = input('Are you still going after your friend leaves ("yes/no")').lower()
                print()
                if q4 == 'yes':
                    print(f'After his friend leave\'s he got pissed too and go alone because he knew the location he just go his home pack some stuff and go to that horror and dangerous place when he finally get the place he observes the whole place from outside of the fence gate he saw big and spooky villa and a graveyard just at the right side off the villa and got little nervous but he still trying to go and check it from inside when he is going to inside he hears some voice and scared but he didn\'t run back he still jump from the fence and go inside from the window because front gate didn\'t open and after going inside suddenly someone grab him from his back he scared and scream than the villas light turned on and he saw 5-6 men in front of himself and he ask who are you all and they told him they are criminals who theft and kills people and someone from their gang pulled his pistol and shot him in his head and {name} is dead.')
                    print('Bad choice you are dead.You lost!!')
                    break
                elif q4 == 'no':
                    print(f'after his friend\'s leave he realize that is a bad idea of going such a dangerous place and he go to {name2}\'s place to say sorry to him after going to his place he ask his mom "aunty where is {name2}" and his mom said he is at your place he didn\'t came after that.')
                    q5 = input('Go back to your home | call him ("a/b")').lower()
                    print()
                    if q5 == 'a':
                        print(f'After hearing from his mom that he never came back to his house {name} go back to his house and use his mobile phone and send {name2} a message that he is sorry for forcing him to go to that place but his internet is off and after that he is going to study later on that day he got his friend mom\'s call his mom told him his son didn\'t came back.')
                        q6 = input('you told his mom to not to panic and hang the phone and then go after study| you told his mom to not to panic i am coming at your place ("a/b")').lower()
                        if q6 == 'a':
                            print(f'After talking to his mom he told her to not to panic and hung up the phone and do nothing next day his friend broke up his friendship with him and told him i don\'t need a friend who do nothing after hearing that his friend missing and told him that he is trying to test {name} that he is really is friend or not and spoiler alert!! his is not. ')
                            print('You didn\'t help your friend.You lost the game!!')
                            break
                        elif q6 == 'b':
                            print(f'After hearing that he tried to calm her and told her to not to panic i am coming your house. After saying that he go to his friends house and ask him the whole situation and find out his friend never came back home after pissed of and leaving him. So he stand up for leaving and finding his friend but suddenly someone from his back closed his both eyes with his back and said surprise!! and then {name} realize that his friend is trying to test him that. If i am missing at night would my friend came to search me or not so he just planned it as a possibility if my friend came to my house after i leave him i told my mom to not to say that i\'m in my room and switched my phone off.')
                            print('This is one of the ending.Congratulations!!')
                            break
                        else:
                            print('Invalid Syntax!!')
                    elif q5 == 'b':
                        pass
                    else:
                        print('Invalid Syntax!!')
                else:
                    print('Invalid Syntax!!')
            else:
                print('Invalid syntax!!')
        else:
            print('Invalid syntax!!')
    else:
        print('Invalid syntax!!')


