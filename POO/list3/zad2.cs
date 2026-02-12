public class DataFetcher
{
    public string GetData()
        return "data";
}

public class Formatter
{
    public string Format(string data)
        return $"sformatowane {data}";
}

public class Printer
{
    public void Print(string data)
        Console.WriteLine(data);
}

public class ReportPrinter
{
    private readonly DataFetcher _fetcher;
    private readonly Formatter _formatter;
    private readonly Printer _printer;

    public ReportPrinter(DataFetcher fetcher, Formatter formatter, Printer printer)
    {
        _fetcher = fetcher;
        _formatter = formatter;
        _printer = printer;
    }

    public void PrintReport()
    {
        string data = _fetcher.GetData();
        string formattedReport = _formatter.Format(data);
        _printer.Print(formattedReport);
    }
}

// kazda klasa ma teraz jedna odpowiedizalnosc - np. ja zmieni sie formatowanie dokumemtow to zmainie ulegnie jedynie Formatter a nie cały RaportPrinter
