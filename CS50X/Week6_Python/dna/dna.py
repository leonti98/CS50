import csv
import sys


def main():
    rows = []
    dna = ""
    sequences = []
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py database.csv sequence.txt")

    # TODO: Read database file into a variable
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    # Add all patterns to the list
    for row in rows:
        for key in row.keys():
            if key not in sequences and key != "name":
                sequences.append(key)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        reader = file.read()
        for char in reader:
            dna = dna + char

    # TODO: Find longest match of each STR in DNA sequence
    sequence_counter = {}
    for sequence in sequences:
        positions = list(find_tandem_repeats(dna, sequence))
        # creade dict of patter and consequent occurances
        try:
            max_position = max(positions, key=lambda x: x[1])
            sequence_counter[sequence] = max_position[1]
        except:
            sequence_counter[sequence] = 0

    # TODO: Check database for matching profiles
    for row in rows:
        matches = 0
        for name in sequence_counter.keys():
            if int(row[name]) == sequence_counter[name]:
                matches += 1
        if matches == len(sequence_counter):
            print(row["name"])
            sys.exit()
    print("No match")
    return


def find_tandem_repeats(sequence, search):
    """ searches through an DNA sequence and returns (position, repeats) tuples """
    if sequence == '' or search == '':
        return

    lengths = list(map(len, sequence.split(search)))
    pos = lengths[0]
    repeats = 0
    pending = False

    for l in lengths[1:]:
        if l == 0:
            pending = True
            repeats += 1
            continue
        repeats += 1
        yield (pos, repeats)
        pos += l + len(search) * repeats
        repeats = 0
        pending = False

    if pending:
        yield (pos, repeats)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
