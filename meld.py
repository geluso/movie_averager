import png
import numpy
import itertools

def px2d(filename):
  print "reading", filename
  x, y, pixels, meta = png.Reader(file=open(filename)).read()
  raw = numpy.vstack(itertools.imap(numpy.uint16, pixels))
  print meta
  return raw, x, y

one, x, y = px2d("subtraction.png")
two, x, y = px2d("subtraction-invert.png")
result = (one + two) / 2
result = result.clip(0, 255)

print "writing data"
out = file("meld.png", "w")
w = png.Writer(x, y)
w.write(out, result)

