using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LP4_5
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter the percentage: ");
            double grade = double.Parse(Console.ReadLine());
            char letgare = ' ';
            if (grade > 90)
            {
                letgare = 'A';
            }
            else if (grade >= 80)
            {
                letgare = 'B';
            }
            else if (grade >= 70)
            {
                letgare = 'C';
            }
            else if (grade >= 60)
            {
                letgare = 'D';
            }
            else
            {
                letgare = 'F';
            }
            Console.WriteLine("The corrasponding letter grade is: " + letgare);
            Console.ReadLine();
        }
    }
}
