#!/bin/bash

# This script is used to automatically modify the python intepreter path configuration on the target system after files have been transferred using the SCP protocol.
# Specifically, it updates the ENS-related path settings to ensure they match the new file locations.
# before running, chmod +x ./this script


correct_interpreter="new_python_intepreter_path_under_a_ens"
old_interpreter="old_python_intepreter_path_under_a_ens"

# loop every packages 
for file in /home/user_name/anaconda3/envs/your_ens_name/bin/*; do
    if head -1 "$file" | grep -q $old_interpreter; then
        # head -1 "$file":`head` is typically used to display the first few lines of a file
        # |: The pipe symbol, which takes the output of the preceding command and passes it as input to the next command.
        # grep -q $old_interpreter: This command uses `grep` to search the output of the previous command (the first line of the file) for the string `$old_interpreter`. The `-q` option specifies quiet mode, meaning `grep` will not output anything.
        sed -i "1s|.*|#!$correct_interpreter|" "$file"
        # -i: This option tells `sed` to edit the file in place, meaning the changes are made directly to the original file.
        # 1: Specifies that the substitution should only occur on the first line of the file.
        # s|.*|: This part of the command means "substitute" (s) everything (.) on the line (*) with:
        # #!$correct_interpreter: The new shebang line that starts with "#!" followed by the path to the correct interpreter, which is stored in the variable "$correct_interpreter".
        # "$file": The name of the file to be modified.
        echo "Modified.: $file"
    fi
done
