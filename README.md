# SQL2CSV
Simple Python script to turn MySql dump files into CSV files.


## Usage
Place `.sql` files with insert statements to the `in` directory, run `python sql2csv.py`, results will be generated in the `out` directory.

In directories `in` and `out` there are `.gitkeep` files. You can delete them. They are there so git would track the "empty" folders.

## Example
Turn this SQL:
```
INSERT INTO `webtemp` VALUES (1,'18967632','4145','24.1','29.5','5.2','-9999','no,no,no,no','Dew point','C','n/a','900','202001271308'),(2,'18967632','4145','22.6','32.2','5.1','-9999','no,no,no,no','Dew point','C','n/a','900','202001271323');
```

Into the following CSV:
```
"1";"18967632";"4145";"24.1";"29.5";"5.2";"-9999";"no,no,no,no";"Dew point";"C";"n/a";"900";"202001271308"
"2";"18967632";"4145";"22.6";"32.2";"5.1";"-9999";"no,no,no,no";"Dew point";"C";"n/a";"900";"202001271323"
```
