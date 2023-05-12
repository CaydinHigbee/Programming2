
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class frmGeneral(Form):
	def __init__(self, prt):
		self.prt = prt
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._txtNumTickets = System.Windows.Forms.TextBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._radSectionA = System.Windows.Forms.RadioButton()
		self._radSectionB = System.Windows.Forms.RadioButton()
		self._radSectionC = System.Windows.Forms.RadioButton()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._lblTickets = System.Windows.Forms.Label()
		self._lblTax = System.Windows.Forms.Label()
		self._lblTotal = System.Windows.Forms.Label()
		self._btnCalculate = System.Windows.Forms.Button()
		self._btnClose = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._txtNumTickets)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(10, 11)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(262, 74)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "How Many Tickets?"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Orchid
		self._label1.Location = System.Drawing.Point(80, 45)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Number of Tickets:"
		# 
		# txtNumTickets
		# 
		self._txtNumTickets.Location = System.Drawing.Point(186, 45)
		self._txtNumTickets.Name = "txtNumTickets"
		self._txtNumTickets.Size = System.Drawing.Size(57, 20)
		self._txtNumTickets.TabIndex = 1
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._radSectionC)
		self._groupBox2.Controls.Add(self._radSectionB)
		self._groupBox2.Controls.Add(self._radSectionA)
		self._groupBox2.Location = System.Drawing.Point(12, 91)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(110, 119)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Section"
		# 
		# radSectionA
		# 
		self._radSectionA.BackColor = System.Drawing.Color.DimGray
		self._radSectionA.Location = System.Drawing.Point(6, 21)
		self._radSectionA.Name = "radSectionA"
		self._radSectionA.Size = System.Drawing.Size(98, 24)
		self._radSectionA.TabIndex = 0
		self._radSectionA.TabStop = True
		self._radSectionA.Text = "Section A"
		self._radSectionA.UseVisualStyleBackColor = False
		# 
		# radSectionB
		# 
		self._radSectionB.BackColor = System.Drawing.Color.DimGray
		self._radSectionB.Location = System.Drawing.Point(6, 51)
		self._radSectionB.Name = "radSectionB"
		self._radSectionB.Size = System.Drawing.Size(98, 24)
		self._radSectionB.TabIndex = 1
		self._radSectionB.TabStop = True
		self._radSectionB.Text = "Section B"
		self._radSectionB.UseVisualStyleBackColor = False
		# 
		# radSectionC
		# 
		self._radSectionC.BackColor = System.Drawing.Color.DimGray
		self._radSectionC.Location = System.Drawing.Point(6, 81)
		self._radSectionC.Name = "radSectionC"
		self._radSectionC.Size = System.Drawing.Size(98, 24)
		self._radSectionC.TabIndex = 2
		self._radSectionC.TabStop = True
		self._radSectionC.Text = "Section C"
		self._radSectionC.UseVisualStyleBackColor = False
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._lblTotal)
		self._groupBox3.Controls.Add(self._lblTax)
		self._groupBox3.Controls.Add(self._lblTickets)
		self._groupBox3.Controls.Add(self._label4)
		self._groupBox3.Controls.Add(self._label3)
		self._groupBox3.Controls.Add(self._label2)
		self._groupBox3.Location = System.Drawing.Point(131, 91)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(141, 119)
		self._groupBox3.TabIndex = 2
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Ticket Cost"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MediumPurple
		self._label2.Location = System.Drawing.Point(6, 22)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(47, 23)
		self._label2.TabIndex = 0
		self._label2.Text = "Tickets:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.MediumPurple
		self._label3.Location = System.Drawing.Point(6, 52)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(47, 23)
		self._label3.TabIndex = 1
		self._label3.Text = "Tax:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.MediumPurple
		self._label4.Location = System.Drawing.Point(6, 82)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(47, 23)
		self._label4.TabIndex = 2
		self._label4.Text = "Total:"
		# 
		# lblTickets
		# 
		self._lblTickets.BackColor = System.Drawing.Color.CadetBlue
		self._lblTickets.Location = System.Drawing.Point(59, 21)
		self._lblTickets.Name = "lblTickets"
		self._lblTickets.Size = System.Drawing.Size(76, 24)
		self._lblTickets.TabIndex = 3
		# 
		# lblTax
		# 
		self._lblTax.BackColor = System.Drawing.Color.CadetBlue
		self._lblTax.Location = System.Drawing.Point(59, 51)
		self._lblTax.Name = "lblTax"
		self._lblTax.Size = System.Drawing.Size(76, 24)
		self._lblTax.TabIndex = 4
		# 
		# lblTotal
		# 
		self._lblTotal.BackColor = System.Drawing.Color.CadetBlue
		self._lblTotal.Location = System.Drawing.Point(59, 81)
		self._lblTotal.Name = "lblTotal"
		self._lblTotal.Size = System.Drawing.Size(76, 24)
		self._lblTotal.TabIndex = 5
		# 
		# btnCalculate
		# 
		self._btnCalculate.Location = System.Drawing.Point(67, 226)
		self._btnCalculate.Name = "btnCalculate"
		self._btnCalculate.Size = System.Drawing.Size(75, 23)
		self._btnCalculate.TabIndex = 3
		self._btnCalculate.Text = "Calculate"
		self._btnCalculate.UseVisualStyleBackColor = True
		self._btnCalculate.Click += self.BtnCalculateClick
		# 
		# btnClose
		# 
		self._btnClose.Location = System.Drawing.Point(148, 226)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(75, 23)
		self._btnClose.TabIndex = 4
		self._btnClose.Text = "Close"
		self._btnClose.UseVisualStyleBackColor = True
		# 
		# frmGeneral
		# 
		self.BackColor = System.Drawing.Color.LightSteelBlue
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._btnClose)
		self.Controls.Add(self._btnCalculate)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "frmGeneral"
		self.Text = "frmGeneral"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self.ResumeLayout(False)
		
	decTAXRATE = 0.6
	def CalcTax(cost):
		returncost * decTAXRATE

	def BtnCalculateClick(self, sender, e):
		# calculate and display the ticket costs.
		intNumTickets = 0
		decTicketCost = 0.0
		decSalesTax = 0.0
		decTotal = 0.0
		
		# Calculate the cost.
		intNumTickets = int(self._txtNumTickets.Text)
		decTicketCost = intNumTickets * PriceEachTicket()
		decSalesTax = CalcTax(decTicketCost)
		decTotal = decTicketCost + decSalseTax
		
		# Display the cost.
		self._lblTickets.Text = str(round(decTicketCost), 2)
		self._lblTax.Text = str(round(decSalesTax), 2)
		self._lblTotal.Text = str(round(decTotal), 2)