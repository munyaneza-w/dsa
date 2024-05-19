import os

class UniqueInt:
    @staticmethod
    def processFile(inputFilePath, outputFilePath):
        unique_integers = set()

        with open(inputFilePath, 'r') as file:
            for line in file:
                value = UniqueInt.readNextItemFromFile(line)
                if value is not None:
                    unique_integers.add(value)

        sorted_unique_integers = sorted(unique_integers)

        with open(outputFilePath, 'w') as file:
            for integer in sorted_unique_integers:
                file.write("{0}\n".format(integer))

    @staticmethod
    def readNextItemFromFile(line):
        line = line.strip()
        
        if not line:
            return None

        parts = line.split()

        if len(parts) != 1:
            return None

        try:
            value = int(parts[0])
            if -1023 <= value <= 1023:
                return value
            else:
                return None
        except ValueError:
            return None

if __name__ == "__main__":
    input_folder = "/dsa/hw01/sample_inputs/"
    output_folder = "/dsa/hw01/sample_results/"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            output_filename = "{0}_results.txt".format(filename)
            output_path = os.path.join(output_folder, output_filename)

            UniqueInt.processFile(input_path, output_path)

