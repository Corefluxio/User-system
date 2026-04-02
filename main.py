class UserSystem:
    
    def __init__(self):
       self.database = {}

    def load_from_file(self):
      try:
        with open("users.txt", "r") as f:
           for line in f:
               if not line.strip():
                 continue
               username, password = line.strip().split(":")
               self.database[username] = password
      except FileNotFoundError:
         pass
              
    def register(self,username,password):
      if username not in self.database:
        self.database[username] = password
        return "User created"
      else:
         return "User already exists"

    def login(self,username,password):
       if username in self.database:
           if self.database[username] == password:
             return "Success"
           else:
            return "Wrong password"
       else:
         return "User not found"
       
    def delete_user(self,username):
       if username in self.database:
          del self.database[username]
          return "User deleted"
       else:
          return "User not found"
    
    def save_to_file(self):
       with open("users.txt", "w") as f:
          for username, password in self.database.items(): 
             f.write(f'{username}:{password}\n')
    
    def __str__(self):
      if len(self.database) == 0:
        return "No users in system"
      else:
       return "Users: " + ', '.join(self.database.keys())
   

system = UserSystem()
system.load_from_file()

while True:
   print("1 - Register")
   print("2 - Login")
   print("3 - Delete")
   print("4 - Show users")
   print("5 - Exit")

   choice = input('Choose: ')

   if choice == "1":
      username = input('Enter username: ')
      password = input('Enter password: ')
      print(system.register(username,password))
      system.save_to_file()
   
   elif choice == "2":
      username = input('Enter username: ')
      password = input('Enter password: ')
      print(system.login(username,password))
   
   elif choice == "3":
      username = input("Enter username to delete: ")
      print(system.delete_user(username))
      system.save_to_file()
   
   elif choice == "4":
      print(system)
   
   elif choice == "5":
      print('Goodbye')
      break
   
   else:
      print('Wrong choice')
  

