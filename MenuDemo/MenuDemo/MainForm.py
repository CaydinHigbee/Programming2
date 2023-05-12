﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._lblMessage = System.Windows.Forms.Label()
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._mnuFile = System.Windows.Forms.ToolStripMenuItem()
		self._mnuFileExit = System.Windows.Forms.ToolStripMenuItem()
		self._mnuColor = System.Windows.Forms.ToolStripMenuItem()
		self._mnuColorRed = System.Windows.Forms.ToolStripMenuItem()
		self._mnuColorGreen = System.Windows.Forms.ToolStripMenuItem()
		self._mnuColorBlue = System.Windows.Forms.ToolStripMenuItem()
		self._mnuColorBlack = System.Windows.Forms.ToolStripMenuItem()
		self._toolStripMenuItem1 = System.Windows.Forms.ToolStripSeparator()
		self._mnuColorVisible = System.Windows.Forms.ToolStripMenuItem()
		self._mnuHelp = System.Windows.Forms.ToolStripMenuItem()
		self._mnuHelpAbout = System.Windows.Forms.ToolStripMenuItem()
		self._contextMenuStrip1 = System.Windows.Forms.ContextMenuStrip(self._components)
		self._menuStrip1.SuspendLayout()
		self.SuspendLayout()
		# 
		# lblMessage
		# 
		self._lblMessage.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblMessage.Location = System.Drawing.Point(2, 355)
		self._lblMessage.Name = "lblMessage"
		self._lblMessage.Size = System.Drawing.Size(472, 31)
		self._lblMessage.TabIndex = 0
		self._lblMessage.Text = "Hello World!"
		self._lblMessage.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# menuStrip1
		# 
		self._menuStrip1.BackColor = System.Drawing.Color.MediumSeaGreen
		self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._mnuFile,
			self._mnuColor,
			self._mnuHelp]))
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(475, 24)
		self._menuStrip1.TabIndex = 1
		self._menuStrip1.Text = "menuStrip1"
		# 
		# mnuFile
		# 
		self._mnuFile.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._mnuFileExit]))
		self._mnuFile.Name = "mnuFile"
		self._mnuFile.Size = System.Drawing.Size(37, 20)
		self._mnuFile.Text = "&File"
		# 
		# mnuFileExit
		# 
		self._mnuFileExit.BackColor = System.Drawing.Color.PowderBlue
		self._mnuFileExit.Name = "mnuFileExit"
		self._mnuFileExit.ShortcutKeys = System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Q
		self._mnuFileExit.Size = System.Drawing.Size(152, 22)
		self._mnuFileExit.Text = "E&xit"
		self._mnuFileExit.Click += self.MnuFileExitClick
		# 
		# mnuColor
		# 
		self._mnuColor.BackColor = System.Drawing.Color.MediumSeaGreen
		self._mnuColor.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._mnuColorRed,
			self._mnuColorGreen,
			self._mnuColorBlue,
			self._mnuColorBlack,
			self._toolStripMenuItem1,
			self._mnuColorVisible]))
		self._mnuColor.Name = "mnuColor"
		self._mnuColor.Size = System.Drawing.Size(48, 20)
		self._mnuColor.Text = "&Color"
		# 
		# mnuColorRed
		# 
		self._mnuColorRed.BackColor = System.Drawing.Color.PowderBlue
		self._mnuColorRed.Name = "mnuColorRed"
		self._mnuColorRed.Size = System.Drawing.Size(152, 22)
		self._mnuColorRed.Text = "&Red"
		self._mnuColorRed.Click += self.MnuColorRedClick
		# 
		# mnuColorGreen
		# 
		self._mnuColorGreen.BackColor = System.Drawing.Color.PowderBlue
		self._mnuColorGreen.Name = "mnuColorGreen"
		self._mnuColorGreen.Size = System.Drawing.Size(152, 22)
		self._mnuColorGreen.Text = "&Green"
		self._mnuColorGreen.Click += self.MnuColorGreenClick
		# 
		# mnuColorBlue
		# 
		self._mnuColorBlue.BackColor = System.Drawing.Color.PowderBlue
		self._mnuColorBlue.Name = "mnuColorBlue"
		self._mnuColorBlue.Size = System.Drawing.Size(152, 22)
		self._mnuColorBlue.Text = "&Blue"
		self._mnuColorBlue.Click += self.MnuColorBlueClick
		# 
		# mnuColorBlack
		# 
		self._mnuColorBlack.BackColor = System.Drawing.Color.PowderBlue
		self._mnuColorBlack.Name = "mnuColorBlack"
		self._mnuColorBlack.Size = System.Drawing.Size(152, 22)
		self._mnuColorBlack.Text = "&Black"
		self._mnuColorBlack.Click += self.MnuColorBlackClick
		# 
		# toolStripMenuItem1
		# 
		self._toolStripMenuItem1.BackColor = System.Drawing.Color.PowderBlue
		self._toolStripMenuItem1.Name = "toolStripMenuItem1"
		self._toolStripMenuItem1.Size = System.Drawing.Size(149, 6)
		# 
		# mnuColorVisible
		# 
		self._mnuColorVisible.BackColor = System.Drawing.Color.PowderBlue
		self._mnuColorVisible.Checked = True
		self._mnuColorVisible.CheckOnClick = True
		self._mnuColorVisible.CheckState = System.Windows.Forms.CheckState.Checked
		self._mnuColorVisible.Name = "mnuColorVisible"
		self._mnuColorVisible.Size = System.Drawing.Size(152, 22)
		self._mnuColorVisible.Text = "Visible"
		self._mnuColorVisible.Click += self.MnuColorVisibleClick
		# 
		# mnuHelp
		# 
		self._mnuHelp.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._mnuHelpAbout]))
		self._mnuHelp.Name = "mnuHelp"
		self._mnuHelp.Size = System.Drawing.Size(44, 20)
		self._mnuHelp.Text = "&Help"
		# 
		# mnuHelpAbout
		# 
		self._mnuHelpAbout.BackColor = System.Drawing.Color.PowderBlue
		self._mnuHelpAbout.Name = "mnuHelpAbout"
		self._mnuHelpAbout.Size = System.Drawing.Size(152, 22)
		self._mnuHelpAbout.Text = "&About"
		self._mnuHelpAbout.Click += self.MnuHelpAboutClick
		# 
		# contextMenuStrip1
		# 
		self._contextMenuStrip1.Name = "contextMenuStrip1"
		self._contextMenuStrip1.Size = System.Drawing.Size(61, 4)
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SeaGreen
		self.ClientSize = System.Drawing.Size(475, 419)
		self.Controls.Add(self._lblMessage)
		self.Controls.Add(self._menuStrip1)
		self.MainMenuStrip = self._menuStrip1
		self.Name = "MainForm"
		self.Text = "Menu Demo"
		self._menuStrip1.ResumeLayout(False)
		self._menuStrip1.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()


	def MnuFileExitClick(self, sender, e):
		Application.Exit()

	def MnuColorRedClick(self, sender, e):
		self._lblMessage.ForeColor = Color.Red

	def MnuColorGreenClick(self, sender, e):
		self._lblMessage.ForeColor = Color.Green

	def MnuColorBlueClick(self, sender, e):
		self._lblMessage.ForeColor = Color.Blue

	def MnuColorBlackClick(self, sender, e):
		self._lblMessage.ForeColor = Color.Black

	def MnuColorVisibleClick(self, sender, e):
		if self._mnuColorVisible.Checked == True:
			self._lblMessage.Visible = True
		else:
			self._lblMessage.Visible = False

	def MnuHelpAboutClick(self, sender, e):
		MessageBox.Show("Menu system demo\n" \
		"Designed for starting out " \
		"with windows form applications",
		"About Menu Demo")