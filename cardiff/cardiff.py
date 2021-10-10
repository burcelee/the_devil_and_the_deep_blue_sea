
import csv
import argparse
import os.path
import warnings

options = "d:"
long_options = ["directory"]

def directory_type(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--baseline_directory", required=True, help="Baseline files", metavar="FILE", type=directory_type)
parser.add_argument("-n", "--new_directory", required=True, help="New files", metavar="FILE", type=directory_type)
parser.add_argument("-o", "--output_directory", required=True, help="Output directory", metavar="FILE", type=directory_type)

args = parser.parse_args()



baseline_files = os.listdir(args.baseline_directory)
new_files = os.listdir(args.new_directory)



def add_rows_from_file(filepath, row_list):
    with open(filepath) as file:
        reader = csv.reader(file)
        for row in reader:
            row_list.append(tuple(row))

def diff_file_name(old_name):
    return "diff_"+old_name
    
changes = [] # [] of tuple(file, num changes)


for file in new_files:
    baseline_rows = []
    new_rows = []
    
    if not file.endswith('.csv'):
        continue
    new_file_path = os.path.join(args.new_directory, file)
    base_file_path = os.path.join(args.baseline_directory, file)
    add_rows_from_file(new_file_path, new_rows)
    if file in baseline_files:
        add_rows_from_file(base_file_path, baseline_rows)
        # hashing container
        baseline_rows = set(baseline_rows)
        

        diff = []
        #preserve order. skip header
        for row in new_rows[1:]:
            if row not in baseline_rows:
                diff.append(row)
    else:
        # skip header
        diff = new_rows[1:]
    
    diff_path = os.path.join(args.output_directory, diff_file_name(file))
    # Remove the file. We won't necessarily remove diff files that aren't in new - probably fine.
    try:
        os.remove(diff_path)
    except FileNotFoundError as err: 
        pass
    if diff:
        changes.append((file, len(diff)))
        with open(diff_path, 'w', newline='') as diff_file:
            writer = csv.writer(diff_file)
            # Write column names. future make this use csv.has_header
            writer.writerow(new_rows[0])
            for row in diff:
                writer.writerow(list(row))
    else:
        print("Removed unchanged file " + diff_path)

if changes:
    print("Changes (file, dissimilar rows):")
    for change in changes:
        print(change)
else:
    print("No changes detected")