import VoiceCommands as vc
import ManageQuery as mq

  


if __name__ == "__main__":
    mq.wishMe()
    vc.speak("To setup, Enter 0 for chat commands Or 1 for voice commands")
    print("To setup, Enter 0 for chat commands Or 1 for voice commands")
    
    choice=int(input("Enter your choice: "))
    while True:
        if(choice==0):
            query=input("Enter your command: ")
            mq.proccesQuery(query.lower(),choice)
        elif(choice==1):
            query=vc.takeCommand()
            mq.proccesQuery(query.lower(),choice)
        else:
            print("Invalid Choice")
            vc.speak("Invalid Choice")
            choice=input("Enter choice again:")

        