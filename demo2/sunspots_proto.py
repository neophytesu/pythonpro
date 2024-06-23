from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing, PolyLine, String
from reportlab.lib import colors

data = [
    # (year, month,predicted,high,low)
    (2007, 8, 113.2, 114.2, 112.2),
    (2007, 9, 113.2, 114.2, 112.2),
    (2007, 10, 113.2, 114.2, 112.2),
    (2007, 11, 113.2, 114.2, 112.2),
    (2007, 12, 113.2, 114.2, 112.2),
    (2008, 1, 113.2, 114.2, 112.2)
]
drawing = Drawing(200, 150)
pred = [row[2] - 40 for row in data]
high = [row[3] - 40 for row in data]
low = [row[4] - 40 for row in data]
times = [200 * ((row[0] + row[1] / 12.0) - 1950) - 110 for row in data]

drawing.add(PolyLine(list(zip(times, pred)), strokeColor=colors.blue))
drawing.add(PolyLine(list(zip(times, high)), strokeColor=colors.red))
drawing.add(PolyLine(list(zip(times, low)), strokeColor=colors.green))

drawing.add(String(65, 115, 'Sunspots', fontSize=18, fillColor=colors.red))
renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')
