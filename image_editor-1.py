import math
import random

class PPMImage(object):
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile

        # Read in data of image
        data = open(self.infile,"r")
        dataIn = data.read()
        splits = dataIn.split()

        # Reads the headers info and writes it
        self.type = splits[0]
        self.columns = int(splits[1])
        self.row = int(splits[2])
        self.colour = splits[3]

        # Splits the pixels and adds them to the matrix using the columns and row information obtained from the image
        self.pixels = splits[4:]
        self.Lines = []
        self.Data = []

        for rowCount in range(self.row):
            rowStart = rowCount * self.columns*3
            rowEnd = rowStart + (self.columns * 3)

            self.Lines.append(self.pixels[rowStart: rowEnd])

    def writeToFile(self):
        # Opens the output file and writes out the header information
        dataOut = open(self.outfile, "w")
        dataOut.write(self.type + "\n" + str(self.columns) + "\n" + str(self.row) + "\n" + self.colour + "\n")

        for line in self.Lines:
            dataOut.write(" ".join(line) + "\n")

        dataOut.close()

    def flip_horizontal(self):
        N = self.columns*3
        for row in range(self.row):
            for col in range(0, int(math.ceil(N/2)), 3):
                r = str(self.Lines[row][col])
                g = str(self.Lines[row][col+1])
                b = str(self.Lines[row][col+2])

                self.Lines[row][col] = self.Lines[row][N - col - 3]
                self.Lines[row][col+1] = self.Lines[row][N - col - 2]
                self.Lines[row][col+2] = self.Lines[row][N - col - 1]

                self.Lines[row][N - col - 3] = r
                self.Lines[row][N - col - 2] = g
                self.Lines[row][N - col - 1] = b

    def grey_scale(self):
        # Converts the supplied image to greyscale.
        for row in range(self.row):
            for col in range(0, self.columns * 3, 3):
                sum = int(self.Lines[row][col]) + int(self.Lines[row][col + 1]) + int(self.Lines[row][col + 2])
                avg = int(sum / 3)

                self.Lines[row][col] = str(avg)
                self.Lines[row][col + 1] = str(avg)
                self.Lines[row][col + 2] = str(avg)

    def flatten_red(self):
        # Loops till end of row in order to grab all red values
        for row in range(self.row):
            # loops by 3 in order to grab only red values
            for col in range(0, self.columns*3, 3):
                self.Lines[row][col]= str(0)

    def negate_red(self):
        # Grabs red values and converts to their negative value, subtracting colour value from  red value
        for row in range(self.row):
            for col in range(0, self.columns*3, 3):
                remainder = int(self.colour) - int((self.Lines[row][col]))
                self.Lines[row][col] = str(remainder)

    def extreme_contrast(self):
        for row in range(self.row):
            for col in range(0, self.columns * 3, 3):
                if int(self.Lines[row][col]) > int(self.colour) / 2:
                    self.Lines[row][col] = str(self.colour)
                elif int(self.Lines[row][col]) < int(self.colour) / 2:
                    self.Lines[row][col] = str(0)

    def random_noise(self):
        for row in range(self.row):
            for col in range(0, self.columns * 3, 3):
                add_subtract = random.randint(0,1)
                change = random.randint(0, int(self.colour))
                if add_subtract == 0 and int(self.Lines[row][col]) - change >= 0:
                    self.Lines[row][col] = str(int(self.Lines[row][col]) - change)
                elif add_subtract == 0 and int(self.Lines[row][col]) - change < 0:
                    self.Lines[row][col] = str(0)
                elif add_subtract == 1 and int(self.Lines[row][col]) + change <= 255:
                    self.Lines[row][col] = str(int(self.Lines[row][col]) + change)
                else:
                    self.Lines[row][col] = str(255)


def main():
    print("Portable Pixmap (PPM) Image Editor\n")

    input_file = input("Enter the name of image file: ")

    output_file = input("Enter the name of the output file: ")

    userInstance = PPMImage(str(input_file), str(output_file))

    print("\nHere are your choices:")
    print("[1] convert to greyscale  [2] flip horizontally")
    print("[3] negative of red  [4] no reds ")
    print("[5] extreme contrast [6] random noise")

    option1 = input("\nDo you want [1]? (y/n) ")
    option2 = input("Do you want [2]? (y/n) ")
    option3 = input("Do you want [3]? (y/n) ")
    option4 = input("Do you want [4]? (y/n) ")
    option5 = input("Do you want [5]? (y/n) ")
    option6 = input("Do you want [6]? (y/n) ")

    if option1 == "y":
        userInstance.grey_scale()

    if option2 == "y":
        userInstance.flip_horizontal()

    if option3 == "y":
        userInstance.negate_red()

    if option4 == "y":
        userInstance.flatten_red()

    if option5 == "y":
        userInstance.extreme_contrast()

    if option6 == "y":
        userInstance.random_noise()

    userInstance.writeToFile()

    print(output_file + " created.")

main()