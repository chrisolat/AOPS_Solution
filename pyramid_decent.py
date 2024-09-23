def find_path(pyramid, target):
    # Helper function for recursive descent
    def recurse(row, index, product, path):
        if row == len(pyramid):
            # If we are at the bottom row and the product is equal to the target
            if product == target:
                return path
            else:
                return None
        
        # Explore left (index remains the same) and right (index + 1)
        if index < len(pyramid[row]):
            left_path = recurse(row + 1, index, product * pyramid[row][index], path + 'L')
            if left_path:
                return left_path
        if index + 1 < len(pyramid[row]):
            right_path = recurse(row + 1, index + 1, product * pyramid[row][index + 1], path + 'R')
            if right_path:
                return right_path
        
        return None
    
    # Start from the top of the pyramid at index 0
    return recurse(1, 0, pyramid[0][0], '')

pyramid = []
target = 0
first = True
with open("pyramid_sample_input.txt", "r") as inputfile:
    lines = inputfile.readlines()
    for line in lines:
        if first:
            data = line.split(":")
            num = data[1].strip()
            target = int(num)
            first = False
        else:
            data = line.split(",")
            numlist = []
            for n in data:
                numlist.append(int(n))
            pyramid.append(numlist)
    # print(line)
output = ""
with open("pyramid_sample_output.txt", "r") as sampleoutputfile:
    lines = sampleoutputfile.readlines()
    output = lines[0].strip()

path = ""
if pyramid:
    path = find_path(pyramid, target)
print("Result: %s, expected: %s" % (path, output))