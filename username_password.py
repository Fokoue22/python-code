# USERNAME and PASSWORD 

username_password = {                # place my username and password in a dictionary called username_password
  "doncfack" : "fack678", 
  "ngueffealex" : "ngueffe999",
  "ekondoamstrong" : "strong3456", 
  "monkampierre" : "monkam5467", 
  "fokouethomas" : "fokoue567", 
  "tabesandra" : "tabe009",
  "tabilucas" : "tabi1900",
  }

guess_username = ''  # initializing the username
guess_password = ''  # initializing the username
count = 0
limite = 5

while count < limite: 
      count += 1
      guess_username = input('Enter your username: ') # ask the user to prompt his username and password
      guess_password = input('Enter your password: ')

      if guess_username in username_password and username_password[guess_username] == guess_password:
            print("\nYOU HAVE BEEN GRANTED ACCESS TO YOUR ACCOUNT")   # if our username and password prompt by the user is similar to one in the dictionary print this line                                                             
            break
      
      elif guess_username not in username_password or username_password[guess_username] != guess_password:
            
            if count != limite:
                  print('\nPlease Try Again')  # if it's not the same with what we have in our dictionary ask him to try again 
       
            else:
                  print("\n!!!!ACCOUNT LOCK PLEASE WAIT FOR 48H OR CALLED YOUR ACCOUNT ADMINISTRATOR!!!!") # After 5 successful try if the user doesn’t have the same username and password with what we have in our dictionary print this line
                  break
      else: 
             break