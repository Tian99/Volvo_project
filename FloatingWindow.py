from PyQt5 import uic, QtWidgets

class FloatingWindow(QtWidgets.QDialog):

	#This class creates floating windows to every button clicked

	def __init__(self, parent = None):
		super(FloatingWindow, self).__init__(parent)

		uic.loadUi('./ui/floatingwindow.ui', self)
		#Change the window title later, as the name for each button in the user interface
		self.setWindowTitle('Sunareas')
		#Example the information after getting more knowledge of what's whould be on the table
		self.subareas_columns = ['name', 'information']
		self.subareas.setColumnCount(len(self.subareas_columns))
		self.subareas.setHorizontalHeaderLabels(self.subareas_columns)

		
		######################################
		#All the drop could be implemented later
		#Igore drop but not with CAC
		#Ignore DS
		######################################





