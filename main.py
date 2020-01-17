import sys
from General import read, normalize, merge
from Categorize import analyze
from PyQt5 import uic, QtCore, QtGui, QtWidgets


class Map(QtWidgets.QMainWindow):
	def __init__(self):

		super().__init__()

		print('User interface started')
		#########################################################
		#Back end part
		#Read the claims and locaiton and store them as pickles
		df_claims, df_location = read()
		#Filter out the unused
		nor_claims, nor_location, df_claims_extra, df_claims_nons = normalize(df_claims, df_location)
		#Merge the two files
		merged = merge(nor_claims, nor_location)

		analyze(merged)

		#########################################################
		#Front end part
		uic.loadUi('./ui/MainWindow.ui', self)

		self.setWindowTitle('Factory Layout')
		#Try to get a list of all the widgest in pyqt
		# self.A_0.setStyleSheet("background-color: red")
		self.combine()

		#Set the color of certain pushbuttons

	def combine(self):

		# #Set the overall background color
		# self.setStyleSheet("background-color: white")
		#All the locations are bssed on a certain naming convention
		cluster = 0
		group = ['A','B','C']
		first_range = range(0, 45)#Find any number from range 0 to 41
		for j in group:
			cluster += 1
			for i in first_range:
				try:
					self.name = 'self.' + j + '_' + str(i) + '.setStyleSheet'
					print(self.name)
					if cluster == 1: 
						self.name = self.name + '("color: #ff5500")'
						eval(self.name)
					elif cluster == 2:
						self.name = self.name + '("color: #0000ff")'
						eval(self.name)
					elif cluster == 3:
						self.name = self.name + '("color: #5c5c8a")'
						eval(self.name)
				except AttributeError:
					continue

		print('Coloring finished')


if __name__ == '__main__':

	APP = QtWidgets.QApplication([])

	if len(sys.argv) > 1:
		WINDOW = Map(config_file=sys.argv[1])
	else:
		WINDOW = Map()

	WINDOW.show()
	sys.exit(APP.exec_())






