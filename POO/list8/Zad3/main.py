from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET

class DataAccessHandler(ABC):
    def execute(self):
        self.connect()
        data = self.get_data()
        result = self.process_data(data)
        self.disconnect()
        return result

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def process_data(self, data):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class DatabaseDataAccessHandler(DataAccessHandler):
    def connect(self):
        print("connecting to database")

    def get_data(self):
        print("fetching data from database")
        return [100, 200, 300, 400]

    def process_data(self, data):
        print("processing data")
        return sum(data)

    def disconnect(self):
        print("disconnecting from database")


class XmlDataAccessHandler(DataAccessHandler):
    def connect(self):
        print("opening xml file")

    def get_data(self):
        print("parsing xml content")
        xml_data = '''
        <root>
            <item name="aaaaaa" />
            <item name="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" />
            <item name="aaaaaaaaaaaa" />
        </root>
        '''
        tree = ET.ElementTree(ET.fromstring(xml_data))
        return tree

    def process_data(self, data):
        print("searching for node with longest name")
        root = data.getroot()
        longest = ""
        for item in root.findall('item'):
            name = item.attrib.get('name', '')
            if len(name) > len(longest):
                longest = name
        return longest

    def disconnect(self):
        print("closing xml file")


# Przykładowe użycie
if __name__ == "__main__":
    db_handler = DatabaseDataAccessHandler()
    db_result = db_handler.execute()
    print(f"database result: {db_result}\n")

    xml_handler = XmlDataAccessHandler()
    xml_result = xml_handler.execute()
    print(f"xml result: {xml_result}")

