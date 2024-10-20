import task001
import task002
import task003
import task004
import task005
import task026

task = input("Which task do you want to solve? ")

match task:
    case '1':
         task001.task001_output()
    case '2':
         task002.task002_output()
    case '3':
         task003.task003_output()
    case '4':
         task004.task004_output()
    case '5':
         task005.task005_output()
    case '26':
         task026.task026_output()
    case _:
        print(f"There is no task {task}!")
