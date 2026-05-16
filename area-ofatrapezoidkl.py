def calculate_trapezium_area():
    print("---Trapezium Area Calculator---")
    try:
        #take interactive inputs from the user
        base1 = float(input("Enter the length of the first base (cm):"))
        base2 = float(input("Enter the length of the second base (cm):"))
        height = float(input("Enter the height of the trapezium (cm):"))
        
        #calculate the area of the trapezium
        #Formula: ((a+b) / 2) * h 
        area = ((base1 + base2) / 2) * height

        #Round the result to 2 decimal places 
        final_area = round(area, 2)

        #Display the final result with units
        print(f"The area of the trapezium is: {final_area} cm²")
    #Handle invalid input
    except ValueError:
        print("Invalid input. Please enter numeric values for bases and height.")   


