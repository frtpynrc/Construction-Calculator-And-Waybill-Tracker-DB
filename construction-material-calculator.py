## First, we define the concrete calculation function with the def keyword
def calculateConcrete(length, width, height):
    concreteVolume = length * width * height
    return concreteVolume

## Then, using the def keyword again, we define the formwork calculation function
def calculateFormwork(length, height):
    formworkArea = length * height
    return formworkArea

## We ask the user for information about which type of quantity calculation to perform
quantityType = input("Enter the quantity type (Formwork/Concrete): ")

## Based on the user input, if formwork quantity will be calculated, our conditions start here
if quantityType == "Formwork":
    elementType = input("Possible answers to the following question are;\nSlab,\nColumn,\nBeam,\nFloor Slab,\nWing Slab\nEnter the element type: ")
    if elementType == "Slab":
        length = float(input("Length: "))
        width = float(input("Width: "))
        height = float(input("Height: "))
        formworkResult = calculateFormwork((2 * length + 2 * width), height)
        print("Slab Formwork quantity: ", formworkResult, "m2")
    elif elementType == "Column":
        length = float(input("Length: "))
        width = float(input("Width: "))
        height = float(input("Height: "))
        formworkResult = calculateFormwork((2 * length + 2 * width), height)
        print("Column Formwork quantity: ", formworkResult, "m2")
    elif elementType == "Beam":
        width = float(input("Beam Width: "))
        length = float(input("Beam Length: "))
        height = float(input("Height: "))
        depth = float(input("Floor Slab Depth: "))
        formworkResult = calculateFormwork((2 * height - 2 * depth + width), length)
        print("Beam Formwork quantity: ", formworkResult, "m2")
    elif elementType == "Floor Slab":
        outerLength = float(input("Outer Length: "))
        outerWidth = float(input("Outer Width: "))
        formworkResult = calculateFormwork(outerLength, outerWidth)
        print("Floor Slab Formwork quantity: ", formworkResult, "m2")
    elif elementType == "Wing Slab":
        outerLength = float(input("Outer Length: "))
        outerWidth = float(input("Outer Width: "))
        height = float(input("Height: "))
        formworkResult = calculateFormwork((2 * outerLength + 2 * outerWidth), height)
        print("Wing Slab Formwork quantity: ", formworkResult, "m2")
    else:
        print("Invalid input")

## Based on the user input, if concrete quantity will be calculated, our conditions start here
elif quantityType == "Concrete":
    elementType = input("Possible answers to the following question are;\nSlab,\nColumn,\nBeam,\nFloor Slab\nEnter the element type: ")
    if elementType in ["Slab", "Column", "Floor Slab"]:
        length = float(input("Length: "))
        width = float(input("Width: "))
        height = float(input("Height: "))
        concreteClass = input("Enter the Concrete Class: ")
        concreteResult = calculateConcrete(length, width, height)
        print("Concrete quantity: ", concreteResult, "m3", "(", concreteClass, ")")
    elif elementType == "Beam":
        width = float(input("Beam Width: "))
        length = float(input("Beam Length: "))
        height = float(input("Height: "))
        depth = float(input("Floor Slab Depth: "))
        concreteClass = input("Enter the Concrete Class: ")
        concreteResult = calculateConcrete(width, length, (height - depth))
        print("Concrete quantity: ", concreteResult, "m3", "(", concreteClass, ")")
    else:
        print("Invalid input")

## We end our conditions here
else:
    print("Invalid input")
