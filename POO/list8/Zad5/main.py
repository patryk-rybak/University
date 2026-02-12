from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, machine):
        self.machine = machine

    @abstractmethod
    def insert_coin(self):
        pass

    @abstractmethod
    def select_coffee(self):
        pass

    @abstractmethod
    def dispense(self):
        pass


class IdleState(State):
    def insert_coin(self):
        print("Coin inserted.")
        self.machine.set_state(self.machine.has_money_state)

    def select_coffee(self):
        print("Insert coin first.")

    def dispense(self):
        print("Nothing to dispense.")


class HasMoneyState(State):
    def insert_coin(self):
        print("Coin already inserted.")

    def select_coffee(self):
        print("Brewing coffee...")
        self.machine.set_state(self.machine.brewing_state)

    def dispense(self):
        print("Select coffee first.")


class BrewingState(State):
    def insert_coin(self):
        print("Brewing in progress.")

    def select_coffee(self):
        print("Already brewing.")

    def dispense(self):
        print("Dispensing coffee...")
        self.machine.set_state(self.machine.dispensing_state)


class DispensingState(State):
    def insert_coin(self):
        print("Wait, dispensing...")

    def select_coffee(self):
        print("Wait, dispensing...")

    def dispense(self):
        print("Coffee served! Returning to idle.")
        self.machine.set_state(self.machine.idle_state)


class OutOfServiceState(State):
    def insert_coin(self):
        print("Out of service.")

    def select_coffee(self):
        print("Out of service.")

    def dispense(self):
        print("Out of service.")


# kontestk
class CoffeeMachine:
    def __init__(self):
        self.idle_state = IdleState(self)
        self.has_money_state = HasMoneyState(self)
        self.brewing_state = BrewingState(self)
        self.dispensing_state = DispensingState(self)
        self.out_of_service_state = OutOfServiceState(self)

        self.state = self.idle_state

    def set_state(self, state):
        self.state = state

    # delegacja do aktualnego stanu
    def insert_coin(self):
        self.state.insert_coin()

    def select_coffee(self):
        self.state.select_coffee()

    def dispense(self):
        self.state.dispense()


if __name__ == "__main__":
    machine = CoffeeMachine()

    machine.insert_coin()      
    machine.select_coffee()    
    machine.dispense()         

    # zla kolejnosc
    machine.select_coffee()    
    machine.dispense()         
    machine.insert_coin()      
    machine.insert_coin()      
    machine.select_coffee()    
    machine.dispense()         

