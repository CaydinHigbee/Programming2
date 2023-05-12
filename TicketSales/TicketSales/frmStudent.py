
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class frmStudent(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._txtNumTickets = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._lblTickets = System.Windows.Forms.Label()
		self._lblTax = System.Windows.Forms.Label()
		self._lblTotal = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._btnCalculate = System.Windows.Forms.Button()
		self._btnClose = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label8)
		self._groupBox1.Controls.Add(self._txtNumTickets)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(13, 9)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(228, 116)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "How Many Tickets?"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._lblTotal)
		self._groupBox2.Controls.Add(self._lblTax)
		self._groupBox2.Controls.Add(self._lblTickets)
		self._groupBox2.Controls.Add(self._label4)
		self._groupBox2.Controls.Add(self._label3)
		self._groupBox2.Controls.Add(self._label2)
		self._groupBox2.Location = System.Drawing.Point(247, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(144, 113)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Total Cost"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(8, 23)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Number of Tickets:"
		# 
		# txtNumTickets
		# 
		self._txtNumTickets.Location = System.Drawing.Point(114, 23)
		self._txtNumTickets.Name = "txtNumTickets"
		self._txtNumTickets.Size = System.Drawing.Size(72, 20)
		self._txtNumTickets.TabIndex = 1
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(6, 20)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(64, 23)
		self._label2.TabIndex = 0
		self._label2.Text = "Tickets:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(6, 43)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(64, 23)
		self._label3.TabIndex = 1
		self._label3.Text = "Tax:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(6, 66)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(64, 23)
		self._label4.TabIndex = 2
		self._label4.Text = "Total:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# lblTickets
		# 
		self._lblTickets.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._lblTickets.Location = System.Drawing.Point(76, 25)
		self._lblTickets.Name = "lblTickets"
		self._lblTickets.Size = System.Drawing.Size(55, 23)
		self._lblTickets.TabIndex = 3
		# 
		# lblTax
		# 
		self._lblTax.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._lblTax.Location = System.Drawing.Point(76, 48)
		self._lblTax.Name = "lblTax"
		self._lblTax.Size = System.Drawing.Size(55, 23)
		self._lblTax.TabIndex = 4
		# 
		# lblTotal
		# 
		self._lblTotal.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._lblTotal.Location = System.Drawing.Point(76, 71)
		self._lblTotal.Name = "lblTotal"
		self._lblTotal.Size = System.Drawing.Size(55, 23)
		self._lblTotal.TabIndex = 5
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(6, 58)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(199, 39)
		self._label8.TabIndex = 2
		self._label8.Text = "Student Tickets are for seating in the student section only."
		# 
		# btnCalculate
		# 
		self._btnCalculate.Location = System.Drawing.Point(235, 151)
		self._btnCalculate.Name = "btnCalculate"
		self._btnCalculate.Size = System.Drawing.Size(75, 23)
		self._btnCalculate.TabIndex = 2
		self._btnCalculate.Text = "Calculate"
		self._btnCalculate.UseVisualStyleBackColor = True
		self._btnCalculate.Click += self.BtnCalculateClick
		# 
		# btnClose
		# 
		self._btnClose.Location = System.Drawing.Point(316, 151)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(75, 23)
		self._btnClose.TabIndex = 3
		self._btnClose.Text = "Close"
		self._btnClose.UseVisualStyleBackColor = True
		# 
		# frmStudent
		# 
		self.ClientSize = System.Drawing.Size(403, 186)
		self.Controls.Add(self._btnClose)
		self.Controls.Add(self._btnCalculate)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "frmStudent"
		self.Text = "frmStudent"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)

	decTAXRATE = 0.6
	def CalcTax(cost):
		returncost * decTAXRATE

	def BtnCalculateClick(self, sender, e):
		intNumTickets = 0   # Number of tickets purchased
		decTicketCost = 0.0 # Ticket price
		decSalesTax = 0.0   # Sales tax
		decTotal = 0.0      #Total cost
		
		# Calculate the cost.
		intNumTickets = int(self._txtNumTickets.Text)
		decTicketCost = intNumTickets * decSTUDENT_PRICE
		decSalesTax = CalcTax(decTicketCost)
		decTotal = decTicketCost + decSalesTax
		
		# Display the cost.
		self._lblTickets.Text = str(round(decTicketCost), 2)
		self._lblTax.Text = str(round(decSalseTax), 2)
		self._lblTotal.Text = str(round(decTotal), 2)
		