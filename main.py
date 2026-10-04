from pick import pick
import sys, os

# Function to search for a game account by phrases
def search_account():
    print('Searching for a game account...')
    founds = 0
    phrase = input('Enter game title: ').lower()
    
    while True:
        with open('accounts.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if not line.strip():  # Skip empty lines
                    continue

                try:
                    account_data = line.strip().split(',')
                    if len(account_data) >= 4:
                        current_title = account_data[0].strip().lower()

                    if phrase in current_title:
                        game_title = account_data[0].capitalize()
                        platform = account_data[1].strip().capitalize()
                        login = account_data[2]
                        password = account_data[3]
                        print(f'''
Game Title: {game_title} 
Platform: {platform} 
Login: {login} 
Password: {password}
''')
                        founds += 1
                except Exception as e:
                    print(f'Error parsing account information: {e}')

            if founds == 0:
                print('No accounts found for the given game title.')
            else:
                print(f'Found {founds} accounts for the given game title.')
        break

# Function to add a new game account
def add_account():
    print('Adding a new game account...')
    account_data = []

    account_data.append(input('Game title: ').strip())
    account_data.append(input('Platform: ').strip())
    account_data.append(input('Login: ').strip())
    account_data.append(input('Password: ').strip())


    with open('accounts.txt', 'a', encoding='utf-8') as file:
        try:
            file.write('\n' + ', '.join(account_data))
        except Exception as e:
            print(f'Error writing to file: {e}')

    print('Game account added successfully.')

# Function to delete a game account
def delete_account():
    print('Deleting a game account...')
    game_title = input('Enter the game title of the account to delete: ').strip().lower()

    try:
        with open('accounts.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('The accounts file does not exist.')
        return

    new_lines = []
    deleted = False

    for line in lines:
        if not line.strip():
            new_lines.append(line)
            continue  # Skip empty lines

        current_game_title = line.split(',')[0].strip().lower()

        if current_game_title != game_title:
            new_lines.append(line)
        else:
            deleted = True

    if deleted:
        with open('accounts.txt', 'w', encoding='utf-8') as file:
            try:
                file.writelines(new_lines)
                print(f'Game account for "{game_title}" deleted successfully.')
            except Exception as e:
                print(f'Error writing to file: {e}')
    else:
        print(f'No game account found for "{game_title}".')

def show_all_accounts():
    print('Showing all game accounts...')
    with open('accounts.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():  # Skip empty lines
                try:
                    account_data = line.strip().split(',')
                    game_title = account_data[0].capitalize()
                    platform = account_data[1].strip().capitalize()
                    login = account_data[2]
                    password = account_data[3]
                    print(f'''
Game Title: {game_title}
Platform: {platform}
Login: {login}
Password: {password}
                    ''')
                except Exception as e:
                    print(f'Error parsing account information: {e}')

def menu():
    title = '''
    ===============================
    | Games Accounts Manager v1.0 |
    ===============================
    '''
    options = ['Search game account', 'Add game account', 'Delete game account', 'Show all game accounts', 'Exit']
    
    while True:
        option, index = pick(options, title, indicator='=>', default_index=0)

        match index:
            case 0:
                search_account()
            case 1:
                add_account()
            case 2:
                delete_account()
            case 3:
                show_all_accounts()
            case 4:
                print('Exiting the program...')
                sys.exit()

        input('Press Enter to return to the menu...')
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    menu()