using System;
using System.Threading;
using System.Diagnostics;

public interface IService
{
    string Execute(string input);
}

public class RealService : IService
{
    private readonly Random _random = new Random();

    public string Execute(string input)
    {
        Console.WriteLine($"RealService: Exeecuting with input: '{input}'");

        if (_random.Next(10) < 3)
        {
            Console.WriteLine("RealService: Operation ended with no success");
            throw new InvalidOperationException("Sth went wrong :(");
        }

        return $"RealService replies for input: {input}";
    }
}

public class RetryProxy : IService
{
    private readonly IService _realService;
    private readonly int _maxRetries;
    private readonly int _retryDelayMs;

    public RetryProxy(IService realService, int maxRetries = 3, int retryDelayMs = 100)
    {
        _realService = realService ?? throw new ArgumentNullException(nameof(realService));
        _maxRetries = maxRetries;
        _retryDelayMs = retryDelayMs;
    }

    public string Execute(string input)
    {
        int retryCount = 0;
        while (retryCount < _maxRetries)
        {
            try
            {
                return _realService.Execute(input);
            }
            catch (Exception ex)
            {
                retryCount++;
                Console.WriteLine($"RetryProxy: Execution didnt succeeded (try {retryCount}/{_maxRetries}). Error: {ex.Message}. Repet after {_retryDelayMs}ms...");
                Thread.Sleep(_retryDelayMs);
            }
        }
        Console.WriteLine("RetryProxy: Maximum number of tries has been reached.");
        throw new AggregateException($"Maximum number of tries has been reached ({_maxRetries}).", new[] { new Exception("Last execution try didnt succeed") });
    }
}


public class LoggingProxy : IService
{
    private readonly IService _realService;

    public LoggingProxy(IService realService)
    {
        _realService = realService ?? throw new ArgumentNullException(nameof(realService));
    }

    public string Execute(string input)
    {
        var stopwatch = Stopwatch.StartNew();
        Console.WriteLine($"LoggingProxy: Execute method call with input: '{input}' on {DateTime.Now}.");
        string result = default;
        Exception exception = null;
        try
        {
            result = _realService.Execute(input);
            return result;
        }
        catch (Exception ex)
        {
            exception = ex;
            throw;
        }
        finally
        {
            stopwatch.Stop();
            if (exception == null)
            {
                Console.WriteLine($"LoggingProxy: Execute method ended with success on {DateTime.Now}. Execution time: {stopwatch.ElapsedMilliseconds}ms. Returned: '{result}'.");
            }
            else
            {
                Console.WriteLine($"LoggingProxy: Execute method ended with failer on {DateTime.Now}. Execution time: {stopwatch.ElapsedMilliseconds}ms. Exception: {exception.Message}.");
            }
        }
    }
}

public class ServiceFactory
{
    public static IService CreateServiceWithRetry(int maxRetries = 3, int retryDelayMs = 100)
    {
        return new RetryProxy(new RealService(), maxRetries, retryDelayMs);
    }

    public static IService CreateServiceWithLogging()
    {
        return new LoggingProxy(new RealService());
    }

    public static IService CreateServiceWithRetryAndLogging(int maxRetries = 3, int retryDelayMs = 100)
    {
        return new LoggingProxy(new RetryProxy(new RealService(), maxRetries, retryDelayMs));
    }

    public static IService CreateRealService()
    {
        return new RealService();
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("RetryProxy:");
        IService retryService = ServiceFactory.CreateServiceWithRetry();
        try
        {
            Console.WriteLine($"Result: {retryService.Execute("input for Retry")}");
        }
        catch (AggregateException ex)
        {
            Console.WriteLine($"Error occurred: {ex.InnerExceptions[0].Message}");
        }

        Console.WriteLine("\nLoggingProxy:");
        IService loggingService = ServiceFactory.CreateServiceWithLogging();
        try
        {
            Console.WriteLine($"Result: {loggingService.Execute("input for Logging")}");
        }
        catch (InvalidOperationException ex)
        {
            Console.WriteLine($"Error occurred: {ex.Message}");
        }

        Console.WriteLine("\nLoggingProxy with RetryProxy:");
        IService combinedService = ServiceFactory.CreateServiceWithRetryAndLogging(2, 500);
        try
        {
            Console.WriteLine($"Result: {combinedService.Execute("input for Doubble")}");
        }
        catch (AggregateException ex)
        {
            Console.WriteLine($"Error occurred: {ex.InnerExceptions[0].Message}");
        }
    }
}
