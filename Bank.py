from queue import Queue
import Account
import Bst

class bank:
  
    def __init__(self):
      self.__q = Queue()
      self.__tree = Bst.bst()
      self.__accounts = []

    def read_file(self, file):
        file = open(file)
        for line in file:
            words = line.split()
            self.__q.put(words)
        file.close()

   
    def execute_file(self):
      while not self.__q.empty():
        words = self.__q.get()
        #open
        #O Minyoung Yoo 1234
        if words[0] == "O":
            key = words[3]
            if len(key) != 4:
              print("ERROR: Invalid account format (CODE: BNK_EXE_O1)")
              return
          
            anode = self.__tree.get(key)
            if anode == None:
              new_acc = Account.account(words[1], words[2], key)
              self.__tree.put(key, new_acc)
              self.__accounts.append(key)

            else:
              print(f"ERROR: Account {key} is already open. Transaction refused. (CODE:BNK_EXE_O2)")
              return

        #Deposit
        #D 10010 542
        elif words[0] == "D":
          key = words[1] #10010
          if len(key) != 5:
            print("ERROR: Invalid account format (CODE: BNK_EXE_D1)")
            return
          if not int(key[4]) in range(0,10): #XXXX0
            print("ERROR: Invalid fund type (CODE: BNK_EXE_D2)")
            return
          if int(words[2]) < 0:
            print("ERROR: cannot deposit negative value (CODE:BNK_EXE_D3)")
            return
            
          #seperate account number and fund index number
          anode = self.__tree.get(key[0:4]) #get account info of 1001
          index = int(key[4])
          money = int(words[2])
          
          #check if the account exists
          #exists in the record 
          if anode != None:
            anode.deposit(index, money)
            self.__tree.put(key[0:4], anode)
          else:
              print(f"ERROR: Account {key[0:4]} does not exist in the server. (CODE: BNK_EXE_D4)")
              return

        #withdraw
        #W 10010 542
        elif words[0] == "W":
          key = words[1] #10010
          if len(key) != 5:
            print("ERROR: Invalid account format (CODE: BNK_EXE_W1)")
            return
          if not int(key[4]) in range(0,10): #XXXX0
            print("ERROR: Invalid fund type (CODE: BNK_EXE_W2)")
            return
          if int(words[2]) < 0:
            print("ERROR: cannot withdraw negative value (CODE:BNK_EXE_W3)")
            return
            
          #seperate account number and fund index number
          anode = self.__tree.get(key[0:4]) #get account info of 1001
          index = int(key[4])
          money = int(words[2])
          
          #check if the account exists
          #exists in the record 
          if anode != None:
            done = anode.withdraw(index, money)
            if done == True:
                self.__tree.put(key[0:4], anode)
            else:
                line = f"W {key} {money} (Failed)"
                anode.put_history(line)
          else:
              print(f"ERROR: Account {key[0:4]} does not exist in the server. (CODE: BNK_EXE_D4)")
              return

        #transfer
        #T 12340 1000 12341
        #T 12340 1000 56780
        elif words[0] == "T":
          from_key = words[1] #12340
          to_key = words[3] #12341
          if len(from_key) != 5 or len(to_key) != 5:
            print("ERROR: Invalid account format (CODE: BNK_EXE_T1)")
            return
          if not int(from_key[4]) in range(0,10) or not int(to_key[4]) in range(0, 10): #XXXX0
            print("ERROR: Invalid fund type (CODE: BNK_EXE_T2)")
            return
          if int(words[2]) < 0:
            print("ERROR: cannot transfer negative value (CODE:BNK_EXE_T3)")
            return

          #seperate account number and fund index number
          from_node = self.__tree.get(from_key[0:4]) #get account info of 1234
          from_index = int(from_key[4])
          to_node = self.__tree.get(to_key[0:4])
          to_index = int(to_key[4])
          money = int(words[2])

          #check if the account exists
          #exists in the record 
          if from_node != None:
              if to_node != None:
                  done = from_node.withdraw(from_index, money)
                  if done == True:
                      to_node.deposit(to_index, money)
                  else:
                      line = f"T {from_node.get_account()}{from_index} {money} {to_node.get_account}{to_index} (Failed.)"
                      from_node.put_history(line)
                  self.__tree.put(from_key[0:4], from_node)
                  self.__tree.put(to_key[0:4], to_node)
              else:
                  print(f"ERROR: Account {to_key[0:4]} not found. Transferal refused. (CODE: BNK_EXE_T4)")
          else:
              print(f"ERROR: Account {from_key[0:4]} not found. Transferal refused. (CODE: BNK_EXE_T5)")
              return

        #H 1234
        #H 12342 
        elif words[0] == "H":
          key = words[1]
          anode = self.__tree.get(key[0:4]) #get account info of 1234
          index = len(key)
          if anode == None:
            print(f"ERROR: Account {key[0:4]} does not exist in the server. (CODE: BNK_EXE_H1)")
            return          
          if index == 4:
            anode.print_trans_history()
          elif index == 5:
            if index < 0 or index > 9:
              print("ERROR: Invalid fund type (CODE: BNK_EXE_H2)")
              return
            anode.print_single_trans(index)
          else:
            print("ERORR: Invalid Transaction (CODE: BNK_EXE)")
            return

    def summary(self):
        for key in self.__accounts:
            self.__tree.get(key).print_final_balances()
           