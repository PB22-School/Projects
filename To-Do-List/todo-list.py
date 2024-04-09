import pickle
import os
import datetime

class ToDo:
    def __init__(self, subject, description, dueDate, dueTime = -1):
        self.subject = subject
        self.description = description
        self.dueDate = dueDate
        self.dueTime = dueTime
    def str(self):
        return self.subject

def load_data():

    if not 'todo.pickle' in os.listdir():
        file = open('todo.pickle','wb')
        pickle.dump([],file)
        file.close()
        return []

    with open('todo.pickle','rb') as f:
        todoList = pickle.load(f)
    return todoList

def save_data(data):
    with open('todo.pickle','wb') as f:
        pickle.dump(data,f)

def add_data(data, loadedData):
    loadedData.append(data)
    save_data(loadedData)

def print_data(toDo):

    if not toDo:
        print("\nYou've completed all your tasks!\n")
        return

    lines = []

    subject_len = len("Subject") + 1

    subject_space = len(max(toDo,key=lambda x: len(x.subject)).subject)

    subject_space = max(subject_space, subject_len)

    for item in toDo:
        lines.append(f" | {item.subject} {' ' * (subject_space - len(item.subject))}| {item.dueDate.date()} | ")
        if len(item.subject) > subject_space:
            subject_space = len(item.subject)

    line = f" | Subject {' ' * (subject_space - subject_len)} | Due Date   | "

    print('\nYour To-Do List:\n\n ' + '-' * (len(line) - 2))

    print(line)

    print(' ' + '-' * (len(line) - 2))

    print("\n".join(lines))

    print(' ' + '-' * (len(line) - 2) + '\n')

def check_not_in(data, array):

    for i in range(len(array)):
        if array[i].subject == data.replace(' ','-'):
            return i
    
    print(f"specified subject {data} not found.")
    return -1


while True:

    toDo = load_data()

    print_data(toDo)

    command = input("enter command: ").replace(' ','~',1).split('~')

    match command[0]:
        case 'help':
            print("\nUse '-a' to add an item to your list.\nUse '-e {subject}' to edit an item in your list.\nUse '-c {subject}' to clear a certain item (don't specify a subject to delete all items).\nUse '-t {subject}' to see how much time is left for an item.\nUse '-q to quit'.")

            input("\nReturn: ")

        case '-a':

            subject = input("subject: ").replace(' ','-')
            description = input("description: ")
            dueDate_raw = input('due date (yyyy-mm-dd) or (mm-dd): ')
            if dueDate_raw.count('-') == 1:
                dueDate_raw = f'{datetime.datetime.now().date().year}-{dueDate_raw}'
            dueTime_raw = input("due time (hh:mm): ")

            try:
                dueDate = datetime.datetime.fromisoformat(dueDate_raw)
            except Exception as e:
                print(e)
                print(f"date {dueDate_raw} not entered correctly.")
                continue

            if dueTime_raw:
                try:
                    dueTime = datetime.time.fromisoformat(dueTime_raw)
                except:
                    print(f"time {dueTime_raw} not entered correctly.")
                    continue
            else:
                dueTime = -1

            newItem = ToDo(subject,description,dueDate,dueTime)
            add_data(newItem,load_data())

        case '-e':

            if len(command) == 1:
                print("no item specified.")
                continue

            if (element_index := check_not_in(command[1], toDo)) == -1:
                continue

            change = input("which attribute would you like to change? (0 : subject, 1 : description, 2 : due date, 3 : due time): ")

            match change:
                case '0':
                    toDo[element_index].subject = input('subject: ').replace(' ','-')
                case '1':
                    toDo[element_index].description = input('description: ')
                case '2':
                    raw = input('due date (yyyy-mm-dd) or (mm-dd): ')
                    if raw.count('-') == 1:
                        raw = f'{datetime.datetime.now().date().year}-{raw}'
                    try:
                        toDo[element_index].dueDate = raw
                    except:
                        print(f"date {raw} not entered correctly.")
                case '3':
                    raw = input('due time (hh:mm): ')
                    if raw:
                        try:
                            toDo[element_index].dueTime = raw
                        except:
                            print(f"time {raw} not entered correctly.")
                    else:
                        toDo[element_index].dueTime = -1
            
            save_data(toDo)

        case '-c':

            if len(command) == 1:
                if 'y' == input('this command will clear everything, do you want to proceed? (y/n) : '):
                    save_data([])
                    continue

            if (element_index := check_not_in(command[1], toDo)) == -1:
                continue

            print(f'\nYou completed {toDo[element_index].subject}!')

            toDo.pop(element_index)

            save_data(toDo)

        case '-t':

            if len(command) == 1:
                print("no item specified.")
                continue
            
            if (element_index := check_not_in(command[1], toDo)) == -1:
                continue

            now = datetime.datetime.now()

            line = f"\nthere is: {(toDo[element_index].dueDate.date() - now.date()).days} day(s)"

            if toDo[element_index].dueTime == -1:
                print(line + ' left.\n')

                input("Return: ")
                continue

            time_now = now.hour * 60 + now.minute

            time_then = toDo[element_index].dueTime.hour * 60 + toDo[element_index].dueTime.minute

            delta_time = time_then - time_now
            d_hour = abs(delta_time // 60)
            d_minute = delta_time % 60
            
            line += f', {d_hour} hours and {d_minute} minutes left.\n'

            print(line)

            input("\n\nReturn: ")

        case '-d':
            if len(command) == 1:
                print("no item specified.")
                continue

            if (element_index := check_not_in(command[1], toDo)) == -1:
                continue

            line = '\n' + toDo[element_index].subject + f' ({toDo[element_index].dueDate.date()})'

            if toDo[element_index].dueTime != -1:
                line += f' ({toDo[element_index].dueTime})'

            print(line + f':\n\n{toDo[element_index].description}\n')

            input("Return: ")

        case '-q':
            quit()

        case _:
            print("\nto see a list of available commands, use 'help'.")