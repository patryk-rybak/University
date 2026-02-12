class MessageType:
    PRAISE = 1
    COMPLAINT = 2
    ORDER = 3
    OTHER = 4
    WRONG = 5


class Message:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class Request:
    def __init__(self, message):
        self.message = message
        self.message_type = None


class TypeCounter:
    counts = {
        MessageType.PRAISE: 0,
        MessageType.COMPLAINT: 0,
        MessageType.ORDER: 0,
        MessageType.OTHER: 0,
        MessageType.WRONG: 0,
    }

    @classmethod
    def increment_count(cls, message_type):
        cls.counts[message_type] += 1

    @classmethod
    def get_counts(cls):
        return cls.counts


class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            return self.successor.handle_request(request)
        return None


class Classifier(Handler):
    indicators = {
        "praise": ["praise", "compliment", "positive feedback", "good job"],
        "complaint": ["complaint", "issue", "problem", "concern"],
        "order": ["order", "purchase", "buy", "transaction"]
    }

    def indicate(self, message_type, message_parts):
        if message_type not in self.indicators:
            raise Exception("message type doesn't exist")
        type_indicators = self.indicators[message_type]
        for part in message_parts:
            for indicator in type_indicators:
                if indicator in part:
                    return True
        return False

    def handle_request(self, request):
        message_parts = [request.message["title"], request.message["content"]]
        if self.indicate("praise", message_parts):
            request.message_type = MessageType.PRAISE
        elif self.indicate("complaint", message_parts):
            request.message_type = MessageType.COMPLAINT
        elif self.indicate("order", message_parts):
            request.message_type = MessageType.ORDER
        else:
            request.message_type = MessageType.OTHER

        if not request.message["title"].strip() or not request.message["content"].strip():
            request.message_type = MessageType.WRONG

        return super().handle_request(request)


class PraiseHandler(Handler):
    def handle_request(self, request):
        if request.message_type == MessageType.PRAISE:
            TypeCounter.increment_count(MessageType.PRAISE)

        return super().handle_request(request)


class ComplaintHandler(Handler):
    def handle_request(self, request):
        if request.message_type == MessageType.COMPLAINT:
            TypeCounter.increment_count(MessageType.COMPLAINT)

        return super().handle_request(request)


class OrderHandler(Handler):
    def handle_request(self, request):
        if request.message_type == MessageType.ORDER:
            TypeCounter.increment_count(MessageType.ORDER)

        return super().handle_request(request)


class OtherHandler(Handler):
    def handle_request(self, request):
        if request.message_type == MessageType.OTHER:
            TypeCounter.increment_count(MessageType.OTHER)

        return super().handle_request(request)


class WrongHandler(Handler):
    def handle_request(self, request):
        if request.message_type == MessageType.WRONG:
            TypeCounter.increment_count(MessageType.WRONG)

        return super().handle_request(request)


class ArchiveHandler(Handler):
    def __init__(self, successor=None):
        super().__init__(successor)

    def handle_request(self, request):
        super().handle_request(request)

        with open("archive.txt", "a") as file:
            file.write(f"Title: {request.message['title']}\n [{request.message_type}]")
            file.write(f"Content: {request.message['content']}\n\n")


classifier = Classifier()
praise_handler = PraiseHandler()
complaint_handler = ComplaintHandler()
order_handler = OrderHandler()
other_handler = OtherHandler()
wrong_handler = WrongHandler()
archive_handler = ArchiveHandler()

classifier.successor = praise_handler
praise_handler.successor = complaint_handler
complaint_handler.successor = order_handler
order_handler.successor = other_handler
other_handler.successor = wrong_handler
wrong_handler.successor = archive_handler

message1 = Request(message={"title": "woow", "content": "this employee did a really good job"})
message2 = Request(message={"title": "compliant", "content": "i've had an issue"})
message3 = Request(message={"title": "order", "content": "i'd like to buy a thing"})
message4 = Request(message={"title": "question", "content": "can i get a discount"})
message5 = Request(message={"title": "", "content": ""})
message6 = Request(message={"title": "concering behaviour", "content": ""})

classifier.handle_request(message1)
classifier.handle_request(message2)
classifier.handle_request(message3)
classifier.handle_request(message4)
classifier.handle_request(message5)
classifier.handle_request(message6)

print(TypeCounter.get_counts())
