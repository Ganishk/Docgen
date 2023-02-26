#!/usr/bin/env python3

import sys
import sphinx
from glob import glob #or os.walk




def main():
    project_dir = sys.argv[1] if len(sys.argv)>1 else "."
    print(project_dir)
    for name in glob(project_dir+"/**/",recursive=True): print(name)






if __name__=="__main__":
    main()
