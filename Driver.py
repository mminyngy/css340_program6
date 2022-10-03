from Bank import bank

b = bank()
b.read_file("test2.txt")
b.execute_file()
print("Processing Done. Final Balances")
#print final balances
b.summary()

 