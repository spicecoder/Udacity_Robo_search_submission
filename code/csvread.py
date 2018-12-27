with open('some.csv', newline='') as f:
  reader = csv.reader(f)
  row1 = next(reader)  # gets the first line
  # now do something here 
  # if first row is the header, then you can do one more next() to get the next row:
  # 