from CashRegister import CashRegister

cash=CashRegister()

print(cash.getTotal())
print(cash.getcount())

cash.addition(99)

print(cash.getTotal())
print(cash.getCount())

print("your charge is".cash.givechange(120))

cash.clear()

print("cash class variable values after cleaning")
print(cash.getTotal())
print(cash.getCount())
