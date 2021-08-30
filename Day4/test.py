def fun(num):
        inc = ""
        for i in range(len(num)):
               inc = inc + str((int(num[i]) + 1) % 10)
        return inc
ans = fun(str(31902))
print(ans)