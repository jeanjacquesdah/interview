import subprocess
import datetime
import time

# Database details
db_host = 'your_db_host'
db_port = 'your_db_port'
db_name = 'your_db_name'
db_user = 'your_db_user'
db_password = 'your_db_password'

# Backup function
def backup_database():
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_file = f'database_backup_{timestamp}.sql'
    
    # Constructing the mysqldump command
    command = [
        'mysqldump',
        '-h', db_host,
        '-P', db_port,
        '-u', db_user,
        '-p' + db_password,  # Note: No space between -p and password
        db_name,
        '--result-file', backup_file
    ]

    # Running the mysqldump command
    subprocess.run(command, check=True)
    print(f"Backup successful. Backup file: {backup_file}")

# Restore function
def restore_database(backup_file):
    # Constructing the mysql command for restoration
    command = [
        'mysql',
        '-h', db_host,
        '-P', db_port,
        '-u', db_user,
        '-p' + db_password,  # Note: No space between -p and password
        db_name,
        '<', backup_file
    ]

    # Running the mysql command
    subprocess.run(" ".join(command), shell=True, check=True)
    print("Restoration successful.")

# Example usage: Backup every day and restore the latest backup for testing
try:
    while True:
        # Backup the database every 24 hours
        backup_database()

        # Restore the latest backup for testing
        latest_backup = f'database_backup_{datetime.datetime.now().strftime("%Y%m%d")}.sql'
        restore_database(latest_backup)

        # Sleep for 24 hours
        time.sleep(24 * 60 * 60)

except KeyboardInterrupt:
    print("Backup and restore script terminated.")


# In this case mysqldump will be use to create a timestamped backup file and the mysql command to restore the database. 