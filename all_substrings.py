def AllSubstrs(S):
    for i in range(l):
        for j in range(l):
            temp = S[i:j]
            if temp != "":
                print temp
            else:
                pass

string = "1234fasdfadf"
AllSubstrs(string)
