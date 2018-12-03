from scores.scores.scores_api import ScoresApi # Change to scores.score_api after figuring out how to install package locally.
import sys


def print_list_students(api):
    results = api.list_students()
    if len(results) == 0:
        print("No results!")
    else:
        print_list_results(results)


def print_list_exams(api):
    results = api.list_exams()
    if len(results) == 0:
        print("No results!")
    else:
        print_list_results(results)


def print_list_avg_student(api, sid):
    result_tup = api.student_results_and_average(sid)
    if len(result_tup[0]) == 0:
        print("No results!")
    if result_tup[1] == -1.0:
        print("No average!")
    if len(result_tup[0]) > 0 and result_tup[1] > -1.0:
        print_avg_tuple_results(result_tup)


def print_list_avg_exams(api, eid):
    result_tup = api.exam_results_and_average(eid)
    if len(result_tup[0]) == 0:
        print("No results!")
    if result_tup[1] == -1.0:
        print("No average!")
    if len(result_tup[0]) > 0 and result_tup[1] > -1.0:
        print_avg_tuple_results(result_tup)


def print_list_results(results):
    for res in results:
        print(res)


def print_avg_tuple_results(results):
    if isinstance(results[0], list) and isinstance(results[1], float):
        for res in results[0]:
            print(res)
        print("Average score: " + str(results[1]))


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

    api = ScoresApi()

    if len(argv) > 1:
        if argv[1] == "start":
            print("Starting data collection...")
            api.start()
            print("Data collection started.")
    
    cli_commands_message() # Prints out command options.

    prompt_user = True
    while prompt_user:
        user_input = input("\nPlease enter a command: ")
        print("")
        if user_input == "list":
            cli_list_options_message() # Prints out options for list command.
            sub_user_input = input("Choose what to list: ")
            if sub_user_input == "students":
                print_list_students(api)
            elif sub_user_input == "exams":
                print_list_exams(api)
            elif "student" in sub_user_input:
                student_id = sub_user_input.split()[-1]
                print(student_id)
                print_list_avg_student(api, student_id)
            elif "exam" in sub_user_input:
                exam_id = sub_user_input.split()[-1]
                print(exam_id)
                print_list_avg_exams(api, exam_id)
            elif sub_user_input == "cancel":
                cli_commands_message()
            else:
                print("Not a valid option!")
        elif user_input == "list students":
            print_list_students(api)
        elif user_input == "list exams":
            print_list_exams(api)
        elif "list student" in user_input:
            student_id = user_input.split()[-1]
            print_list_avg_student(api, student_id)
        elif "list exam" in user_input:
            exam_id = user_input.split()[-1]
            print_list_avg_exams(api, exam_id)
        elif user_input == "start":
            print("Starting data collection...")
            api.start()
            print("Data collection started.")
        elif user_input == "stop":
            print("Stopping data collection...")
            api.stop()
            print("Data collection stopped.")
        elif user_input == "menu":
            print("menu")
            cli_commands_message()
        elif user_input == "quit":
            print("Quitting")
            api.stop()
            prompt_user = False
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    main(sys.argv)
