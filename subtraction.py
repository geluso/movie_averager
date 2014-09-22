import png
import numpy
import itertools

def px2d(filename):
  print "reading", filename
  x, y, pixels, meta = png.Reader(file=open(filename)).read()
  raw = numpy.vstack(itertools.imap(numpy.uint16, pixels))
  print meta
  return raw, x, y

average, x, y = px2d("average_shopped.png")
for i in range(10):
  frame, _, _ = px2d("frames/*-%d.png" % i)
  result = average - frame
  result = result.clip(0, 255)

  print "writing data", i
  out = file("subtraction/%d.png" % i, "w")
  w = png.Writer(x, y)
  w.write(out, result)

