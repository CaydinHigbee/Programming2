﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg273BookClub
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int books = int.Parse(textBox1.Text);
            int points = 0;
            if (books == 0) points = 0;
            else if (books == 1) points = 5;
            else if (books == 2) points = 15;
            else if (books == 3) points = 30;
            else if (books >= 4) points = 60;
            else label3.Text = "Invalid number of books";
            label3.Text = ("Number of points is: " + points);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label3.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
