#get the price of each item
item1=input("Enter the price of the first item: ")
#converting price into a floating number
item1=float(input("Enter the price of the first item: "))
item2=float(input("Enter the price of the second item: "))
item3=float(input("Enter the price of the third item: "))
item4=float(input("Enter the price of the fourth item: "))
item5=float(input("Enter the price of the fifth item: "))
#calculate the subtotal - no tax
subtotal=item1+item2+item3+item4+item5
#calculate sales tax for the items
#define tax object
tax_rate=0.07
#calculate sales tax using rate
tax=subtotal*tax_rate
#calculate total - with tax
total=subtotal+tax
#print the values
print(f'Subtotal: {subtotal:.2f}')
print(f'Sales Tax: {tax:.2f}')
print(f'Total: {total:.2f}')