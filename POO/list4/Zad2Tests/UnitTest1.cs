using System;
using Xunit;

public class UnitTest1
{
    [Fact]
    public void ShapeFactory_CreatesSquare_WhenSquareWorkerIsRegistered()
    {
        var factory = new ShapeFactory();
        var shape = factory.CreateShape("Square", 4);

        Assert.IsType<Square>(shape);
    }

    [Fact]
    public void ShapeFactory_CreatesRectangle_WhenRectangleWorkerIsRegistered()
    {
        var factory = new ShapeFactory();
        factory.RegisterWorker(new RectangleFactoryWorker());
        var shape = factory.CreateShape("Rectangle", 3, 6);

        Assert.IsType<Rectangle>(shape);
    }

    [Fact]
    public void ShapeFactory_ThrowsException_WhenNoWorkerCanHandleShape()
    {
        var factory = new ShapeFactory();

        var ex = Assert.Throws<ArgumentException>(() =>
        {
            factory.CreateShape("Circle", 5);
        });

        Assert.Contains("No worker found", ex.Message);
    }
}
