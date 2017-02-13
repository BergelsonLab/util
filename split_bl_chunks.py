import csv
import sys
import os

def split_chunks(input):
    results = []
    header = None
    with open(input, "rU") as input_file:
        reader = csv.reader(input_file)
        header = reader.next()
        chunk = []
        for row in reader:
            if row[0] == "":
                results.append(chunk)
                chunk = []
            else:
                chunk.append(row)
    return header, results

def output_chunks(header, chunks):
    for i, chunk in enumerate(chunks):
        original = os.path.basename(input_file)
        out = os.path.join(output_dir,
                           original.replace(".csv",
                                            "_{}.csv".format(i)))
        with open(out, "wb") as output:
            writer = csv.writer(output)
            writer.writerow(header)
            for row in chunk:
                writer.writerow(row)

if __name__ == "__main__":

    input_file = sys.argv[1]
    output_dir = sys.argv[2]

    header, chunks = split_chunks(input_file)
    output_chunks(header, chunks)
