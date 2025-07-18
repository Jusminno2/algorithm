N, M = map(int, input().split())

adult = 2
elderly = 3
baby = 4

for ad in range(N+1):
    for el in range(N - ad + 1):
        ba = N - ad - el
        legs = adult * ad + elderly * el + baby * ba

        if legs == M:
            print(ad, el, ba)
            exit()

print(-1, -1, -1)
