using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace Pg498Payroll
{
    public partial class Form1 : Form
    {
        const decimal decHOURLY_PAY_RATE = 6.0m;
        const int intMAX_EMPLOYEES = 5;
        
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int[] intHours = new int[intMAX_EMPLOYEES];
            // Make new int array of capacity intMAX_EMPLOYEES
            // Capacity can never change, unlike lists in python
            int intcount = 0;
            int intEmpHours = 0;
            decimal decEmpPay = 0.0m;

            for (intcount = 0; intcount < intMAX_EMPLOYEES; intcount++) {
                while (int.TryParse(Interaction.InputBox("Enter the number of hours worked by employee #" + (intcount + 1).ToString(), "Need Hours Worked"), out intEmpHours) == false)
                {
                    MessageBox.Show("Please enter an integer for hours worked");
                }
                intHours[intcount] = intEmpHours;
            }
            listBox1.Items.Clear();
            for (intcount = 0; intcount < intMAX_EMPLOYEES; intcount++)
            {
                decEmpPay = intHours[intcount] * decHOURLY_PAY_RATE;
                listBox1.Items.Add("Employee " + (intcount + 1).ToString() +
                    " earned " + decEmpPay.ToString("$.00"));
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
