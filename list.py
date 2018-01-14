class CashRegister:

      def_init_(self):
          self_itemCount=0
          self_totalPrice=0.0

      def additem(self,price):
          self_itemCount=self_itemCount+1
          self_totalPrice=sel_totalPrice+price

      def getCount(self):
        return self_itemCount

      def clear(self):
          self_itemCount=0
          self_totalPrice=0.0

      def givechange(self,paid):
        return(paid-self._totalPrice)


    
