def cross(bank1, boat, bank2):
    if bank1["Missionaries"] + bank1["Cannibals"] == 0 and boat["Missionaries"] + boat["Cannibals"] == 0:
        return "Journey complete"
    
    elif bank1["Missionaries"] + bank1["Cannibals"] > 0 and boat["Missionaries"] + boat["Cannibals"] < 2:
        if bank1["Missionaries"] - 1 >= bank1["Cannibals"]:
            bank1["Missionaries"] -= 1 
            boat["Missionaries"] += 1
            print(bank1, boat, bank2)
        elif bank1["Cannibals"] > 0:
            bank1["Cannibals"] -= 1
            boat["Cannibals"] += 1
            print(bank1, boat, bank2)
        
    else:
        if boat["Cannibals"] >= 1 and bank2["Missionaries"] >= bank2["Cannibals"] + 1:
            bank2["Cannibals"] += 1
            boat["Cannibals"] -= 1
        elif boat["Missionaries"] >= 1:
             bank2["Missionaries"] += 1 
             boat["Missionaries"] -= 1
        print(bank1, boat, bank2)

    cross(bank1, boat, bank2)
         

def main():
    bank1 = {"name": "B1", "Missionaries": 3, "Cannibals": 3}
    bank2 = {"name": "B2", "Missionaries": 0, "Cannibals": 0}
    boat = {"name": "boat", "Missionaries": 0, "Cannibals": 0}

    return cross(bank1, boat, bank2)

print(main())