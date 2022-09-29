receiver_name = input('Введите имя получателя: ')
receiver_last_name = input('Введите фамилию получателя: ')
sender_name = input('Введите имя отправителя: ')
sender_surname = input('Введите фамилию отправителя: ')
sender_position = input('Введите должность отправителя: ')


def input_phrase(receiver_name, receiver_last_name, sender_name, sender_surname, sender_position):
    message = f''' Dear {receiver_name} {receiver_last_name},\n   
 We are lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum in faucibus massa. 
Suspendisse at ex varius, porttitor eros sit amet, sagittis nibh. In vel est a tortor tempor luctus 
a. \n ________________ \n {sender_name} {sender_surname} \n {sender_position}'''
    return message


x = input_phrase(receiver_name, receiver_last_name, sender_name, sender_surname, sender_position)
print(x)