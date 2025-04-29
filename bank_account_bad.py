class bankaccount:
 def __init__(self,Owner,balance=0):self.Owner=Owner;self.Balance=balance
 def Deposit(self,AMOUNT):self.Balance=self.Balance+AMOUNT
 def withdraw(self,aMt):
     if(self.Balance>=aMt):self.Balance=self.Balance-aMt;print("withdrawn",aMt)
     else:print("Insufficient Funds!")
 def DisplayBalance(self):print("Balance for "+self.Owner+": "+str(self.Balance))
 def OwnerDetails(self):print("Account owner:"+self.Owner)
