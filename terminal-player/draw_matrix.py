import math

# let the input matrix define the size later
# ROWS should be max 60
# COLUMNS should be max 128

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


# Ignores the last row if not even amount and any incomplete columns
def create_pixel_matrix(matrix):     # assume matrix is structured like [row, row2, ...]
    # update matrix sizes
    ROWS = len(matrix)
    COLUMNS = len(matrix[0])
    [matrix, COLUMNS] = fix_errors(matrix, COLUMNS)
    pixel_matrix = []
    for r in range(math.floor(ROWS/2)):
        pixel_matrix.append("")
        for c in range(COLUMNS):
            pixel_matrix[r] += choose_block(matrix[r*2][c], matrix[r*2+1][c])
    return pixel_matrix
   

def draw(pixel_matrix):   # draw the matrix
    for row in pixel_matrix:
        print(row)


# a bit of error prevention
def fix_errors(matrix, COLUMNS):
    # remove any incomplete columns
    for r in range(len(matrix)):  
        COLUMNS = min(COLUMNS, len(matrix[r]))
        # change any non-binary elements to 0
        for c in range(len(matrix[r])): 
            if matrix[r][c] not in [0,1]:
                matrix[r][c]=0
    return [matrix, COLUMNS]



# ------ run tests ---------------------

def main():
    print("start!")
    print(choose_block(0,0))
    matrix = [[1, 0, 1,1,1], [0, 1, 0, 1], [0, 0, 0], [1, 1, 0], [1,1,1], [1,1,1]]
    matrix2 = [[1, 2, 2, 1, 1, 1, 0, 0, 1, 1,1], [0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1, 1, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 1, 0, 1, 0, 1], [1, 1, 0, 0, 0, 0, 0, 1, 1, 1]]
    pm = create_pixel_matrix(matrix2)
    
    #matrix.append([1,1,1])
    #print(matrix, "wow"+"WOW")
    draw(pm)

if __name__=="__main__":
    main()