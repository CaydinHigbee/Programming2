import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.HotPink
		self._label1.Location = System.Drawing.Point(12, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Radius:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(172, 18)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.HotPink
		self._label2.Location = System.Drawing.Point(12, 66)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Area:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.HotPink
		self._label3.Location = System.Drawing.Point(158, 66)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(114, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "Circumference:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightPink
		self._button1.Location = System.Drawing.Point(12, 102)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 27)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightPink
		self._button2.Location = System.Drawing.Point(158, 102)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(106, 27)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightPink
		self._button3.Location = System.Drawing.Point(12, 135)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(252, 27)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkOrchid
		self.ClientSize = System.Drawing.Size(284, 165)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pi = float(3.14159)
		radius = float(self._textBox1.Text)
		area = round(radius * pi * radius, 3)
		circ = round(2 * pi * radius, 3)
		self._label2.Text = "Area: " + str(area)
		self._label3.Text = "Circumference: " + str(circ)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label2.Text = "Area:"
		self._label3.Text = "Circumference:"

	def Button3Click(self, sender, e):
		Application.Exit()