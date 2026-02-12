using System;
using System.Collections.Generic;

public class Person { public override string ToString() => "Pracownik"; }

public interface IDataSource
{
    List<Person> GetPersons();
}

public class ListDataSource : IDataSource
{
    public List<Person> GetPersons()
    {
        return new List<Person>()
        {
            new Person(),
            new Person(),
            new Person()
        };
    }
}

public class XmlDataSource : IDataSource
{
    public List<Person> GetPersons()
    {
        Console.WriteLine("Loading XML data...");
        return new List<Person>();
    }
}

public abstract class PersonRegistry
{
    protected readonly IDataSource _dataSource;

    public PersonRegistry(IDataSource dataSource)
    {
        _dataSource = dataSource ?? throw new ArgumentNullException(nameof(dataSource));
    }

    public List<Person> GetPersons()
    {
        return _dataSource.GetPersons();
    }

    public abstract void NotifyPersons();
}

public class ConsoleNotifierRegistry : PersonRegistry
{
    public ConsoleNotifierRegistry(IDataSource dataSource) : base(dataSource) { }

    public override void NotifyPersons()
    {
        Console.WriteLine("Notification through console:");
        foreach (Person person in GetPersons())
        {
            Console.WriteLine(person);
        }
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        PersonRegistry registry1 = new ConsoleNotifierRegistry(new ListDataSource());
        registry1.NotifyPersons();
    }
}
