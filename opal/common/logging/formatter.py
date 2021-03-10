class Formatter:

    MAX_FIELD_LEN = 25

    def __init__(self):
        self.fmt = "<green>{time}</green> |<blue>{name: <30}|{function: ^20}:{line: <3}</blue>|<level>{level:^6} | {message}</level>\n"

    def limit_len(self, record, field, length=MAX_FIELD_LEN):
        #Shorten field content 
        content = record[field]
        if len(content) > length:
            parts = content.split(".")
            if len(parts) > 2:
                content = f"{parts[0]}...{parts[-1]}"
        if len(content) > length:   
            content = f"{content[:length-3]}..."
        record[field] = content

    def format(self, record):
        self.limit_len(record,"name",30)
        self.limit_len(record,"function",20)
        return self.fmt

