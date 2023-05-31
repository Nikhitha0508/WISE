import sys
def wall_construction(width_of_wall, height_of_wall, type3_bricks_available, type2_bricks_available, type1_bricks_available):
    string = 'The Wall'
    width = width_of_wall
    if width_of_wall > type3_bricks_available * 3 + type2_bricks_available * 2 + type1_bricks_available * 1 or height_of_wall <= 0:
        return 'case not possible'
    while height_of_wall >= 1:
        width_of_wall = width
        if width_of_wall > type3_bricks_available * 3 + type2_bricks_available * 2 + type1_bricks_available * 1:
            string += '\n Required case is not possible because we are left with '
            string += str(type3_bricks_available * 3 + type2_bricks_available * 2 + type1_bricks_available * 1)
            string += ' bricks only'
            break
        else:
            string += '\n'
            brick,type3_bricks_available, type2_bricks_available, type1_bricks_available=build_wall(width_of_wall,type3_bricks_available, type2_bricks_available, type1_bricks_available)
            string += '\n'
            string+=brick
            height_of_wall=height_of_wall-1
    return string

def build_wall(width_of_wall,type3_bricks_available, type2_bricks_available, type1_bricks_available):
    brick = ""
    string1 = ""
    string2 = ""
    for i in range(type3_bricks_available):
        if width_of_wall >= 3:
            string1 +=  15 * "*"
            string2 += "*" +(" " * (15 - 2)) + "*"
            type3_bricks_available = type3_bricks_available - 1
            width_of_wall = width_of_wall - 3
    
    for i in range(type2_bricks_available):
        if width_of_wall >= 2:
            string1 +=  10 * "*"
            string2 += "*" +(" " * (10 - 2)) + "*"
            type2_bricks_available = type2_bricks_available - 1
            width_of_wall = width_of_wall - 2
    
    for i in range(type1_bricks_available):
        if width_of_wall >= 1:
            string1 +=  5 * "*"
            string2 += "*" +(" " * (5 - 2)) + "*"
            type1_bricks_available = type1_bricks_available - 1
            width_of_wall = width_of_wall - 1
            
    brick += string1 + '\n' + string2 + '\n' + string1
    return brick, type3_bricks_available, type2_bricks_available, type1_bricks_available

print(wall_construction(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])))
            
