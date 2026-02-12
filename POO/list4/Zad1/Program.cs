using System;
using System.Threading;

namespace Zad1;

// process
public sealed class ProcessSingleton
{
	private static ProcessSingleton? _instance;
	public static ProcessSingleton GetInstance()
	{
		if (_instance == null)
			_instance = new ProcessSingleton();

		return _instance;
	}
	private ProcessSingleton() { }
}


// per wątek
public sealed class ThreadSingleton
{
	[ThreadStatic]
	private static ThreadSingleton? _instance;

	public static ThreadSingleton GetInstance()
	{
		if (_instance == null)
			_instance = new ThreadSingleton();

		return _instance;
	}

	private ThreadSingleton() { }
}



// 5 sekund
public sealed class TimedSingleton
{
	private static TimedSingleton? _instance;
	private static DateTime? _expirationTime;

	public static TimedSingleton GetInstance()
	{
		if (_instance == null || DateTime.UtcNow > _expirationTime)
		{
			_instance = new TimedSingleton();
			_expirationTime = DateTime.UtcNow.AddSeconds(5);
		}
		return _instance;
	}

	private TimedSingleton() { }
}

class Program
{
	static void Main(string[] args)
	{
		Console.WriteLine("aaa");
	}
}