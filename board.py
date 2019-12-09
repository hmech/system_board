import hold

class board:
    holds = []
    #fills a board with the dimensions height x width with hold objects 
    def __init__(self, height, width):
        for i in range(height):
            row = []
            for j in range(width):
                temp = hold()
                row.append(temp)
