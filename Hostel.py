
id = '23GH4KJH5T'
import random
secret_word = random.randint(10000000, 100000000)
print('Sunshine hostel\nlocation- kotei\n4 in a room - 2200 cedis rooms available- 1,2,3,4,5\n3 in a room - 2400 cedis rooms available- 1,2,3,4,5\n2 in a room - 2600 cedis rooms available- 1,2,3,4,5\n1 in a room - 2800 cedis rooms available- 1,2,3,4,5')
print('Amen hostel\nlocation- Ayeduase\n4 in a room - 2500 cedis rooms available- 1,2,3,4,5\n3 in a room - 2700 cedis rooms available- 1,2,3,4,5\n2 in a room - 2900 cedis rooms available- 1,2,3,4,5\n1 in a room - 3100 cedis rooms available- 1,2,3,4,5')
print('Evandy hostel\nlocation- Bomso\n4 in a room - 2800 cedis rooms available- 1,2,3,4,5\n3 in a room - 3000 cedis rooms available- 1,2,3,4,5\n2 in a room - 3200 cedis rooms available- 1,2,3,4,5\n1 in a room - 3400 cedis rooms available- 1,2,3,4,5')
print('Franco hostel\nlocation- Ayeduase\n4 in a room - 3100 cedis rooms available- 1,2,3,4,5\n3 in a room - 3300 cedis rooms available- 1,2,3,4,5\n2 in a room - 3500 cedis rooms available- 1,2,3,4,5\n1 in a room - 3700 cedis rooms available- 1,2,3,4,5')


print('Answer the following questions if you want to book a room')
name = input('Write your name in full:')
program = input('What program are you reading?:')
print('First year,Second year,Third year,Fourth year,Fifth year,sixth year')
year = input('Which year are you?:')
hostel = input('Which hostel do you want?:')
room = input('How many in a room ? 4 , 3 ,2 ,1:')
room_number = input('Which room do you want?:')
fee = input('How much are you paying now?:')

print('Room booked sueccesfully! details of occupant:\nName:'+name+'\nYear:'+year+'\nProgram:'+program+'\nroom number: '+room_number+'\nroom type: '+room+' in a room\nYou are to pay an amount of  '+fee+' and 30 cedis for charges\nFees are to be paid within 48 hours at GCB bank\nYour unique id is '+str(secret_word)+'\nPrint this page and present it at the bank for payment')






