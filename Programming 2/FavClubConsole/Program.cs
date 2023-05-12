using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FavClubConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your favorite club or sport: ");
            string club = Console.ReadLine();
            Console.Write("Your favorite club is: " + club);
            Console.ReadLine();
        }
    }
}
