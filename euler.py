import task001
import task002
import task003
import task004
import task005
import task006
import task007
import task008
import task009
import task010
import task011
import task012
import task013
import task014
import task016
import task017
import task026

task = input("Which task do you want to solve? ")

match task:
    case '1':
         task001.solution()
    case '2':
         task002.solution()
    case '3':
         task003.solution()
    case '4':
         task004.solution()
    case '5':
         task005.solution()
    case '6':
         task006.solution()
    case '7':
         task007.solution()
    case '8':
         task008.solution()
    case '9':
         task009.solution()
    case '10':
         task010.solution()
    case '11':
         task011.solution()
    case '12':
         task012.solution()
    case '13':
         task013.solution()
    case '14':
         task014.solution()
    case '16':
         task016.solution()
    case '17':
         task017.solution()
    case '26':
         task026.task026_output()
    case _:
        print(f"There is no task {task}!")
