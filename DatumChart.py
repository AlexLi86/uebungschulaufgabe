from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QSplineSeries, QValueAxis, QAbstractAxis, QDateTimeAxis
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QPixmap, QBrush, QColor, QPen
# Package: PyQt6-Charts
# https://github.com/chey00/qchart
class DatumChart(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        #series erstellt
        self.series = QLineSeries()
        self.series2 = QSplineSeries()
        self.series.setName("Series")
        self.series2.setName("Series2")

        #Farbe für die Line ändern
        #pen = QPen(QColor(144, 238, 144))
        #pen.setWidth(5)
        #self.series.setPen(pen)

        #andere methode für farbe hinzufügen
        self.series.setColor(QColor("blue"))
        self.series2.setColor(QColor("yellow"))


        #chart erstellt und series hinzufgefügt
        self.chart = QChart()
        self.chart.setTitle("2te Chart")
        self.chart.setTitleBrush(QColor("green"))
        self.chart.addSeries(self.series)
        self.chart.addSeries(self.series2)

        #achsen erstellt und range eingestellt
        axis_y = QValueAxis()
        axis_y.setRange(0, 10)



        #datum x-achse erstellen
        axis_x = QDateTimeAxis()
        axis_x.setTickCount(10)  # Anzahl der Datenpunkte (Tage)
        axis_x.setFormat("dd.MM")  # Format des Datums
        axis_x.setTitleText("Datum")
        axis_x.setTitleBrush(QColor("green"))

        start_date = QDateTime.currentDateTime()
        end_date = QDateTime.currentDateTime().addDays(-9)
        axis_x.setRange(end_date, start_date)

        #achsen andere farbe
        axis_x.setLabelsColor(QColor("blue"))
        axis_y.setLabelsColor(QColor("white"))

        #grid farbe ändern
        pen_grid = QPen(QColor("red"))
        axis_x.setGridLinePen(pen_grid)
        axis_y.setGridLineColor(QColor("blue"))


        #achsen dem chart hinzugefügt
        self.chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        #nachdem achsen hinzufügen einfügen
        self.series.attachAxis(axis_x)
        self.series.attachAxis(axis_y)

        self.series2.attachAxis(axis_x)
        self.series2.attachAxis(axis_y)

        #werte für die series hinzufügen
        self.series.append(QDateTime.currentDateTime().addDays(-9).toMSecsSinceEpoch(), 1)
        self.series.append(QDateTime.currentDateTime().addDays(-8).toMSecsSinceEpoch(), 2)
        self.series.append(QDateTime.currentDateTime().addDays(-7).toMSecsSinceEpoch(), 3)
        self.series.append(QDateTime.currentDateTime().addDays(-6).toMSecsSinceEpoch(), 4)



        #werte für 2te series hinzufügen
        self.series2.append(QDateTime.currentDateTime().addDays(-9).toMSecsSinceEpoch(), 4)
        self.series2.append(QDateTime.currentDateTime().addDays(-8).toMSecsSinceEpoch(), 5)
        self.series2.append(QDateTime.currentDateTime().addDays(-7).toMSecsSinceEpoch(), 6)
        self.series2.append(QDateTime.currentDateTime().addDays(-6).toMSecsSinceEpoch(), 7)

        #Manuel datum hinzufügen
        #self.series2.append(QDateTime(2024, 2, 1, 0, 0).toMSecsSinceEpoch(), 3.5)
        #self.series2.append(QDateTime(2025, 2, 9, 0, 0).toMSecsSinceEpoch(), 4.0)
        #self.series2.append(QDateTime(2026, 2, 5, 0, 0).toMSecsSinceEpoch(), 5.5)
        #self.series2.append(QDateTime(2027, 2, 6, 0, 0).toMSecsSinceEpoch(), 4.0)
        #self.series2.append(QDateTime(2028, 2, 7, 0, 0).toMSecsSinceEpoch(), 6.0)
        #self.series2.append(QDateTime(2029, 2, 3, 0, 0).toMSecsSinceEpoch(), 9.0)
        #self.series2.append(QDateTime(2030, 2, 5, 0, 0).toMSecsSinceEpoch(), 3.5)


        #hintergrund farbe ändern
        self.chart.setBackgroundBrush(QColor("black"))

        #chart anzeigen
        self.setChart(self.chart)
