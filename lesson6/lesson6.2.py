user_input =  int(input("Введіть кількість секунд: "))

days = divmod(user_input, 24*60*60)
hours = divmod(days[1], 60*60)
minutes, seconds = divmod(hours[1], 60)
seconds = str(seconds)

if (days[0] % 100) >= 11 and (days[0] % 100) <= 14:
    days = (f"{days[0]} днів")
elif days[0] % 10 in [0, 5, 6, 7, 8, 9]:
    days = (f"{days[0]} днів")
elif days[0] % 10 in [2, 3, 4]:
    days = (f"{days[0]} дні")
else:
    days = (f"{days[0]} день")

hours = str(hours[0])
minutes = str(minutes)

print(f"{days}, {hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}")