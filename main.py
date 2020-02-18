import sys
import FloatingWindow
from functools import partial
from Categorize import analyze
from General import read, normalize, merge
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

		#Drop the unused and merge the used by its class number(Vehicle model family)
		analyze(merged)


		#########################################################
		#Front end part
		uic.loadUi('./ui/MainWindow.ui', self)
		#Add rhe floating windoe to every buttons in the userinterface
		self.FloatingWindow = FloatingWindow.FloatingWindow(self)
		#loop thought every possibility and call the specific window
		self.detection()
		self.setWindowTitle('Factory Layout')
		self.coloring()

		#Set the color of certain pushbuttons
	#This function is to detect which button is clicked
	#Which means loop through every signle one of them
	def detection(self):
		# print('clicking detected')
		group = ['A', 'B', 'C']
		limit = range(0, 45)
		for j in group:
			for i in limit:
				convention = j+'_'+str(i)
				name =  'self.'+j+'_'+str(i)+'.clicked.connect(partial(self.floating_window_pushed, convention))'
				# print(name)
				try:
					eval(name)
				except AttributeError:
					continue


	def floating_window_pushed(self, convention):
		sys.path.insert(0, '../data')
		import recognition
		#Every window should look different because every button have different aasignments, implement it later.
		dictionary = recognition.combination
		self.FloatingWindow.show()
		#Set the location in the floating window
		self.FloatingWindow.location.setText(dictionary[convention])
		print(dictionary[convention])

		# name = j+'_'+str(i)
		# print(name)


	def coloring(self):

		# Set the overall background color
		# self.setStyleSheet("background-color: white")
		#All the locations are bssed on a certain naming convention
		#The code below colors the userinterface
		cluster = 0
		group = ['A','B','C']
		first_range = range(0, 45)#Find any number from range 0 to 41
		for j in group:
			cluster += 1
			for i in first_range:
				try:
					self.name = 'self.' + j + '_' + str(i) + '.setStyleSheet'
					# print(self.name)
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

	def fill_update_table(self):
		#THe table keeps tracks of the most recent update, also the small useful informaiton
		print('Still implementing')




#The code download called everything
if __name__ == '__main__':

	APP = QtWidgets.QApplication([])

	if len(sys.argv) > 1:
		WINDOW = Map(config_file=sys.argv[1])
	else:
		WINDOW = Map()

	WINDOW.show()
	sys.exit(APP.exec_())






