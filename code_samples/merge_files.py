import glob2
from datetime import datetime

output_file = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"
with open(output_file, "w") as myfile:
    for file in glob2.glob("readFiles/*.txt"):
        with open(file, "r") as textfile:
            myfile.write(textfile.readline() + "\n")