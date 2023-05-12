using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pg273
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter number of books purchased: ");
            int books = int.Parse(Console.ReadLine());
            int points = 0;
            if (books == 0) points = 0;
            else if (books == 1) points = 5;
            else if (books == 2) points = 15;
            else if (books == 3) points = 30;
            else if (books >= 4) points = 60;
            else Console.WriteLine("Invalid number of books");
            Console.WriteLine("Number of points is: " + points);
            Console.ReadLine();
        }
    }
}
