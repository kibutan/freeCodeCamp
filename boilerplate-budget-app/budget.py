class Category:
  def __init__(self,ctg):
    self.ctg = ctg
    # self.ledger = [{"category":ctg}]
    self.ledger = []
    self.total = 0
    self.spent = 0
    print(self.ctg)
    print("tostr",str(self))

  def __str__(self):
    title=format(self.ctg, '*^30')+"\n"
    body = ""
    for i in self.ledger:
      print("ledger",self.ledger[0]["description"])
      # body = ""
      body += str(i["description"]).ljust(23)[:23]
      body += str(format(i["amount"], ".2f")).rjust(7)+"\n"
    body += "Total: "+str(format(self.total,".2f"))
    print(title + body)
    return title + body

  def deposit(self,amt,dsp = ""):
    self.ledger.append({"amount":amt,"description":dsp})
    self.total += amt
    print("dps total amt",self.total,self.ledger)
    # return self.ledger
  
  def check_funds(self,amt = ""):
    if self.total < amt:return False
    else:return True

  def withdraw(self,amt,dsp = ""):
    if self.check_funds(amt):
      self.ledger.append({"amount":-1*amt,"description":dsp})
      self.total -= amt
      self.spent += amt
      print("wdr",self.total,self.ledger)
      return True
    else:return False
  
  def get_balance(self):
    return self.total
  
  def transfer(self,amt = "",ctg_obj=""):
    if self.check_funds(amt):
      ctg_obj.ledger.append({"amount":amt,"description":"Transfer from " +str(self.ctg)})
      self.ledger.append({"amount":-1*amt,"description":"Transfer to " +str(ctg_obj.ctg)})
      self.total -= amt
      ctg_obj.total += amt
      return True
    else:return False

def create_spend_chart(categories):
  sum = 0
  rate={}
  max_len = 0
  for i in categories:
    print("***************categories spent*************", i.ctg,i.spent)
    sum += i.spent
  for i in categories:
    rate[i.ctg] = (((i.spent*100)/sum)//10)*10
    max_len = max(max_len,len(i.ctg))
  print(sum)
  print("o rate--------------------------:",rate)

  graph = "Percentage spent by category\n"
  for j in range(100,-10,-10):
    graph += str(j).rjust(3)+"| "
    for i in range(len(categories)):      
      if(rate[categories[i].ctg] >= j):graph += "o  "
      else:graph += "   "
    graph += "\n"
  graph += "    ----------\n"
  for j in range(max_len):
    graph += " "*5
    for i in range(len(categories)):      
      if(len(categories[i].ctg) >= j+1):graph += categories[i].ctg[j]+"  "
      else:graph += "   "
    graph += "\n"
  graph = graph.rstrip()
  graph += "  "
  print(graph)

  return graph
