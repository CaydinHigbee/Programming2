using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace YourNameConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your full name: ");
            string name = Console.ReadLine();
            Console.Write("Your full name is: " + name);
            Console.ReadLine();
        }
    }
}
