using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg266LargeSmall
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string strnum1 = textBox1.Text;
            string strnum2 = textBox2.Text;
            int num1 = 0;
            int num2 = 0;
            if (int.TryParse(strnum1, out num1)) {
                num1 = num1;
            }
            else {
                label2.Text = "Error invalid input";
            } if (int.TryParse(strnum2, out num2)) {
                num2 = num2;
            }
            else
            {
                label2.Text = "Error invalid input";
            }
            if (num1 > num2) label2.Text = "A is greater than B";
            else if (num2 > num1) label2.Text = " B is greater than A";
            else if (num1 == num2) label2.Text = "A and B are equal";
            if (int.TryParse(strnum1, out num1))
            {
                num1 = num1;
            }
            else
            {
                label2.Text = "Error invalid input";
            } if (int.TryParse(strnum2, out num2))
            {
                num2 = num2;
            }
            else
            {
                label2.Text = "Error invalid input";
            }
        }
    }
}
