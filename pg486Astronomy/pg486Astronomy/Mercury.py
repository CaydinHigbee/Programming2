
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Mercury(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.parent = parent
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Coral
		self._label1.Location = System.Drawing.Point(9, 14)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(94, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Type:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Coral
		self._label2.Location = System.Drawing.Point(12, 60)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(94, 34)
		self._label2.TabIndex = 1
		self._label2.Text = "Average distance from sun:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Coral
		self._label3.Location = System.Drawing.Point(12, 114)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(94, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Mass:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Coral
		self._label4.Location = System.Drawing.Point(12, 159)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(94, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Surface Temp:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(136, 14)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 4
		self._label5.Text = "Terrestrial"
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(136, 60)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 5
		self._label6.Text = "0.387 AU"
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(126, 114)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 6
		self._label7.Text = "3.31*10^23 kg"
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(126, 159)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 7
		self._label8.Text = "-173C to 430C"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(9, 204)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(263, 45)
		self._button1.TabIndex = 8
		self._button1.Text = "Close"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# Mercury
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
		self.Name = "Mercury"
		self.Text = "Mercury"
		self.FormClosing += self.MercuryFormClosing
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.Close()
		self.parent.Show()

	def MercuryFormClosing(self, sender, e):
		self.parent.Show()