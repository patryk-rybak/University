namespace Zad3Tests;

public class UnitTest1
{
    [Fact]
    public void InvalidSize_ThrowsArgumentException()
    {
        Assert.Throws<ArgumentException>(() =>
        {
            var pool = new ObjectPool(0);
        });
    }

    [Fact]
    public void ValidSize_ReturnsReusableInstance()
    {
        var pool = new ObjectPool(1);
        var reusable = pool.AcquireReusable();
        Assert.NotNull(reusable);
    }

    [Fact]
    public void CapacityDepleted_ThrowsWhenAcquiringBeyondLimit()
    {
        var pool = new ObjectPool(1);
        var reusable = pool.AcquireReusable();

        Assert.Throws<ArgumentException>(() =>
        {
            var reusable2 = pool.AcquireReusable();
        });
    }

    [Fact]
    public void ReusedInstance_IsReturnedBackToPool()
    {
        var pool = new ObjectPool(1);
        var reusable = pool.AcquireReusable();
        pool.ReleaseReusable(reusable);
        var reusable2 = pool.AcquireReusable();

        Assert.Same(reusable, reusable2);
    }

    [Fact]
    public void ReleaseInvalidInstance_ThrowsException()
    {
        var pool = new ObjectPool(1);
        var external = new Reusable();

        Assert.Throws<ArgumentException>(() =>
        {
            pool.ReleaseReusable(external);
        });
    }

    [Fact]
    public void DoWork_OnReleasedResource_ThrowsInvalidOperationException()
    {
        var better = new BetterReusable();
        better.Release();

        var ex = Assert.Throws<InvalidOperationException>(() =>
        {
            better.DoWork();
        });

        Assert.Contains("released", ex.Message);
    }

    [Fact]
    public void Release_Twice_ThrowsInvalidOperationException()
    {
        var better = new BetterReusable();
        better.Release();

        Assert.Throws<InvalidOperationException>(() =>
        {
            better.Release();
        });
    }
}