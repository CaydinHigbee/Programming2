import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._btnGeneral = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._btnStudent = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._btnStudent)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._btnGeneral)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(326, 141)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Select Type of Ticket Sales"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Violet
		self._label1.Location = System.Drawing.Point(6, 28)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(202, 38)
		self._label1.TabIndex = 0
		self._label1.Text = "Select General Sales for all ticket sales in the general public."
		# 
		# btnGeneral
		# 
		self._btnGeneral.BackColor = System.Drawing.Color.MediumPurple
		self._btnGeneral.Location = System.Drawing.Point(215, 19)
		self._btnGeneral.Name = "btnGeneral"
		self._btnGeneral.Size = System.Drawing.Size(105, 48)
		self._btnGeneral.TabIndex = 1
		self._btnGeneral.Text = "General Sales"
		self._btnGeneral.UseVisualStyleBackColor = False
		self._btnGeneral.Click += self.BtnGeneralClick
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Violet
		self._label2.Location = System.Drawing.Point(6, 81)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(202, 35)
		self._label2.TabIndex = 2
		self._label2.Text = "Select Student Sales for all student ticket sales."
		# 
		# btnStudent
		# 
		self._btnStudent.BackColor = System.Drawing.Color.MediumPurple
		self._btnStudent.Location = System.Drawing.Point(214, 73)
		self._btnStudent.Name = "btnStudent"
		self._btnStudent.Size = System.Drawing.Size(105, 48)
		self._btnStudent.TabIndex = 3
		self._btnStudent.Text = "Student Sales"
		self._btnStudent.UseVisualStyleBackColor = False
		# 
		# btnExit
		# 
		self._btnExit.BackColor = System.Drawing.Color.Salmon
		self._btnExit.Location = System.Drawing.Point(223, 162)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(75, 23)
		self._btnExit.TabIndex = 1
		self._btnExit.Text = "Exit"
		self._btnExit.UseVisualStyleBackColor = False
		self._btnExit.Click += self.BtnExitClick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSteelBlue
		self.ClientSize = System.Drawing.Size(350, 197)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "TicketSales"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def BtnGeneralClick(self, sender, e):
		from frmGeneral import *
		formG = frmGeneral(self)
		formG.Show()
		self.Hide()

	def BtnExitClick(self, sender, e):
		Application.Exit()