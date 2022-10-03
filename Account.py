class account:

    success = False

    def __init__(self, fname, lname, account):
        self.__first_name = fname
        self.__last_name = lname
        self.__account = account
        self.__funds = {
            0: "Money Market",
            1: "Prime Money Market",
            2: "Long-Term Bond",
            3: "Short-Term Bond",
            4: "500 Index Fund",
            5: "Capital Value Fund",
            6: "Growth Equity Fund",
            7: "Growth Index Fund",
            8: "Value Fund",
            9: "Value Stock Index"
        }
        self.__balance = []
        for j in range(10):
            self.__balance.append(0)

        #double list
        self.__history = [[],[],[],[],[],[],[],[],[],[]]

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_account(self):
        return self.__account

    def get_funds(self):
        return self.__funds

    #D 10010 542
    def deposit(self, fund_index, money):
        self.__balance[fund_index] += money
        line = f"D {self.__account}{fund_index} {money}"
        self.__history[fund_index].append(line)

    #W 10010 342
    def withdraw(self, fund_index, money):
        if self.__balance[fund_index] >= money:
           self.__balance[fund_index] -= money
           line = f"W {self.__account}{fund_index} {money}"
           self.__history[fund_index].append(line)
           return True
        #if there is not enough balance in a fund
        elif fund_index in range(0,4):
            #Money Market
            if fund_index == 0:
                sub = money - self.__balance[0]
                if self.__balance[1] >= sub:
                    self.__balance[0] = 0
                    line = f"W {self.__account}{fund_index} {money-sub}"
                    self.__history[0].append(line)
                    self.__balance[1] -= sub
                    line = f"W {self.__account}{fund_index} {sub}"
                    self.__history[1].append(line)
                    return True
                else:
                    print(f"ERROR: Not enough funds to withdraw {money} from Money Market (CODE: ACC_WTHDW0)")
                    success = False
            #Prime Money Market
            elif fund_index == 1:
                sub = money - self.__balance[1]
                if self.__balance[0] >= sub:
                    self.__balance[1] = 0
                    line = f"W {self.__account}{fund_index} {money-sub}"
                    self.__history[1].append(line)
                    self.__balance[0] -= sub
                    line = f"W {self.__account}{fund_index} {sub}"
                    self.__history[0].append(line)
                    return True
                else:
                    print(f"ERROR: Not enough funds to withdraw {money} from Prime Money Market (CODE: ACC_WTHDW1)")
                    return False
            #Long-Term Bond
            elif fund_index == 2:
                sub = money - self.__balance[2]
                if self.__balance[3] >= sub:
                    self.__balance[2] = 0
                    line = f"W {self.__account}{fund_index} {money-sub}"
                    self.__history[2].append(line)
                    self.__balance[3] -= sub
                    line = f"W {self.__account}{fund_index} {sub}"
                    self.__history[3].append(line)
                    return True
                else:
                    print(f"ERROR: Not enough funds to withdraw {money} from Long-Term Bond (CODE: ACC_WTHDW2)")
                    success = False
            #Short-Term Bond
            elif fund_index == 3:
                sub = money - self.__balance[3]
                if self.__balance[2] >= sub:
                    self.__balance[3] = 0
                    line = f"W {self.__account}{fund_index} {money-sub}"
                    self.__history[3].append(line)
                    self.__balance[2] -= sub
                    line = f"W {self.__account}{fund_index} {sub}"
                    self.__history[2].append(line)
                    return True
                else:
                    print(f"ERROR: Not enough funds to withdraw {money} from Short-Term Bond (CODE: ACC_WTHDW3)")
                    return False
            else:
                print(f"ERROR: Not enough funds to withdraw {money} from {self.__funds[fund_index]}")  
                return False
        else:
            print(f"ERROR: Not enough funds to withdraw {money} from {self.__funds[fund_index]}")

    def put_history(self, line):
        self.__history.append(line)

    #ex) Johnny Cash Account ID: 1001
    #       Money Market: $220
    def print_final_balances(self):
        print(f"{self.__first_name} {self.__last_name} Account ID: {self.__account}")
        for i in range(10):
            print(f"    {self.__funds[i]}: ${self.__balance[i]}")
        print("\n")

    #ex) Transaction History for Johnny Cash by fund.
    #    Money Market: $470
    #    D 10010 542
    #    W 10010 72
    def print_trans_history(self):
        print(f"Transaction History for {self.__first_name} {self.__last_name} by fund.")
        for i in range(10):
            print(f"{self.__funds[i]}: ${self.__balance[i]}")
            for j in range(0, len(self.__history[i])):
                print(f"    {self.__history[i][j]}")


    #Transaction History for Hank Williams 500 Index Fund: $10000
    #D 12534 10000
    def print_single_trans(self, fund_index):
        print(f"Transaction History for {self.__first_name} {self.__last_name} {self.__funds[fund_index]}: ${self.__balance[fund_index]}")
        for i in range(0, len(self.__history[fund_index])):
            print(f"    {self.__history[fund_index][i]}")