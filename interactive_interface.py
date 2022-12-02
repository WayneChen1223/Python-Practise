from multiplication_table import print_multiplication_table, export_multiplication_table

def interactive_interface():
    command = ""
    while(command != "exit"):
        command = input(" 請輸入指令(輸入help, 顯示可用指令)$ ")
        if command == "help":
            display_command_option()
        else:
            if command == "exit":
                continue
            command_options = command.split(" ")
            if command_options[0] == "multi-table":
                execute_options(command_options[1:])
            else:
                print(f"\n 指令錯誤! 您輸入的是{command_options[0]}, 請重新輸入。\n")
    print("\n 程式結束。")

def execute_options(command_options):
    if ("--displayTo" in command_options) and not("--displayRowTo" in command_options):
        option_index_of_display_to = command_options.index("--displayTo")
        setting_value_of_display_to = command_options[(option_index_of_display_to + 1)]
        if (setting_value_of_display_to.isdigit() and (int(setting_value_of_display_to) > 0)):
            if ("--export" in command_options):
                option_index_of_export = command_options.index("--export")
                fileName = command_options[(option_index_of_export + 1)]
                export_multiplication_table(int(setting_value_of_display_to), 3, fileName)
            else:
                print_multiplication_table(int(setting_value_of_display_to), 3)
        else:
            print("\n 指令錯誤! --displayTo 設定值應為正整數。\n")
    elif not("--displayTo" in command_options) and ("--displayRowTo" in command_options):
        option_index_of_display_row_to = command_options.index("--displayRowTo")
        setting_value_of_display_row_to = command_options[(option_index_of_display_row_to + 1)]
        if (setting_value_of_display_row_to.isdigit() and (int(setting_value_of_display_row_to) > 0)):
            if ("--export" in command_options):
                option_index_of_export = command_options.index("--export")
                fileName = command_options[(option_index_of_export + 1)]
                export_multiplication_table(9, int(setting_value_of_display_row_to), fileName)
            else:
                print_multiplication_table(9, int(setting_value_of_display_row_to))
        else:
            print("\n 指令錯誤! --displayRowTo 設定值應為正整數。\n")
    elif ("--displayTo" in command_options) and ("--displayRowTo" in command_options):
        option_index_of_display_to = command_options.index("--displayTo")
        option_index_of_display_row_to = command_options.index("--displayRowTo")
        setting_value_of_display_to = command_options[(option_index_of_display_to + 1)]
        setting_value_of_display_row_to = command_options[(option_index_of_display_row_to + 1)]
        if (setting_value_of_display_to.isdigit() and (int(setting_value_of_display_to) > 0)):
            if (setting_value_of_display_row_to.isdigit() and (int(setting_value_of_display_row_to) > 0)):
                if ("--export" in command_options):
                    option_index_of_export = command_options.index("--export")
                    fileName = command_options[(option_index_of_export + 1)]
                    export_multiplication_table(int(setting_value_of_display_to), int(setting_value_of_display_row_to), fileName)
                else:
                    print_multiplication_table(int(setting_value_of_display_to), int(setting_value_of_display_row_to))
            else:
                print("\n 指令錯誤! --displayRowTo 設定值應為正整數。\n")
        else:
            print("\n 指令錯誤! --displayTo 設定值應為正整數。\n")
    else:
        print("\n 指令錯誤! 請參考help提供的指令清單更改。\n")

def display_command_option():
    help_content = ""
    with open("command_options.txt", encoding='UTF-8') as command_options:
        help_content = command_options.read()
    print(help_content)