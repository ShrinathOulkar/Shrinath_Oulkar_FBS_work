amt =int(input("Entyer Amount"))

temp = amt
n_2000 = temp //2000
temp =temp % 2000

n_500 = temp // 500
temp  = temp % 500

n_200 = temp // 200
temp = temp % 200

n_100 = temp // 100
temp  = temp % 100

n_50 = temp // 50
temp  = temp% 50

n_20 = temp // 20
temp  = temp% 20

n_10 = temp // 10
temp  = temp% 10

print(f"2k notes :{n_2000}\n500 notes :{n_500}\n200 notes :{n_200}\n 100 notes :{n_100}\n50 notes :{n_50}\n20 notes :{n_20}\n10 notes :{n_10}")


total_amount = n_2000+n_500+n_200+n_100+n_50+n_20+n_10

print(f"Total Amount :{total_amount}")