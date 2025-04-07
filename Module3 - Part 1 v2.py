#Part 1: Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the user to enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales tax. Display each of these amounts and the total price.
def main():
    #Get user input for food
    numDishes = int(input('Please enter the number of dishes ordered: '))
    foodList = []
    i = 1
    for i in range(numDishes):
        foodList.append(float(input('Please enter the price your dish: ')))
        i += 1

    #Add up the total cost of food
    foodTotal = round(sum(foodList),2)

    #Calculate sales tax using food and drink cost
    salesTax = round(foodTotal * 0.07,2)
    # Calculate subtotal using food and drink + sales tax
    subtotal = round(foodTotal + salesTax,2)
    # Calculate tip using subtotal
    tip = round(subtotal * 0.18,2)
    # Calculate total using subtotal + tip
    total = round(subtotal + tip,2)

    #print itemized bill
    print('Food Cost Before Tax & Tip: $',(foodTotal))
    print('Sales Tax: $' ,(salesTax))
    print('Subtotal: $' ,(subtotal))
    print('Tip: $',(tip))
    print('Total: $',(total))
if __name__ == '__main__': main()
