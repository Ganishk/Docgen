#!/usr/bin/env python3

import sys
import sphinx #to generate html from documentation
import re #regex to easily detect required format of string
import os
from glob import iglob as glob #or os.walk
#imported iglob for iterator



def main():
    project_dir = sys.argv[1] if len(sys.argv)>1 else "." #only 1 directory is allowed at a time
    print(f"""{project_dir}""".center(os.get_terminal_size()[0],"="))

    with open(".docignore") as file: ignoring = file.read().split()

    for name in glob(project_dir+"/**",recursive=True):
        for ignore in ignoring:
            if name.endswith(ignore): print("[!!!]",end=" ")
        print(name)






if __name__=="__main__":
    main()
