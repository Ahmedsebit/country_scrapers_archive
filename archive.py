import subprocess
import os


gazette_repository_name =  'archive'#os.getenv('GAZETTE_REPOSITORY_NAME')
gazette_repository_url= 'https://github.com/Ahmedsebit/archive.git' #os.getenv('GAZETTE_REPOSITORY_URL')
gazette_repository_branch = 'master'#os.getenv('GAZETTE_REPOSITORY_BRANCH')
country_repository_name = 'country_scrapers_archive'#os.getenv('COUNTRY_REPOSITORY_NAME')
country_repository_url = 'https://github.com/Ahmedsebit/country_scrapers_archive.git'#os.getenv('COUNTRY_REPOSITORY_URL')
country_repository_branch = 'deploy'#os.getenv('COUNTRY_REPOSITORY_BRANCH')


def archive_country(gazette_repo_url, gazette_repo_name, git_repo_url, git_repo_name, country):
    '''
    Function for archiving a country repo
    '''
    #Cloning the two repo
    subprocess.call(['git', 'clone', gazette_repo_url])
    subprocess.call(['git', 'clone', git_repo_url])
    subprocess.check_call(["ls", "-l"])
    print('Repositories have been cloned\n')

    #Creating the country repo archive
    os.chdir(git_repo_name)
    country_archive = '.' + country + ".git"
    subprocess.call(['git', 'clone', git_repo_url])
    subprocess.call(['git', 'bundle', 'create', country_archive, 'HEAD'])
    subprocess.call(['cp', country_archive, '../'+gazette_repo_name+'/archive/'])
    print('The country repo has been archived\n')

    #Pushing the archived country to gazette repo
    os.chdir('../'+gazette_repository_name)
    country_archive_forpush = '/archive/'+country_archive
    subprocess.call(['git', 'add', country_archive_forpush])
    commit_message = 'ARCHIVE '+country_archive
    subprocess.call(['git', 'commit', '-m', commit_message])
    subprocess.call(['git', 'push', '-u', 'origin', gazette_repository_branch])
    print('The country has been pushed to gazette repo\n')


def main():
    print('Starting the process\n')
    archive_country(
        gazette_repository_url, gazette_repository_name,
        country_repository_name, country_repository_url,
        gazette_repository_branch
    )


if __name__ == '__main__':
    main()
