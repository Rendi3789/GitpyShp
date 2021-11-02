import shapefile
w=shapefile.Writer('./soal7', shapeType=shapefile.POLYLINE)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")


w.line([[[1,3],[5,3],[1,2],[5,2]]])