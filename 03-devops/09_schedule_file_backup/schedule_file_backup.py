import shutil
import schedule
import time

def backup_files():
    source_dir = 'source'
    destination_dir = 'backup'
    
    try:
        shutil.copytree(source_dir, destination_dir)
        print('Backup completed successfully.')
    except Exception as e:
        print(f'An error occurred during backup: {str(e)}')

# Schedule the backup task to run every day at a specific time (e.g., 2:00 PM)
schedule.every().day.at('14:00').do(backup_files)

while True:
    schedule.run_pending()
    time.sleep(1)
