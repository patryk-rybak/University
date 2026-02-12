using System;
using System.IO;

public interface ILogger
{
    void Log(string Message);
}

public enum LogType { None, Console, File }

public class ConsoleLogger : ILogger
{
    public void Log(string Message)
    {
        Console.WriteLine($"[Cmd] {DateTime.Now}: {Message}");
    }
}

public class FileLogger : ILogger
{
    private readonly string _filePath;

    public FileLogger(string filePath)
    {
        _filePath = filePath ?? throw new ArgumentNullException(nameof(filePath));
    }

    public void Log(string Message)
    {
        try
        {
            File.AppendAllText(_filePath, $"[File] {DateTime.Now}: {Message}{Environment.NewLine}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"[Error during file logging] {DateTime.Now}: Cannot write to file '{_filePath}'. Error: {ex.Message}");
        }
    }
}

public class NullLogger : ILogger
{
    public void Log(string Message)
    {

    }
}

public class LoggerFactory
{
    private static readonly Lazy<LoggerFactory> _instance = new Lazy<LoggerFactory>(() => new LoggerFactory());
    public static LoggerFactory Instance => _instance.Value;

    private LoggerFactory() { }

    public ILogger GetLogger(LogType logType, string parameters = null)
    {
        switch (logType)
        {
            case LogType.Console:
                return new ConsoleLogger();
            case LogType.File:
                if (string.IsNullOrEmpty(parameters))
                {
                    throw new ArgumentException("File path i needed for file logger.", nameof(parameters));
                }
                return new FileLogger(parameters);
            case LogType.None:
                return new NullLogger();
            default:
                throw new ArgumentException($"Unknown logger type: {logType}", nameof(logType));
        }
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        // file logger
        ILogger fileLogger = LoggerFactory.Instance.GetLogger(LogType.File, "log.txt");
        fileLogger.Log("file first log");
        fileLogger.Log("file second log");

        // null logger
        ILogger nullLogger = LoggerFactory.Instance.GetLogger(LogType.None);
        nullLogger.Log("null log message");

        // cmd logger
        ILogger consoleLogger = LoggerFactory.Instance.GetLogger(LogType.Console);
        consoleLogger.Log("cmd log message");
    }
}
