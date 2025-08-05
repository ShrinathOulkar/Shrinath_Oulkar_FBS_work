#3. A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
#for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
#length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
#cost of fencing the field.


r = 20
l= 50
b = 40

peri_of_Feild = (2 * l )+ b  + ( 3.14 * r)

barbed_wire = peri_of_Feild * 5

cost_of_fencing = barbed_wire * 35

print(f"Cost of fencing the feild is :{cost_of_fencing}")