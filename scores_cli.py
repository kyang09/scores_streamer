from scores.scores.scores_api import ScoresApi # Change to scores.score_api after figuring out how to install package locally.
import sys

def main(argv):
    def cli_commands_message():
        print("\nWelcome to Scores!")
        print("You may choose from the list of commands:")
        print("-----------------------------------------")
        print("start : Start collecting scores data.")
        print("stop : Stop collecting scores data.")
        print("list students : Lists all students that have received at least one test score.")
        print("list student <student_id> : Lists the test results for the student specified by student_id and provides the student's average score across all exams.")
        print("list exams : Lists all the exams that have been recorded.")
        print("list exam <exam_id> : Lists all the results for the exam specified by exam_id and provides the average score across all students.")
        print("menu : Show the commands menu.")
        print("quit : Exit the program.")
        print("-----------------------------------------\n")

    def cli_list_options_message():
        print("\nHere's what you can list:")
        print("-----------------------------------------")
        print("students : Lists all students that have received at least one test score.")
        print("student <student_id> : Lists the test results for the student specified by student_id and provides the student's average score across all exams.")
        print("exams : Lists all the exams that have been recorded.")
        print("exam <exam_id> : Lists all the results for the exam specified by exam_id and provides the average score across all students.")
        print("cancel : Go back to the main commands menu.")
        print("-----------------------------------------\n")

    stream_thread = None
    api = ScoresApi()

    if len(argv) > 1:
        if argv[1] == "start":
            print("started")
            api.start()
    
    cli_commands_message() # Prints out command options.

    while not stream_thread or not stream_thread.kill.is_set():
        user_input = input("Please enter a command: ")
        if user_input == "list":
            cli_list_options_message() # Prints out options for list command.
            sub_user_input = input("Choose what to list: ")
            if sub_user_input == "students":
                print("list students")
                api.list_students()
            elif sub_user_input == "exams":
                print("exams")
                api.list_exams()
            elif "student" in sub_user_input:
                print("student results")
                student_id = 0 # Replace with actual student id from input.
                api.student_results_and_average(student_id)
            elif "exam" in sub_user_input:
                print("exam results")
                exam_id = 0 # Replace with actual exam id from input.
                api.exam_results_and_average(exam_id)
            elif sub_user_input == "cancel":
                print("cancelled")
                cli_commands_message()
            else:
                print("Not a valid option!")
        elif user_input == "list students":
            print("list students")
            print(api.list_students())
        elif user_input == "list exams":
            print("exams")
            api.list_exams()
        elif "list student" in user_input:
            print("student results")
            student_id = 0 # Replace with actual student id from input.
            api.student_results_and_average(student_id)
        elif "list exam" in user_input:
            print("exam results")
            exam_id = 0 # Replace with actual exam id from input.
            api.exam_results_and_average(exam_id)
        elif user_input == "start":
            print("starting")
            api.start()
        elif user_input == "stop":
            print("stopping")
            api.stop()
        elif user_input == "menu":
            print("menu")
            cli_commands_message()
        elif user_input == "quit":
            print("quitting and stopping")
            api.stop() # Since we made our thread a daemon (to main thread), we may not need to call stop() here.
            quit()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main(sys.argv)