
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Venus(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.parent = parent
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label8 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(11, 203)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(263, 45)
		self._button1.TabIndex = 17
		self._button1.Text = "Close"
		self._button1.UseVisualStyleBackColor = True
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(128, 158)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 16
		self._label8.Text = "472C"
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(128, 113)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 15
		self._label7.Text = "4.87 x 10^24 kg"
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(138, 59)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 14
		self._label6.Text = "0.7233 AU"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(138, 13)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 13
		self._label5.Text = "Terrestrial"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Coral
		self._label4.Location = System.Drawing.Point(14, 158)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(94, 23)
		self._label4.TabIndex = 12
		self._label4.Text = "Surface Temp:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Coral
		self._label3.Location = System.Drawing.Point(14, 113)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(94, 23)
		self._label3.TabIndex = 11
		self._label3.Text = "Mass:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Coral
		self._label2.Location = System.Drawing.Point(14, 59)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(94, 34)
		self._label2.TabIndex = 10
		self._label2.Text = "Average distance from sun:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Coral
		self._label1.Location = System.Drawing.Point(11, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(94, 23)
		self._label1.TabIndex = 9
		self._label1.Text = "Type:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# Venus
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "Venus"
		self.Text = "Venus"
		self.FormClosing += self.VenusFormClosing
		self.ResumeLayout(False)


	def Label6Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self.Close()
		self.parent.Show()

	def VenusFormClosing(self, sender, e):
		self.parent.Show()