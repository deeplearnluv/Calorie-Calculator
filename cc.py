BIG_MAC_CALORIES = 563
FRIES_CALORIES = 378
SHAKE_CALORIES = 530

JOGGING_BURN = 398
RUNNING_BURN = 557

print("""
      Welcome to the Calorie Calculator!""")

big_mac_count = int(input("""
How many Big Mac's are you getting? 
You: """))
fries_count = int(input("""How many fries are you getting?
You: """))
shake_count = int(input("""How many shakes are you getting?
You: """))

big_mac_total = big_mac_count * BIG_MAC_CALORIES
fries_total = fries_count * FRIES_CALORIES
shake_total = shake_count * SHAKE_CALORIES

total_calories = big_mac_total + fries_total + shake_total

jog_hours = total_calories / JOGGING_BURN

run_hours = total_calories / RUNNING_BURN

print(f"""
Big Mac total calories: {big_mac_total}
Fries total calories: {fries_total}
Shake total calories: {shake_total}

Jogging hours:{int(jog_hours)}
Running hours:{int(run_hours)}""") 