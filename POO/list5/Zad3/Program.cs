using System;
using System.Collections;
using System.Collections.Generic;

class Program
{
    static int IntComparer(int x, int y)
    {
        return x.CompareTo(y);
    }

    private class ComparisonComparer<T> : IComparer
    {
        private readonly Comparison<T> _comparison;

        public ComparisonComparer(Comparison<T> comparison)
        {
            _comparison = comparison;
        }

        public int Compare(object? x, object? y)
        {
            if (x is T tx && y is T ty)
            {
                return _comparison(tx, ty);
            }
            throw new ArgumentException("Objects must have the same type " + typeof(T).Name);
        }
    }

    static void Main(string[] args)
    {
        ArrayList a = new ArrayList() { 1, 5, 3, 3, 2, 4, 3 };

        a.Sort(new ComparisonComparer<int>(IntComparer));

        foreach (int i in a)
        {
            Console.Write(i);
        }
    }
}
