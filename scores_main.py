from scores.score_stream_thread import ScoreStreamThread
import sys

def main(argv):
    """print_lock = threading.Lock()
    def threadTest():
        # when this exits, the print_lock is released
        with print_lock:
            print(worker)

    def threader():
      while True:
        threadTest(q.get())
    """
    stream_thread = None
    if len(argv) > 1:
        if argv[1] == "start":
            stream_thread = ScoreStreamThread()
            stream_thread.daemon = True
            stream_thread.start()
    
    print("Welcome to Scores!")
    print("You may choose from the list of commands:")
    print("start : start collecting scores data.")
    print("stop : stop collecting scores data.")
    print("list students: lists all students that have received at least one test score.")
    print("list student <student_id> : lists the test results for the student specified by student_id and provides the student's average score across all exams.")
    print("list exams : lists all the exams that have been recorded.")
    print("list exam <exam_id> : lists all the results for the exam specified by exam_id and provides the average score across all students")
    print("exit : exit the program")
    while not stream_thread or not stream_thread.kill.is_set():
        user_input = input("Please enter a command: ")
        if user_input == "list":
            print("Here's what you can list:")
            print("students: lists all students that have received at least one test score.")
            print("student <student_id> : lists the test results for the student specified by student_id and provides the student's average score across all exams.")
            print("exams : lists all the exams that have been recorded.")
            print("exam <exam_id> : lists all the results for the exam specified by exam_id and provides the average score across all students")
            sub_user_input = input("Choose what to list: ")
            if sub_user_input == "students":
                pass
            elif sub_user_input == "exams":
                pass
            elif "student" in sub_user_input:
                pass
            elif "exam" in sub_user_input:
                pass
            else:
                print("Not valid option!")
                pass
            
        elif user_input == "start":
            print("started")
            pass
        elif user_input == "stop":
            print("stopped")
            quit()
        else:
            pass

if __name__ == "__main__":
    main(sys.argv)