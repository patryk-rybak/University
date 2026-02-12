using System;
using System.IO;
using System.Text;

public class CaesarStream : Stream
{
    private readonly Stream _baseStream;
    private readonly int _shift;

    public CaesarStream(Stream baseStream, int shift)
    {
        _baseStream = baseStream;
        _shift = shift;
    }

    public override void Write(byte[] buffer, int offset, int count)
    {
        byte[] encrypted = new byte[count];
        for (int i = 0; i < count; i++)
        {
            encrypted[i] = (byte)((buffer[offset + i] + _shift) % 256);
        }
        _baseStream.Write(encrypted, 0, count);
    }

    public override int Read(byte[] buffer, int offset, int count)
    {
        byte[] tempBuffer = new byte[count];
        int bytesRead = _baseStream.Read(tempBuffer, 0, count);

        for (int i = 0; i < bytesRead; i++)
        {
            buffer[offset + i] = (byte)((tempBuffer[i] - _shift + 256) % 256);
        }

        return bytesRead;
    }

    public override bool CanRead => _baseStream.CanRead;
    public override bool CanSeek => _baseStream.CanSeek;
    public override bool CanWrite => _baseStream.CanWrite;
    public override long Length => _baseStream.Length;

    public override long Position
    {
        get => _baseStream.Position;
        set => _baseStream.Position = value;
    }

    public override void Flush() => _baseStream.Flush();

    public override long Seek(long offset, SeekOrigin origin) =>
        _baseStream.Seek(offset, origin);

    public override void SetLength(long value) =>
        _baseStream.SetLength(value);
}


class Program
{
    static void Main()
    {
        string filePath = "cezar_bytes.bin";
        string tekst = "abcd";
        byte[] dane = Encoding.UTF8.GetBytes(tekst);

        FileStream fileToWrite = File.Create(filePath);
        CaesarStream caeToWrite = new CaesarStream(fileToWrite, 5);
        caeToWrite.Write(dane, 0, dane.Length);

        caeToWrite.Flush();
        caeToWrite.Close();
        fileToWrite.Close();

        FileStream fileToRead = File.Open(filePath, FileMode.Open);
        CaesarStream caeToRead = new CaesarStream(fileToRead, 5);
        byte[] bufor = new byte[dane.Length];
        int ilosc = caeToRead.Read(bufor, 0, bufor.Length);

        caeToRead.Close();
        fileToRead.Close();

        string decoded = Encoding.UTF8.GetString(bufor, 0, ilosc);
        Console.WriteLine("read: " + decoded);
    }
}

