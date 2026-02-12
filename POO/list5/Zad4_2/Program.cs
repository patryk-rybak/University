using System;
using System.Collections.Generic;

public class Person { public override string ToString() => "Pracownik"; }

public interface INotifier
{
    void Notify(Person person);
}

public class SmsNotifier : INotifier
{
    public void Notify(Person person)
    {
        Console.WriteLine($"Send SMS to: {person}");
    }
}

public abstract class PersonRegistry
{
    protected readonly INotifier _notifier;

    public PersonRegistry(INotifier notifier)
    {
        _notifier = notifier ?? throw new ArgumentNullException(nameof(notifier));
    }

    public abstract List<Person> GetPersons();

    public void NotifyPersons()
    {
        foreach (Person person in GetPersons())
        {
            _notifier.Notify(person);
        }
    }
}

public class DatabaseDataSourceRegistry : PersonRegistry
{
    public DatabaseDataSourceRegistry(INotifier notifier) : base(notifier) { }

    public override List<Person> GetPersons()
    {
        Console.WriteLine("Loading data from database...");
        return new List<Person>()
        {
            new Person(),
            new Person(),
            new Person()
        };
    }
}

public class BridgeExample2
{
    public static void Main(string[] args)
    {
        PersonRegistry registry2 = new DatabaseDataSourceRegistry(new SmsNotifier());
        registry2.NotifyPersons();
    }
}
