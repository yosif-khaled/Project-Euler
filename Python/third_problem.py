# I am still bad at math
#problem not resolved
#too many calculations
#search for better solution

primefctr_list = []

def prime_fctr_finder(n, range_X):

    for a in range (range_X):

        a += 1

        for b in range (range_X):
            if b < a:
                b += 1
            else:
                break

            for c in range (range_X):
                if c < b:
                    c += 1
                else:
                    break

                for d in range(range_X):
                    if d < c:
                        d += 1
                    else:
                        break

                    if (a*b*c*d) == n and a != 1 and b != 1 and c != 1 and d != 1:

                        primefctr_list.append(a)
                        primefctr_list.append(b)
                        primefctr_list.append(c)
                        primefctr_list.append(d)


sea = prime_fctr_finder(13195, 100)
print(max(primefctr_list))