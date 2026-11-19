class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:        
        

        money_made = 0 # each transaction will keep a track of money made so far

        # made a bills hashmap
        bills_hsmp = {}
        for k in ([5,10,20]):
            bills_hsmp[k] = 0 # we assign all the bill counts as 0

        for i in range(len(bills)):

            transaction_amount = bills[i]
            #we find this amount in our bills_hsmp and add it to the counter
            bills_hsmp[transaction_amount] += 1
            money_made += 5
            change = transaction_amount - 5            
            if change > money_made:
                return False # this implies that we dont have enough money to provide a change
            else:

                # this is where we can use greedy
                if change == 5: # we gotta return a 5 dollar bill back
                    if bills_hsmp[5] == 0: # we dont have any 5 dollar bills, so we return false
                        return False
                    else:
                        bills_hsmp[5] -= 1 # we simply remove one bill
                
                elif change == 15:
                    # check if we have 10 bill and 5 bill
                    if bills_hsmp[10] == 0: # we have no 10 bills, then we move onto 5 bills
                        
                        if bills_hsmp[5] >= 3:
                            bills_hsmp[5] -= 3 # we straight up remove 5 dollar bills and return
                        else:
                            return False

                    else: # this means we have atleast 1 10 dollar bill
                        # now we check if bills_hsmp[5] is not zero 
                        if bills_hsmp[5] != 0:
                            bills_hsmp[10] -= 1
                            bills_hsmp[5] -= 1
                        else:
                            return False
        return True
                    
                
                


                
        return True
        