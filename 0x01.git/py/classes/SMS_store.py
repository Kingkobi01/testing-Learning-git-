class SMS_store:
    def __init__(self, messages: list = []) -> None:
        self.messages = messages

    def add_new_arrival(self, from_number: str, time_arrived: str, text_of_SMS: str):
        has_been_viewed = False
        new_message = (has_been_viewed, from_number, time_arrived, text_of_SMS)
        self.messages.append(new_message)

    def message_count(self):
        return len(self.messages)

    def get_unread_indexes(self):
        return [
            self.messages.index(message)
            for message in self.messages
            if message[0] == False
        ]

    def get_message(self, i):
        if len(self.messages) > i:
            selected_message = self.messages[i]
            list_selected_message = list(selected_message)
            list_selected_message[0] = True
            modified_message = tuple(list_selected_message)
            self.messages[i] = modified_message
            return modified_message
        else:
            return None

    def delete(self, i) -> None:
        try:
            selected_message = self.messages[i]
            self.messages.remove(selected_message)
        except len(self.messages) <= i:
            print(f"There is not any message with an index of {i}")

    def clear(self):
        self.messages.clear()


my_inbox = SMS_store()

my_inbox.add_new_arrival("0231456789", "11:45pm", "Killer, ma memfiili wo")
my_inbox.add_new_arrival("0124356489", "08:451m", "Hey, killer wadware?")


assert len(my_inbox.get_unread_indexes()) == 2

assert my_inbox.get_message(0)

assert len(my_inbox.get_unread_indexes()) == 1

my_inbox.clear()

assert my_inbox.message_count() == 0


## Please try your hands with the testings
