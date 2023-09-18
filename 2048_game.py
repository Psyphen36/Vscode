import Logic

def display_mat(mat):
    for v in mat:
        print(" ".join(str(x) for x in v))

if __name__ == '__main__':

    mat = Logic.start_game()

    display_mat(mat)    

    while True:
        x = input('Enter your key: ').lower()

        if x == 'w':
            mat, flag = Logic.move_up(mat)

            status = Logic.get_current_state(mat)
            print(status)

            if status == 'GAME NOT OVER':
                Logic.add_new_2(mat)
            else:
                print('test1')
                break
        elif x == 'a':
            mat, flag = Logic.move_left(mat)

            status = Logic.get_current_state(mat)
            print(status)

            if status == 'GAME NOT OVER':
                Logic.add_new_2(mat)
            else:
                print('test2')
                break
        elif x == 's':
            mat, flag = Logic.move_down(mat)

            status = Logic.get_current_state(mat)
            print(status)

            if status == 'GAME NOT OVER':
                Logic.add_new_2(mat)
            else:
                print('test3')
                break
        elif x == 'd':
            mat, flag = Logic.move_right(mat)

            status = Logic.get_current_state(mat)
            print(status)

            if status == 'GAME NOT OVER':
                Logic.add_new_2(mat)
            else:
                print('test4')
                break
        else:
            print('Invalid Key Pressed!!')

        display_mat(mat)
        



