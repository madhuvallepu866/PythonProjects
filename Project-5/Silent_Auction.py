import os
def find_winner(details):
    highest_bid=0
    winner=""
    for bidder in details:#key
        bidding_price=details[bidder]#value
        if bidding_price > highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(f"All the Biddrs Details: {details}")
    print(f"The Winner Is {winner} and Bid Price is {highest_bid}")
bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("What is Your Name?: ")
    price=int(input("What is your Price?: "))
    bidder_data[name]=price
    more_bidders=input("Are there more bidders? Type 'yes' OR 'no' :").lower()
    if more_bidders == 'no':
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders == 'yes':
        os.system("cls")

