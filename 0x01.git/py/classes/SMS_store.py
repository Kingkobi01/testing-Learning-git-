class SMS_store:
    def __init__(self, messages: list=[]) -> None:
        self.messages = messages

    def add_new_arrival(self, from_number:str, time_arrived:str, text_of_SMS:str):
        has_been_viewed = False
        new_message = (has_been_viewed, from_number, time_arrived, text_of_SMS)
        self.messages.append(new_message)

    

    def message_count(self):
        return len(self.messages)
    
    def get_unread_indexes(self):
        return [message.index() for message in self.messages if message[0] == False]


    def get_message(self, i):
        if len(self.messages) > i:
            selected_message =   self.messages[i]
            selected_message[0] = True
            return selected_message 
        else:
            return None    
        

   
    def delete(self,i)-> None:
        try:
            selected_message =   self.messages[i]
            self.messages.remove(selected_message)
        except len(self.messages <= i):
            print(f"There is not any message with an index of {i}")
    
    def clear(self):
        self.messages.clear()



my_inbox = SMS_store()

my_inbox.add_new_arrival("0231456789", "11:45pm", "Killer, ma memfiili wo")
my_inbox.message_count()
my_inbox.get_unread_indexes()
my_inbox.get_message(0)
