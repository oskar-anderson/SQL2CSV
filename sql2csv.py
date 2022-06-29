#!/usr/bin/env python
import csv
import os


def parse_sql_insert_statement2list(line: str):
    """Parse SQL insert statement values
    
    Args:
        line: SQL insert statement string. Example 1: "INSERT INTO Authors VALUES ("Mark", "Twain");".

    Returns:
        list: a list of rows(list) containing column values (string)

    Example:
        >>> parse_sql_insert_statement2list("INSERT INTO 'CarBrands' (Id, Name) VALUES (1,'Volkswagen'),(2, 'BMW');")
        [['1', 'Volkswagen'], ['2', 'BMW']]
    """
    input = line.partition(' VALUES ')[2] # remove string before ' VALUE '
    input = input.rstrip(';').rstrip(')')
    input = input.lstrip('(')
    rows = input.split("),(") # now we should have a list of strings, but the strings are unparsed SQL values
    reader = csv.reader(rows, # https://docs.python.org/2/library/csv.html#csv-fmt-params
                        delimiter=',',  # defaults to `,`, but you might need `;` or something else
                        doublequote=False,
                        escapechar='\\',
                        quotechar="'",
                        strict=True, # raise error on bad CSV
                        skipinitialspace=True # removes whitespace after delimiter
                        )
    parsed_rows = [row for row in reader]
    return parsed_rows


def parse_files():
    """Handle SQL file reading and CSV file writing
    """
    root = './in/'
    file_names = os.listdir(root)
    file_names = [x for x in file_names if x != ".gitkeep"]
    for full_file_name in file_names: 
        [file_name, extension] = os.path.splitext(full_file_name)
        print(file_name)
        print(extension)
        if (extension == "gitkeep"):
            continue
        parsed_lines = []
        with open(root + full_file_name, "r") as input_file:
            for line in input_file:
                parsed_lines.extend(parse_sql_insert_statement2list(line))
        with open(f'./out/{file_name}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile,
                                quoting=csv.QUOTE_NONNUMERIC, 
                                delimiter=";")
            for parsed_line in parsed_lines:
                writer.writerow(parsed_line)


def main():
    parse_files()
    print('Generated CSV files are in "out" directory.')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
