# Creating backup file
import os
import time

source = 'C:\\Users\Hp\Desktop\Works\Python' #Fail to excute this line of code.

target_dir = 'C:\\User\Hp\Desktop\Works\Backup'

target = target_dir + os.sep + \
    time.strftime('%Y%M%D%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)


zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

#Run backup
print('Zip command is:')
print(zip_command)
print('Running...')
if os.system(zip_command) == 0:
    print('Successfuly backup to ',target)

else:
    print('BACKUP FAILED!')