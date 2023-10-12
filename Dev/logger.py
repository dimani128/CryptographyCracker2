
class Logger:
    def __init__(self, logFile):
        # clear the file, then open in append mode
        self.logfile = open(logFile, 'w') if isinstance(logFile, str) else logFile
        self.logfile.close()
        self.logfile = open(logFile, 'a') if isinstance(logFile, str) else logFile

        import signal
        import atexit

        atexit.register(self.handle_exit)
        signal.signal(signal.SIGTERM, self.handle_exit)
        signal.signal(signal.SIGINT, self.handle_exit)

    def formatText(self, text):
        # Create a string with self.dateTime left-justified
        formatted_text = self.dateTime().ljust(30) + text.split('\n')[0] + '\n'

        # Split the text into lines and add 30 spaces before each line
        lines = text.split('\n')
        for line in lines[1:]:
            formatted_text += ' ' * 30 + line + '\n'

        return formatted_text

    def log(self, text):
        text = self.formatText(text)
        self.logfile.write(text)
    
    def handle_exit(self):
        self.log('Exiting tasks:\n\tClose File')
        self.logfile.close()

    def dateTime(self):
        import datetime
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime('%y/%m/%d %H:%M:%S.%f')[:-3]
        return formatted_time