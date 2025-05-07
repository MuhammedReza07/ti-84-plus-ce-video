import math

# let the input matrix define the size later
ROWS = -1    # should be max 60
COLUMNS = -1 # should be max 128

def choose_block(top, bottom): # [top, bottom]
    character=""
    match [top, bottom]:
        case [1,0]:
            character="▀"
        case [0,1]:
            character="▄"
        case [1,1]:
            character="█"
        case [0,0]:
            character=" "
        case _:
            character="x"  # something went wrong if this appears
    return character

# Ignores the last row if not even amount, assumes all rows are equal in length
def create_pixel_matrix(matrix):     # assume matrix is structured like [row, row2, ...]
    # update matrix sizes
    ROWS = len(matrix)
    COLUMNS = len(matrix[0])
    pixel_matrix = []
    for r in range(math.floor(ROWS/2)):
        pixel_matrix.append("")
        for c in range(COLUMNS):
            pixel_matrix[r] += choose_block(matrix[r*2][c], matrix[r*2+1][c])
    return pixel_matrix
   

def draw(pixel_matrix):   # draw the matrix
    for row in pixel_matrix:
        print(row)



# run tests

def main():
    print("start!")
    print(choose_block(0,0))
    matrix = [[1, 0, 1], [0, 1, 0, 1], [0, 0, 0], [1, 1, 0], [1,1,1], [1,1,1]]
    matrix2 = [[1, 0, 0, 1, 1, 1, 0, 0, 1, 1], [0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1, 1, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 1, 0, 1, 0, 1], [1, 1, 0, 0, 0, 0, 0, 1, 1, 1]]
    pm = create_pixel_matrix(matrix2)
    
    #matrix.append([1,1,1])
    #print(matrix, "wow"+"WOW")
    draw(pm)

if __name__=="__main__":
    main()