from PyQt5 import uic, QtWidgets

class FloatingWindow(QtWidgets.QDialog):

	#This class creates floating windows to every button clicked

	def __init__(self, parent = None):
		super(FloatingWindow, self).__init__(parent)

		uic.loadUi('./ui/floatingwindow.ui', self)
		#Change the window title later, as the name for each button in the user interface
		self.setWindowTitle('Change it later')



