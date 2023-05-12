import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._radioButton10 = System.Windows.Forms.RadioButton()
		self._radioButton11 = System.Windows.Forms.RadioButton()
		self._radioButton12 = System.Windows.Forms.RadioButton()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._checkBox4 = System.Windows.Forms.CheckBox()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self._groupBox4.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._radioButton9)
		self._groupBox1.Controls.Add(self._radioButton5)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Location = System.Drawing.Point(9, 10)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(143, 120)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Decks"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._radioButton10)
		self._groupBox2.Controls.Add(self._radioButton6)
		self._groupBox2.Controls.Add(self._radioButton2)
		self._groupBox2.Location = System.Drawing.Point(233, 10)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(143, 120)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Truck Assemblies"
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._radioButton12)
		self._groupBox3.Controls.Add(self._radioButton11)
		self._groupBox3.Controls.Add(self._radioButton7)
		self._groupBox3.Controls.Add(self._radioButton3)
		self._groupBox3.Location = System.Drawing.Point(9, 149)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(143, 154)
		self._groupBox3.TabIndex = 1
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Wheel sets"
		# 
		# groupBox4
		# 
		self._groupBox4.Controls.Add(self._checkBox4)
		self._groupBox4.Controls.Add(self._checkBox3)
		self._groupBox4.Controls.Add(self._checkBox2)
		self._groupBox4.Controls.Add(self._checkBox1)
		self._groupBox4.Location = System.Drawing.Point(233, 149)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(143, 154)
		self._groupBox4.TabIndex = 1
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "Misc."
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(6, 19)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(131, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "The Master Thrasher"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(6, 19)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "7.75 axle"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(6, 19)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "51mm"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# radioButton5
		# 
		self._radioButton5.Location = System.Drawing.Point(6, 49)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(131, 24)
		self._radioButton5.TabIndex = 1
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "The Dictator of Grind"
		self._radioButton5.UseVisualStyleBackColor = True
		# 
		# radioButton6
		# 
		self._radioButton6.Location = System.Drawing.Point(6, 49)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(104, 24)
		self._radioButton6.TabIndex = 2
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "8 axle"
		self._radioButton6.UseVisualStyleBackColor = True
		# 
		# radioButton7
		# 
		self._radioButton7.Location = System.Drawing.Point(6, 49)
		self._radioButton7.Name = "radioButton7"
		self._radioButton7.Size = System.Drawing.Size(104, 24)
		self._radioButton7.TabIndex = 3
		self._radioButton7.TabStop = True
		self._radioButton7.Text = "55mm"
		self._radioButton7.UseVisualStyleBackColor = True
		# 
		# radioButton9
		# 
		self._radioButton9.Location = System.Drawing.Point(6, 79)
		self._radioButton9.Name = "radioButton9"
		self._radioButton9.Size = System.Drawing.Size(131, 24)
		self._radioButton9.TabIndex = 2
		self._radioButton9.TabStop = True
		self._radioButton9.Text = "The street king"
		self._radioButton9.UseVisualStyleBackColor = True
		# 
		# radioButton10
		# 
		self._radioButton10.Location = System.Drawing.Point(6, 79)
		self._radioButton10.Name = "radioButton10"
		self._radioButton10.Size = System.Drawing.Size(104, 24)
		self._radioButton10.TabIndex = 3
		self._radioButton10.TabStop = True
		self._radioButton10.Text = "8.5 axle"
		self._radioButton10.UseVisualStyleBackColor = True
		# 
		# radioButton11
		# 
		self._radioButton11.Location = System.Drawing.Point(6, 79)
		self._radioButton11.Name = "radioButton11"
		self._radioButton11.Size = System.Drawing.Size(104, 24)
		self._radioButton11.TabIndex = 4
		self._radioButton11.TabStop = True
		self._radioButton11.Text = "58mm"
		self._radioButton11.UseVisualStyleBackColor = True
		# 
		# radioButton12
		# 
		self._radioButton12.Location = System.Drawing.Point(6, 109)
		self._radioButton12.Name = "radioButton12"
		self._radioButton12.Size = System.Drawing.Size(104, 24)
		self._radioButton12.TabIndex = 5
		self._radioButton12.TabStop = True
		self._radioButton12.Text = "61mm"
		self._radioButton12.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(14, 325)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(51, 23)
		self._label1.TabIndex = 2
		self._label1.Text = "Subtotal:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(70, 325)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(49, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Test1"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(14, 348)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(51, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Tax:"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(70, 348)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(49, 23)
		self._label4.TabIndex = 5
		self._label4.Text = "Test2"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(15, 371)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(51, 23)
		self._label5.TabIndex = 6
		self._label5.Text = "Total:"
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(70, 371)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(49, 23)
		self._label6.TabIndex = 7
		self._label6.Text = "Test3"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(139, 320)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 68)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(220, 320)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 68)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(301, 320)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 68)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(6, 20)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Grip Tape"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(6, 50)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "Bearings"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Location = System.Drawing.Point(6, 80)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(104, 24)
		self._checkBox3.TabIndex = 2
		self._checkBox3.Text = "Riser Pads"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# checkBox4
		# 
		self._checkBox4.Location = System.Drawing.Point(6, 110)
		self._checkBox4.Name = "checkBox4"
		self._checkBox4.Size = System.Drawing.Size(104, 24)
		self._checkBox4.TabIndex = 3
		self._checkBox4.Text = "Nuts and Bolts"
		self._checkBox4.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(388, 400)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg485SkateboardDesigner"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self._groupBox4.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		p1 = 0
		p2 = 0
		p3 = 0
		p4 = 0
		
		if self._radioButton1.Checked == True:
			p1 = 60
		elif self._radioButton5.Checked == True:
			p1 = 45
		elif self._radioButton9.Checked == True:
			p1 = 50
		
		if self._radioButton2.Checked == True:
			p2 = 35
		elif self._radioButton6.Checked == True:
			p2 = 40
		elif self._radioButton10.Checked == True:
			p2 = 45
			
		if self._radioButton3.Checked == True:
			p3 = 20
		elif self._radioButton7.Checked == True:
			p3 = 22
		elif self._radioButton11.Checked == True:
			p3 = 24
		elif self._radioButton12.Checked == True:
			p3 = 28
			
		if self._checkBox1.Checked == True:
			p4 += 10
		if self._checkBox2.Checked == True:
			p4 += 30
		if self._checkBox3.Checked == True:
			p4 += 2
		if self._checkBox4.Checked == True:
			p4 += 3
		
		subtot = p1 + p2 + p3 + p4
		tax = subtot * 2
		total = subtot + tax
		self._label2.Text = str(subtot)
		self._label4.Text = str(tax)
		self._label6.Text = str(total)