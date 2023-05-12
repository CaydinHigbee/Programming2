
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class ConferenceOptions(Form):
	def __init__(self, parent):
		self.parent = parent
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._groupBox2.SuspendLayout()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._label1)
		self._groupBox2.Controls.Add(self._listBox1)
		self._groupBox2.Location = System.Drawing.Point(238, 15)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(169, 100)
		self._groupBox2.TabIndex = 3
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Preconference Workshops"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(6, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(80, 17)
		self._label1.TabIndex = 1
		self._label1.Text = "Select One"
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Items.AddRange(System.Array[System.Object](
			["Intro to E-Commerce",
			"The Future of the Web",
			"Advanced Visual Basic",
			"Network Security"]))
		self._listBox1.Location = System.Drawing.Point(6, 36)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(157, 56)
		self._listBox1.TabIndex = 0
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._checkBox2)
		self._groupBox1.Controls.Add(self._checkBox1)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(220, 100)
		self._groupBox1.TabIndex = 2
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Conference"
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(13, 53)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(207, 24)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "Opening Night Dinner & Keynote: $30"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(13, 23)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(201, 24)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Conference Registration: $895"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# ConferenceOptions
		# 
		self.ClientSize = System.Drawing.Size(421, 129)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "ConferenceOptions"
		self.Text = "ConferenceOptions"
		self.FormClosing += self.ConferenceOptionsFormClosing
		self._groupBox2.ResumeLayout(False)
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def ConferenceOptionsFormClosing(self, sender, e):
		self.parent.Show()