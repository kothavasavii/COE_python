def calculate_total(cart):
    total=sum(cart.values())
    if total>20000 and total<50000:
        total*=0.1
    if total>=50000:
        total*=0.15
    return total


cart={'laptop':500,'headphones':2000,'mouse':35000,'keyboard':1500,'monitor':8000,'USB drvie':1000}
print(f"cart items:{cart}")
print(f"total price:{calculate_total(cart)}")