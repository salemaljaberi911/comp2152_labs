print("="*50)
print("Quastion 2 : Shopping Cart  ")
print("="*50)

cart =["apple", "banana", "milk", "bread", "apple", "eggs"]

apple_count =cart.count("apple")
print("Numbe of apples: ",apple_count)

milk_postion = cart.index("milk")
print("postion of the milk : ",milk_postion)

cart.remove("apple")

removed_item =cart.pop()
print("Removed item using pop ",removed_item)
print("Is banan in the cart? ","banana" in cart)
print("final Cart : ",cart)
print()