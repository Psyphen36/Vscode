
def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):

            if list1[i] == list2[j]:
                char = list1[i]

                list1.remove(char)
                list2.remove(char)

                list3 = list1 + ['*'] + list2

                return [list3, True]

    list3 = list1 + ['*'] + list2
    return [list3, False]


if __name__ == '__main__':
    p1 = input('Enter player1 name: ')
    p1. lower()

    p1.replace(" ", "")

    p1_list = list(p1)

    print(p1_list)

    p2 = input('Enter player2 name: ')

    p2.lower()

    p2.replace(" ", "")

    p2_list = list(p2)

    print(p2_list)
    proceed = True

    while proceed:
        return_list = remove_match_char(p1_list, p2_list)

        concat_value = return_list[0]

        proceed = return_list[1]

        asterisk_char = concat_value.index('*')

        p1_list = concat_value[:asterisk_char]

        p2_list = concat_value[asterisk_char+1:]

    count = len(p1_list) + len(p2_list)

    result = ['Friend', 'Lover', 'Affection', 'Marriage' ,'Enemy', 'Siblings']

    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[:split_index]

            result = right + left
        else:
            result = result[:len(result) - 1]

    print('Relationship Status:',result[0])






