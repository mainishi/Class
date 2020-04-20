print("Name: Mailyn Nishiguchi")

# I received some help from the TA, Yi Shang, during recitation. I also referred to the textbook "Python in easy steps" by Mike McGrath. 

# Play the game loop
play = True
while play:
    print("Welcome to Lunar Lander")
    
    # Initial variables
    altitude = 1000
    velocity = 0.0
    fuel = 1000
    seconds = 0
    print("Initial altitude:",altitude,"meters")
    print("Initial velocity:",velocity,"meters/second")
    print("Initial fuel:",fuel,"liters")

    # When the altitude is positive, the following calculations will occur
    while (altitude > 0):
        fuel_to_burn = input("How much fuel would you like to burn?")
        fuel_to_burn = float(fuel_to_burn)

        # If the user tries to burn negative fuel
        if fuel_to_burn < 0:
            fuel_to_burn = 0

        # If the user tries to burn more fuel than they have 
        elif fuel_to_burn > fuel:
            fuel_to_burn = fuel
            fuel = fuel - (fuel_to_burn)

        # If the user burns an acceptable amount of fuel, caluculate how much fuel is left 
        else:
            fuel = fuel - (fuel_to_burn)
        print("current fuel=",fuel,"liters")

        # Calculation of how many seconds
        second = 1
        seconds= second + 1

        # Caluculation of velocity based on fuel to burn
        velocity = velocity + (1.6 * second)
        velocity = velocity - (0.15 * (fuel_to_burn))
        print ("current velocity=",velocity,"meters/second")

        # Calculation of altitude 
        altitude = altitude - velocity
        print ("current altitude=",altitude,"meters")

    # If the altitude is 0 or negative, print final variable amounts
    if altitude <= 0:
        print("final velocity=",velocity)
        print("total seconds=",seconds)
        print("fuel left=",fuel)
        
        # If the velocity is too high and will result in a dangerous landing, lose the game
        if velocity >= 10:
            print("Oh no! You lose! Unsafe landing")

    # If the velocity at an amount for safe landing, win the game
    if velocity < 10:
        print("You win! Congratulations on successfully landing on the moon")

    # Asking if the user would like to play again    
    correct = False
    while not correct:        
        end = input("Would you like to play again?:")
        if end.startswith('y') or end.startswith('Y'):
            print("Yay!")
            correct = True
        elif end.startswith('n') or end.startswith('N'):
            print("Thank you for playing, goodbye")
            correct = True
            play = False  
