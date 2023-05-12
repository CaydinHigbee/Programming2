import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(8, 7)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(379, 235)
		self._button1.TabIndex = 0
		self._button1.Text = "Show new Form"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(394, 251)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "MultiForm"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self, "Goodbye World!")
		form1.Show()
		self.Hide()

	def MainFormLoad(self, sender, e):
		pass