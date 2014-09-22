import png
import numpy
import itertools

total = 10
image = None
for n in range(total):
  filename = "frames/*-%d.png" % n
  print "reading", filename
  x, y, pixels, _ = png.Reader(file=open(filename)).asDirect()
  image_2d = numpy.vstack(itertools.imap(numpy.uint16, pixels))

  if n == 0:
    image = image_2d
  else:
    image = image + image_2d

image = image / total

print "writing data"
out = file("numper.png", "w")
w = png.Writer(x, y)
w.write(out, image)

