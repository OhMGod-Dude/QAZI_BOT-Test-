from pricing import totalamunt


print('''Hello, Welcome to QAZI CAFE ☺! My name is QaziBot and I am the supervising bot of QAZI CAFE.''')

#Getting required details from the user

while True:
  user_name = input('\nwhat is your name? ')
  if not user_name :
    print('Please enter your name!')
  else:
    break
while True:
    nic_number = input("\nwhat is your nic number? ")
    if not nic_number:
      print('Please enter your nic number!')
      
    elif user_name != 'Luther Parker' or nic_number == "7897192345":
      print(f'\nWelcome to QAZI CAFE {user_name} ☺ ! ')
    else:
      print(f'\nYou are not Welcomed to QAZI CAFE {user_name} ☺ ! ')
    break
  
menu = ["1. Potato", "2. Coffee" , "3. Tea" , "4. Pasta", "5. Salad"]

price = [50, 30, 20, 60, 40]

for i in price:
  l = 0 
  for k in range[l]:
    l = k 
  print(l)  





print(f"Total price is ${totalamunt(price = 50, tipa = 2.5)}")




      


