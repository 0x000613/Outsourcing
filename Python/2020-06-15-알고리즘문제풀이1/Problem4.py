calllist = [("min", "01011111111"), ("jin", "01022222222"), ("jay", "01033333333"), ("ken", "01044444444"), ("ain", "01055555555")]
for target in ["jake", "jin"]:
    for callnumber in calllist:
        if callnumber[0] == target:
            print(callnumber[1])