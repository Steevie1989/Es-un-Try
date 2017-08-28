using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SortingAlgorithmPractice
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] unarray = { 100, 0, 12, 2, 6, 5, 3, 99, 55, 8, 45, 12 };
            //  bubbleswap(unarray);
            selectionsort(unarray);
            for(int i = 0; i < unarray.Length; i++)
            {
                Console.WriteLine(unarray[i]);
            }
            Console.Read();
        }
       static int[] bubbleswap(int[] elarray)
        {
            for (int i = 0; i < elarray.Length; i++)
            {
                for (int j = i + 1; j < elarray.Length; j++)
                {
                    //  Console.WriteLine("\n this is the value before swap index i", + elarray[i]);
                    //   Console.WriteLine("this is the value before swap index j", + elarray[j]);
                    if (elarray[i] > elarray[j])
                    {
                        int temp = elarray[i];
                        elarray[i] = elarray[j];
                        elarray[j] = temp;

                    }
                }
            }return elarray;
        } static int[] selectionsort(int[] elarray)
        {
          
            for(int i = elarray.GetUpperBound(0); i>=0; i--)
            { int highvalue = elarray[0];
               int highindex = 0;
                for (int j = 1; j <= i; j++)
                {
                    if (highvalue < elarray[j])
                    {
                        highvalue = elarray[j];
                        highindex = j;
                    }
                }
                if (highindex != i)
                {
                    int temp = elarray[i];
                    elarray[i] = highvalue;
                    elarray[highindex] = temp;
                }
            } return elarray;
        }
    }
}
