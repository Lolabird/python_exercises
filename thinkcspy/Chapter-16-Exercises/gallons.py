def setState():
    jugA = {"name": "Jug A", "state": 0, "cap": 4}
    jugB = {"name": "Jug B", "state": 0, "cap": 3}
    target = 2

    return fillJug(1, jugA, jugB, target)


def fillJug(rounds, jugA, jugB, target):
    pour = 0

    if jugA["state"] == target:
        print("Target reached")
        return 
    else:
        if jugB["state"] == 0:
            jugB["state"] += jugB["cap"] #fill jugB
            print(rounds, jugA, jugB)
        
        if jugA["state"] == 0:
            pour = jugB["state"] - jugA["state"]
        else:
            pour = jugA["cap"] - jugA["state"]
            
        #fill jugA with the contents of jugB
        jugA["state"] += pour
        jugB["state"] -= pour
        print(rounds, jugA, jugB)

        if jugA["state"] == jugA["cap"]:
            jugA["state"] = 0 #empty jugA if full
            print(rounds, jugA, jugB)
        
        fillJug(rounds + 1, jugA, jugB, target)


setState()