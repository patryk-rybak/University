from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET

# strategia przetwarzania danych
class DataProcessingStrategy(ABC):
    @abstractmethod
    def process(self, data):
        pass


class SumColumnStrategy(DataProcessingStrategy):
    def process(self, data):
        print("processing data")
        return sum(data)


class LongestXmlNodeStrategy(DataProcessingStrategy):
    def process(self, data):
        print("searching for node with longest name")
        root = data.getroot()
        longest = ""
        for item in root.findall('item'):
            name = item.attrib.get('name', '')
            if len(name) > len(longest):
                longest = name
        return longest


# handler kontekstowy - uuywa strategii
class DataAccessHandler:
    def __init__(self, strategy: DataProcessingStrategy):
        self.strategy = strategy

    def load_data(self):
        raise NotImplementedError

    def connect(self):
        pass

    def disconnect(self):
        pass

    def execute(self):
        self.connect()
        data = self.load_data()
        result = self.strategy.process(data)
        self.disconnect()
        return result


# implementacja dla bazy danych
class DatabaseDataAccessHandler(DataAccessHandler):
    def connect(self):
        print("connecting to database")

    def load_data(self):
        print("fetching data from database")
        return [100, 200, 300, 400]

    def disconnect(self):
        print("disconnecting from database")


# implementacja dla xml
class XmlDataAccessHandler(DataAccessHandler):
    def connect(self):
        print("opening XML file")

    def load_data(self):
        print("parsing XML content")
        xml_data = '''
        <root>
            <item name="aaa" />
            <item name="aaaaaaaaaaaaaaaaaaaaaaaaaaaa" />
            <item name="aaaaaaaaaa" />
        </root>
        '''
        return ET.ElementTree(ET.fromstring(xml_data))

    def disconnect(self):
        print("closing xml file")


if __name__ == "__main__":
    db_handler = DatabaseDataAccessHandler(strategy=SumColumnStrategy())
    result_db = db_handler.execute()
    print(f"Database result: {result_db}\n")

    xml_handler = XmlDataAccessHandler(strategy=LongestXmlNodeStrategy())
    result_xml = xml_handler.execute()
    print(f"XML result: {result_xml}")

