import glob

read_files = glob.glob("*.log")

with open("result.log", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
