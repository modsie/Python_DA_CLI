'''
Create a list of at least 5 states and capital.
From user option 1-4
1. Read - display all stats and capital
2. Create - User can add a state and it capital
3. Update - User can edit a particular state and capital
4. Delete - User can delete a particular state and capital
'''
    
state1 = { 'State': 'Oyo', 'Capital': 'Ibadan'}
state2 = { 'State': 'Lagos', 'Capital': 'Ikeja'}
state3 = { 'State': 'Ogun', 'Capital': 'Abeokuta'}
state4 = { 'State': 'Osun', 'Capital': 'Osogbo'}
state5 = { 'State': 'Ekiti', 'Capital': 'Ado-Ekiti'}

stateCapital_list = [state1, state2, state3, state4, state5]

def stateCapital():
    print('''
    Enter 1 to view list of states and capital
    Enter 2 to add a state and capital
    Enter 3 to edit a state of you choice
    Enter 4 to delete a particular state and it capital
    Enter 5 to close the program
    ''')
    
    user_input = input('Enter your option: ')

    stateList = []
    for state_capital in stateCapital_list:
        state = f'{state_capital["State"]} : {state_capital["Capital"]}'
        stateList.append(state)

    stateList.sort()

    def read():
        
        num = 1
        for eachState in stateCapital_list:
            print(f'{num}. {eachState}')
            num += 1

    if user_input == '1':
        print('View list of states and capital\n')
        read()

        stateCapital()


    elif user_input == '2':
        print('Add a state and capital\n')
        getState = input('Enter state: ')
        getCapital = input('Enter capital: ')
        state_capital = {
                'State' : getState,
                'Capital' : getCapital
            }
        
        stateCapital_list.append(state_capital)

        read()

        stateCapital()

    elif user_input == '3':
        print('Edit a state of you choice\n')
        num = 1
        for state_capital in stateCapital_list:
            state = f'{state_capital["State"]} : {state_capital["Capital"]}'
            print(f'{num}. {state}')
            num += 1
        # read()
        index = input('\nEnter the number of the state: ')
        
        indexInt = int(index)
        print(stateCapital_list[indexInt-1])

        stateCapital_list[indexInt-1]['State'] = input('Enter new state')
        stateCapital_list[indexInt-1]['Capital'] = input('Enter new capital')
        
        num = 1
        for state_capital in stateCapital_list:
            state = f'{state_capital["State"]} : {state_capital["Capital"]}'
            print(f'{num}. {state}')
            num += 1

        # try:
        # except:
        #     print('Error with your input')

        stateCapital()

    elif user_input == '4':
        print('Delete a particular state and it capital')
        
        num = 1
        for state_capital in stateCapital_list:
            state = f'{state_capital["State"]} : {state_capital["Capital"]}'
            print(f'{num}. {state}')
            num += 1
        # read()
        index = input('\nEnter the number of the state to delete: ')
        indexInt = int(index)
        print(stateCapital_list[indexInt-1])
        item = stateCapital_list[indexInt-1]
        stateCapital_list.remove(item)
        
        
        num = 1
        for state_capital in stateCapital_list:
            state = f'{state_capital["State"]} : {state_capital["Capital"]}'
            print(f'{num}. {state}')
            num += 1

        stateCapital()

    elif user_input == '5':
        print('Thank you for using our software')

    else:
        print('Input invalid')
        stateCapital()
        
stateCapital()
