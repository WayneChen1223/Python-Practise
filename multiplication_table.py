def print_multiplication_table(displayTo, displayRowTo):
    displayCount = displayTo//displayRowTo 
    if (displayTo % displayRowTo) > 0:
        displayCount += 1
    start_number = 1
    end_number = displayTo
    break_point = displayRowTo
    while(displayCount > 0):
        for column in range(1,10):
            row_content = ""
            for row in range(start_number, (end_number + 1)):
                new_content = str(row) + " * " + str(column) + " = " + str(row * column) + "\t"
                row_content = row_content + new_content
                if row == break_point:
                    break
            print(row_content)
        print()
        start_number += displayRowTo
        break_point += displayRowTo
        displayCount -= 1

def export_multiplication_table(displayTo, displayRowTo, fileName):
    displayCount = displayTo//displayRowTo
    if (displayTo % displayRowTo) > 0:
        displayCount += 1
    start_number = 1
    end_number = displayTo
    break_point = displayRowTo
    with open(fileName + ".txt", "w") as multi_table:
        while(displayCount > 0):
            for column in range(1,10):
                row_content = ""
                for row in range(start_number, (end_number + 1)):
                    new_content = str(row) + " * " + str(column) + " = " + str(row * column) + "\t"
                    row_content = row_content + new_content
                    if row == break_point:
                        break
                multi_table.write(row_content)
                multi_table.write("\n")
            multi_table.write("\n")
            start_number += displayRowTo
            break_point += displayRowTo
            displayCount -= 1