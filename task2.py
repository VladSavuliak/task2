price = int(input("Введи суму для оплати: "))
ukr_bills = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
total_bills = 0

if price in ukr_bills:
    print("Для оплати товару потрібно одна купюра")
else:
    for ukr_bill in ukr_bills:
        if price >= ukr_bill:
            total_bills += price // ukr_bill
            price %= ukr_bill

    print(f"Для оплати товару потрібно {total_bills} купюр")







