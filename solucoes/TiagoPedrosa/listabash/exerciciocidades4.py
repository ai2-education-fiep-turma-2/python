import shutil
import os
def copyDelete():
    shutil.copy('arq1.txt', '/tmp/arq1.txt')
    shutil.copy('arq2.txt', '/tmp/arq2.txt')

    os.remove('/tmp/arq1.txt')
    os.remove('/tmp/arq2.txt')

    
copyDelete()