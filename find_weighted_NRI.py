while True:

    print("How many different NRIs are there?")
    nri_count = int(input())

    all_nris = []
    all_acreages = []
    royalty_acres = []

    counter = 1
    for a in range(nri_count):
        nri_1 = float(input("What is NRI # " + str(counter)))
        all_nris.append(nri_1)
        counter = counter + 1

    counter = 1
    for a in range(nri_count):
        acreage_1 = float(input("What is acreage #" + str(counter)))
        all_acreages.append(acreage_1)
        counter = counter + 1

    counter = 0
    for a in range(nri_count):
        royalty_acre = all_nris[counter] * all_acreages[counter]
        royalty_acres.append(float(royalty_acre))
        counter = counter + 1

    weighted_nri = sum(royalty_acres) / sum(all_acreages)

    print('Your weighted NRI is: ' + str(weighted_nri))
    print('Your total acreage is: ' + str(sum(all_acreages)))









