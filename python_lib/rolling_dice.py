from dice import Dice

roll_dice_1 = Dice()
print(f"Rolling the dice for {roll_dice_1.sides} sides.")
roll_dice_1.roll_dice(10)

roll_dice_2 = Dice(10)
print(f"Rolling the dice for {roll_dice_2.sides} sides")
roll_dice_2.roll_dice(10)

roll_dice_3 = Dice(20)
print(f"Rolling the dice for {roll_dice_3.sides} sides")
roll_dice_3.roll_dice(20)
