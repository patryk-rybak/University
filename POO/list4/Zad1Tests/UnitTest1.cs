using System;
using System.Threading;
using System.Threading.Tasks;
using Xunit;
using Zad1;

namespace Zad1Tests
{
    public class SingletonTests
    {
        [Fact]
        public void ProcessSingleton_ShouldReturnSameInstance()
        {
            var instance1 = ProcessSingleton.GetInstance();
            var instance2 = ProcessSingleton.GetInstance();

            Assert.Same(instance1, instance2);
        }

        [Fact]
        public void ThreadSingleton_ShouldReturnSameInstanceInSameThread()
        {
            var instance1 = ThreadSingleton.GetInstance();
            var instance2 = ThreadSingleton.GetInstance();

            Assert.Same(instance1, instance2);
        }

        [Fact]
        public void ThreadSingleton_ShouldReturnDifferentInstancesInDifferentThreads()
        {
            ThreadSingleton? instance1 = null;
            ThreadSingleton? instance2 = null;

            var t1 = new Thread(() => instance1 = ThreadSingleton.GetInstance());
            var t2 = new Thread(() => instance2 = ThreadSingleton.GetInstance());

            t1.Start();
            t2.Start();

            t1.Join();
            t2.Join();

            Assert.NotNull(instance1);
            Assert.NotNull(instance2);
            Assert.NotSame(instance1, instance2);
        }

        [Fact]
        public void TimedSingleton_ShouldReturnSameInstanceWithin5Seconds()
        {
            var instance1 = TimedSingleton.GetInstance();
            Thread.Sleep(1000); 
            var instance2 = TimedSingleton.GetInstance();

            Assert.Same(instance1, instance2);
        }

        [Fact]
        public void TimedSingleton_ShouldReturnDifferentInstanceAfter5Seconds()
        {
            var instance1 = TimedSingleton.GetInstance();
            Thread.Sleep(6000); 
            var instance2 = TimedSingleton.GetInstance();

            Assert.NotSame(instance1, instance2);
        }
    }
}
