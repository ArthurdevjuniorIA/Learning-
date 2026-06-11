for k in range(0,21,2):
    i = k/10
    for d in range(1,4):
        if k % 10 == 0:
            print(f"I={int(i)} J={int(d+i)}")
        else:
            print(f"I={i} J={d+i}")