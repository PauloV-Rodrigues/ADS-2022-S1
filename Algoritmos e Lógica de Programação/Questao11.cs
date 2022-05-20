using System;

namespace CSharp_Questao
{
    public class Counter
    {
        public static void Main(string[] args)
        {
            int i = 0;
            do {
                Console.WriteLine(i);
				i += 3;
            } while(i <= 30);
            Console.WriteLine("Acabou!");
        }
    }
}