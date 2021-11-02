import shapefile

j = shapefile.Writer('shapefile/soal10/soal10', shapeType=shapefile.POLYGON)
j.shapeType

j.field('Kolom 1', 'C')
j.field('Kolom 2', 'C')

j.record('ngek', 'satu')
j.record('hai', 'dua')
j.record('aku', 'tiga')
j.record('sayang', 'empat')
j.record('kamu', 'lima')
j.record('kamuuh', 'enam')

j.poly([[[4,3],[1,1],[7,1],[4,3]]])
j.poly([[[3,6],[1,4],[5,4],[3,6]]])
j.poly([[[8,4],[6,6],[10,6],[8,4]]])
j.poly([[[3,7],[5,9],[1,9],[3,7]]])
j.poly([[[8,9],[6,7],[10,7],[8,9]]])
j.poly([[[11,12],[9,10],[13,10],[11,12]]])

j.close()