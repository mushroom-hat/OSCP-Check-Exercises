import docx2txt
import sys

def check_exercises(filename):
    exercises = [
        '2.4.3.4',
        '3.1.3.1',
        '3.2.5.1',
        '3.3.5.1',
        '3.5.3.1',
        '3.6.3.1',
        '3.7.2.1',
        '3.8.3.1',
        '3.9.3.1',
        '4.2.4.1',
        '4.3.8.1',
        '4.4.5.1',
        '4.5.2.1',
        '5.7.3.1',
        '6.3.1.1',
        '6.4.1.1',
        '6.5.1.1',
        '6.7.1.1',
        '6.12.1.1',
        '6.13.2.1',
        '7.1.6.3',
        '7.2.2.9',
        '7.3.2.1',
        '7.4.2.1',
        '7.5.1.1',
        '7.6.3.6',
        '8.2.4.1',
        '8.2.5.1',
        '8.2.6.1',
        '8.3.1.1',
        '9.3.3.1',
        '9.4.1.2',
        '9.4.2.5',
        '9.4.3.2',
        '9.4.4.5',
        '9.4.4.7',
        '9.4.4.10',
        '9.4.5.4',
        '9.4.5.9',
        '9.4.5.11',
        '9.4.5.13',
        '10.2.5',
        '11.1.1.1',
        '11.2.3.1',
        '11.2.5.1',
        '11.2.7.1',
        '11.2.9.1',
        '11.2.10.1',
        '12.2.1.1',
        '12.3.1.1',
        '12.5.1.1',
        '12.6.1.1',
        '12.7.1.1',
        '13.2.2.1',
        '13.3.2.1',
        '13.3.3.1',
        '13.3.4.1',
        '14.3.1.1',
        '15.1.3.1',
        '15.1.4.1',
        '15.1.5.1',
        '15.1.6.1',
        '15.1.7.1',
        '15.2.3.1',
        '15.2.4.1',
        '17.3.3.2',
        '17.3.3.4',
        '18.1.1.13',
        '18.1.2.1',
        '18.2.3.1',
        '18.2.4.1',
        '18.3.2.1',
        '18.3.3.1',
        '19.4.2.1',
        '20.1.1.1',
        '20.2.1.1',
        '20.2.2.1',
        '20.2.3.1',
        '20.3.1.1',
        '20.4.1.1',
        '20.5.1.1',
        '21.2.1.1',
        '21.2.2.1',
        '21.2.3.1',
        '21.2.4.1',
        '21.2.5.1',
        '21.3.3.1',
        '21.3.4.1',
        '21.3.5.1',
        '21.4.2.1',
        '21.4.3.1',
        '21.4.4.1',
        '21.5.1.1',
        '22.1.3.1',
        '22.2.1.1',
        '22.3.3.1',
        '22.3.7.1',
        '22.4.1.1',
        '22.5.4.1',
        '22.6.1.1',
        '23.1.3.1',
        '23.3.1.1',
        '24.2.2.1',
        '24.5.1.1',

    ]
    print(len(exercises))
    completed_exercise = []
    text = docx2txt.process(filename)

    # checks each line in the .docx file to see if the line contains the exercise number
    # if the line contains the exercise number, append it to another list called "completed_exercise"
    for line in text.splitlines():
        if line != '':
            for exercise in exercises:
                if exercise in line:
                    completed_exercise.append(exercise)

    # compares the PWK Exercise list with the "completed_exercise" list
    uncompleted_exercises = [ex for ex in exercises if ex not in completed_exercise]
    if uncompleted_exercises:
        print("[+] These exercises are in the PWK course but NOT in your report")
        for ex in uncompleted_exercises:
            print("Exercise {}".format(ex))
    else:
        print("[+] All exercises are included in both the PWK course and your report!")

def main(args):
    if args:
        filename = args[0]
        try:
            check_exercises(filename)
        except:
            print("Something went wrong! Check your input file path or file permissions.")
    else:
        print("File path is missing!")

if __name__ == '__main__':
    main(sys.argv[1:])
