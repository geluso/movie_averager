import png
from collections import defaultdict

def rec_dd():
  return defaultdict(rec_dd)

votes = rec_dd()

# read first 10 image files
for n in range(0, 1):
  filename = "frames/*-%d.png" % n
  print "reading", filename
  x, y, pixels, meta = png.Reader(file=open(filename)).read()
  import pdb; pdb.set_trace()

  # read pixel information
  for r, row in enumerate(pixels):
    for c, value in enumerate(row):
      cell = votes[r][c][value]
      if cell:
        print "incrementing cell"
        cell += 1
      else:
        print "creating cell", r, c, value
        cell = 1

for row in votes:
  import pdb; pdb.set_trace()
  for col in row:
    colors = votes[row][col]
    most_votes, winning_color = None, None
    for color in colors:
      occurrences = colors[color]
      if (occurrences > most_votes):
        print "new winning color", color
        wining_color = color
    results[row][col] = winning_color
print "complete"

out = open('election.png', 'wb')
w = png.Writer(x, y)
w.write(out, out_data)
