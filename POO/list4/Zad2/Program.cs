using System;
using System.Collections.Generic;

public interface IShape
{
      void Draw();
}

public class Square : IShape
{
      private readonly int _side;

      public Square(int side)
      {
            _side = side;
      }

      public void Draw()
      {
            Console.WriteLine($"rysuje square o boku {_side}");
      }
}

public class Rectangle : IShape
{
      private readonly int _width;
      private readonly int _height;

      public Rectangle(int width, int height)
      {
            _width = width;
            _height = height;
      }

      public void Draw()
      {
            Console.WriteLine($"rysuje rectangle o szerokosci {_width} i dlugosci {_height}");
      }
}

public interface IShapeFactoryWorker
{
      bool CanCreateShape(string shapeName);
      IShape CreateShape(params object[] parameters);
}

public class SquareFactoryWorker : IShapeFactoryWorker
{
      public bool CanCreateShape(string shapeName)
      {
            return shapeName.Equals("Square", StringComparison.OrdinalIgnoreCase);
      }

      public IShape CreateShape(params object[] parameters)
      {
            int side = (int)parameters[0];
            return new Square(side);
      }
}

public class RectangleFactoryWorker : IShapeFactoryWorker
{
      public bool CanCreateShape(string shapeName)
      {
            return shapeName.Equals("Rectangle", StringComparison.OrdinalIgnoreCase);
      }

      public IShape CreateShape(params object[] parameters)
      {
            int width = (int)parameters[0];
            int height = (int)parameters[1];
            return new Rectangle(width, height);
      }
}

public class ShapeFactory
{
      private readonly List<IShapeFactoryWorker> _workers = new List<IShapeFactoryWorker>();

      public ShapeFactory()
      {
            this.RegisterWorker(new SquareFactoryWorker());
      }

      public void RegisterWorker(IShapeFactoryWorker worker)
      {
            _workers.Add(worker);
      }

      public IShape CreateShape(string shapeName, params object[] parameters)
      {
            foreach (var worker in _workers)
            {
                  if (worker.CanCreateShape(shapeName))
                  {
                        return worker.CreateShape(parameters);
                  }
            }

            throw new ArgumentException($"No worker found for shape {shapeName}");
      }
}

public class Program
{
      public static void Main()
      {
            // klient
            ShapeFactory factory = new ShapeFactory();
            IShape square = factory.CreateShape("Square", 5);
            square.Draw();

            // rozszerzenie
            factory.RegisterWorker(new RectangleFactoryWorker());
            IShape rect = factory.CreateShape("Rectangle", 3, 5);
            rect.Draw();
      }
}
