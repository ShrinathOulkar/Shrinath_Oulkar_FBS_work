
area_one_wall = float(input("Enter area of one wall (in sq meters): "))
interior_cost = float(input("Enter cost per sq meter for interior painting: "))
exterior_cost = float(input("Enter cost per sq meter for exterior painting: "))

# Assume 4 walls per room, 2 rooms => 8 walls
total_area = area_one_wall * 8
total_area_1= area_one_wall * 7


# Total costs
total_interior = total_area * interior_cost
total_exterior = total_area_1 * exterior_cost

print(f"Total Interior Painting Cost: {total_interior}")
print(f"Total Exterior Painting Cost: {total_exterior}")
