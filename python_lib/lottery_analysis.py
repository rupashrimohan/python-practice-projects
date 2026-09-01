from random import choice

my_lottery = (1, 4, 3, 5, 53, 555, 77, 233, "PP", "yy", "lglk")
my_win = "PP"
count = 0
active_state = True
while active_state:
    win = choice(my_lottery)
    if my_win == win:
        print(f"my_win: {my_win} and win: {win}")
        active_state = False
    else:
        print(win)
        count += 1
print(f"The number of time the loop ran to find my winning{win} lotter is {count}")
