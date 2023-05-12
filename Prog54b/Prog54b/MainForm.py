import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkSlateBlue
		self._button1.Location = System.Drawing.Point(12, 204)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(117, 39)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkSlateBlue
		self._button2.Location = System.Drawing.Point(155, 204)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(117, 39)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkSlateBlue
		self._button3.Location = System.Drawing.Point(12, 249)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(260, 39)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkCyan
		self._label1.Location = System.Drawing.Point(43, 10)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(56, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Num 1:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkCyan
		self._label2.Location = System.Drawing.Point(43, 44)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(56, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Num 2:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkCyan
		self._label3.Location = System.Drawing.Point(43, 76)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(56, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Num 3:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkCyan
		self._label4.Location = System.Drawing.Point(43, 109)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(56, 23)
		self._label4.TabIndex = 6
		self._label4.Text = "Num 4:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(144, 7)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 7
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(144, 41)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 8
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(144, 73)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 9
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(144, 106)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 10
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkCyan
		self._label5.Location = System.Drawing.Point(10, 155)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 11
		self._label5.Text = "Sum:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkCyan
		self._label6.Location = System.Drawing.Point(155, 155)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 12
		self._label6.Text = "Average:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkViolet
		self.ClientSize = System.Drawing.Size(283, 300)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = float(self._textBox1.Text)
		num2 = float(self._textBox2.Text)
		num3 = float(self._textBox3.Text)
		num4 = float(self._textBox4.Text)
		sum = num1 + num2 + num3 + num4
		average = sum / 4
		self._label5.Text = "Sum: " + str(sum)
		self._label6.Text = "Average: " + str(average)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._label5.Text = "Sum:"
		self._label6.Text = "Average:"

	def Button3Click(self, sender, e):
		Application.Exit()