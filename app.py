# 1
len_string = lambda text: len(text)

print(f"Matn uzunligi: {len_string('Hello')}")


# 2
check_num = lambda num: "Musbat" if num > 0 else("Manfiy" if num < 0 else "Nol")

print(check_num(5))


# 3
surface = lambda asos, balandlik: 0.5 *  asos * balandlik

print(surface(4, 2))


# 4
even_odd = lambda num: True if num % 2 == 0 else False

print(even_odd(3))


# 5
check_num_2 = lambda num: "10 dan katta" if num > 10 else "10 dan kichik"

print(check_num_2(15))
