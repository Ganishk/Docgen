#!/usr/bin/env python3

import sys
import sphinx
from glob import iglob as glob #or os.walk
#imported iglob for iterator



def main():
    project_dir = sys.argv[1] if len(sys.argv)>1 else "." #only 1 directory is allowed at a time
    print(f"""
================={project_dir}=============="
""")
    for name in glob(project_dir+"/**",recursive=True): print(name)






if __name__=="__main__":
    main()
