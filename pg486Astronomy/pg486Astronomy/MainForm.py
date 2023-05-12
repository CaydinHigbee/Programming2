import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label9 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._button10 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label9
		# 
		self._label9.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label9.Location = System.Drawing.Point(12, 280)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(53, 23)
		self._label9.TabIndex = 37
		self._label9.Text = "Pluto:"
		self._label9.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label8
		# 
		self._label8.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label8.Location = System.Drawing.Point(12, 246)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(53, 23)
		self._label8.TabIndex = 36
		self._label8.Text = "Neptune:"
		self._label8.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label7
		# 
		self._label7.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label7.Location = System.Drawing.Point(12, 212)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(53, 23)
		self._label7.TabIndex = 35
		self._label7.Text = "Uranus:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label6
		# 
		self._label6.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label6.Location = System.Drawing.Point(12, 178)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(53, 23)
		self._label6.TabIndex = 34
		self._label6.Text = "Saturn:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label5
		# 
		self._label5.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label5.Location = System.Drawing.Point(12, 145)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(53, 23)
		self._label5.TabIndex = 33
		self._label5.Text = "Jupiter:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label4
		# 
		self._label4.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label4.Location = System.Drawing.Point(12, 111)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(53, 23)
		self._label4.TabIndex = 32
		self._label4.Text = "Mars:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label3
		# 
		self._label3.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label3.Location = System.Drawing.Point(12, 77)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(53, 23)
		self._label3.TabIndex = 31
		self._label3.Text = "Earth:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label2
		# 
		self._label2.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label2.Location = System.Drawing.Point(12, 43)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(53, 23)
		self._label2.TabIndex = 30
		self._label2.Text = "Venus:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label1
		# 
		self._label1.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(53, 23)
		self._label1.TabIndex = 29
		self._label1.Text = "Mercury:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# button10
		# 
		self._button10.Location = System.Drawing.Point(12, 309)
		self._button10.Name = "button10"
		self._button10.Size = System.Drawing.Size(134, 34)
		self._button10.TabIndex = 28
		self._button10.Text = "Exit"
		self._button10.UseVisualStyleBackColor = True
		self._button10.Click += self.Button10Click
		# 
		# button9
		# 
		self._button9.Location = System.Drawing.Point(71, 275)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(75, 28)
		self._button9.TabIndex = 27
		self._button9.UseVisualStyleBackColor = True
		self._button9.Click += self.Button9Click
		# 
		# button8
		# 
		self._button8.Location = System.Drawing.Point(71, 241)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(75, 28)
		self._button8.TabIndex = 26
		self._button8.UseVisualStyleBackColor = True
		self._button8.Click += self.Button8Click
		# 
		# button7
		# 
		self._button7.Location = System.Drawing.Point(71, 207)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(75, 28)
		self._button7.TabIndex = 25
		self._button7.UseVisualStyleBackColor = True
		self._button7.Click += self.Button7Click
		# 
		# button6
		# 
		self._button6.Location = System.Drawing.Point(71, 173)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(75, 28)
		self._button6.TabIndex = 24
		self._button6.UseVisualStyleBackColor = True
		self._button6.Click += self.Button6Click
		# 
		# button5
		# 
		self._button5.Location = System.Drawing.Point(71, 140)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(75, 28)
		self._button5.TabIndex = 23
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(71, 106)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(75, 28)
		self._button4.TabIndex = 22
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(71, 4)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 28)
		self._button3.TabIndex = 21
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(71, 38)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 28)
		self._button2.TabIndex = 20
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(71, 72)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 28)
		self._button1.TabIndex = 19
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(156, 351)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button10)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "pg486Astronomy"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		from Mercury import *
		Mercury = Mercury(self)
		Mercury.Show()
		self.Hide()

	def Button2Click(self, sender, e):
		from Venus import *
		Venus = Venus(self)
		Venus.Show()
		self.Hide()

	def Button1Click(self, sender, e):
		from Earth import *
		Earth = Earth(self)
		Earth.Show()
		self.Hide()

	def Button4Click(self, sender, e):
		from Mars import *
		Mars = Mars(self)
		Mars.Show()
		self.Hide()

	def Button5Click(self, sender, e):
		from Jupiter import *
		Jupiter = Jupiter(self)
		Jupiter.Show()
		self.Hide()

	def Button6Click(self, sender, e):
		from Saturn import *
		Saturn = Saturn(self)
		Saturn.Show()
		self.Hide()

	def Button7Click(self, sender, e):
		from Uranus import *
		Uranus = Uranus(self)
		Uranus.Show()
		self.Hide()

	def Button8Click(self, sender, e):
		from Neptune import *
		Neptune = Neptune(self)
		Neptune.Show()
		self.Hide()

	def Button9Click(self, sender, e):
		from Pluto import *
		Pluto = Pluto(self)
		Pluto.Show()
		self.Hide()

	def Button10Click(self, sender, e):
		Application.Exit()