using System;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProgramSonson
{
    class Program
    {
        static void Main(string[] args)
        {
            string team1, team2;
            int pronostic1, pronostic2;
            int score1, score2;
            int userTotal = 0;
            int loop = 0;
            // This calculate the total Point for the Pronostic of 3 Games
            while (loop < 3)
            {
                Console.WriteLine("{0,18}","Who is playing ");
                Console.Write("\t Team 1 : ");
                team1 = Console.ReadLine();
                Console.Write("\t Team 2 : ");
                team2 = Console.ReadLine();
                Console.WriteLine("Enter Your pronostic for the Game ");
                Console.Write("\t" + team1 + " : ");
                pronostic1 = int.Parse(Console.ReadLine());
                Console.Write("\t" + team2 + " : ");
                pronostic2 = int.Parse(Console.ReadLine());
                Console.WriteLine("The Game score is : ");
                Console.Write("\t" + team1 + " : ");
                score1 = int.Parse(Console.ReadLine());
                Console.Write("\t" + team2 + " : ");
                score2 = int.Parse(Console.ReadLine());
                if(pronostic1==score1 && pronostic2 == score2)
                {
                    Console.WriteLine(" 'BOOM', You Guessed it right , You have earn 9 Points");
                    userTotal += 9;

                }
              else  if (pronostic1 > pronostic2 && score1 > score2 || pronostic2 > pronostic1 && score2 > score1)
                {
                    Console.WriteLine("You have earn 6 points ");
                    userTotal += 6;
                }
                else if (pronostic1 == pronostic2 && score1 == score2)
                {
                    Console.WriteLine("You have earn 3 point ");
                    userTotal += 3;
                }
                else { Console.WriteLine("You have earn 0 points "); }
                loop += 1;
                Console.WriteLine();
            }
            Console.WriteLine("Based on your pronostics ");
            Console.WriteLine("Your Total Point is : " + userTotal);
            Console.Read();
          

        }
    }
}
