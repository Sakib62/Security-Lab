def checkSame(h1, h2):
    i = 0
    cnt = 0
    for ch in h1:
        if ch==h2[i]:
            cnt = cnt + 1
        i = i + 1

    print("Number of same bit: ", cnt)

h1 = "482c48d5234eff1ca0a1cb3f6d47f8fc"
h2 = "823a13f73f84674bd64ec678e074ef16"

checkSame(h1, h2)