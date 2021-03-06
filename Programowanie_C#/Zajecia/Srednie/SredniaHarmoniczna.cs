using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Srednie
{
    class SredniaHarmoniczna : ISrednia
    {
        public double ObliczSrednia(double[] liczby)
        {
            double suma = 0;
            foreach (var liczba in liczby)
            {
                suma += 1.0 / liczba;
            }
            return liczby.Length / suma;
        }
    }
}
