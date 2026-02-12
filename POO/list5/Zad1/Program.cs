using System;
using System.IO;
using System.Net;
using System.Net.Mail;

public class SmtpFacade
{
    public void Send(string From, string To, string Subject, string Body, Stream Attachment, string AttachmentMimeType)
    {
        string appPasswd = File.ReadAllText(@"/home/patryk/Documents/apppasswd").Trim();

        using (var message = new MailMessage(From, To, Subject, Body))
        {
            if (Attachment != null)
            {
                var attachment = new Attachment(Attachment, "attachment", AttachmentMimeType);
                message.Attachments.Add(attachment);
            }

            using (var client = new SmtpClient("smtp.gmail.com", 587))
            {
                client.EnableSsl = true;
                client.Credentials = new NetworkCredential("patrykrybak2@gmail.com", appPasswd);
                client.Send(message);
            }
        }
    }
}

class Program
{
    static void Main()
    {
        var facade = new SmtpFacade();

        // it is seen as byte stream for attachment contetn
        string attachmentText = "attachment content";
        MemoryStream attachmentStream = new MemoryStream(System.Text.Encoding.UTF8.GetBytes(attachmentText));

        try
        {
            facade.Send(
                From: "patrykrybak2@gmail.com",
                To: "patrykrybak6@gmail.com",
                Subject: "topic",
                Body: "content",
                Attachment: attachmentStream,
                AttachmentMimeType: "text/plain"
            );

            Console.WriteLine("Message is send.");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Sth went wrong:" + ex.Message);
        }
    }
}

