from pathlib import Path
import ezgmail
from ezgmail import GmailThread, GmailMessage

# print(Path.cwd())
ezgmail.send(
    "shahzaib84.sk@gmail.com", "First Time From Python Code", "AOA Is this Working"
)

udread_thread: GmailMessage = ezgmail.search("umair")
# print(udread_thread)
# ezgmail.summary(udread_thread[0])
print(udread_thread[0].messages[0].subject)
print(udread_thread[0].messages[0].body)
print(udread_thread[0].messages[0].timestamp)
print(udread_thread[0].messages[0].sender)
print(udread_thread[0].messages[0].recipient)
print(udread_thread[0].messages[8].attachments)
udread_thread[0].messages[8].downloadAttachment("Untitled.wma")
