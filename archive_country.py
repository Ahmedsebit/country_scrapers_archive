import subprocess
import os


gazette_repository_name =  os.getenv('GAZETTE_REPOSITORY_NAME')
gazette_repository_url= os.getenv('GAZETTE_REPOSITORY_URL')
gazette_repository_branch = os.getenv('GAZETTE_REPOSITORY_BRANCH')
country_repository_name = os.getenv('COUNTRY_REPOSITORY_NAME')
country_repository_url = os.getenv('COUNTRY_REPOSITORY_URL')
country_repository_branch = os.getenv('COUNTRY_REPOSITORY_BRANCH')
country_name = os.getenv('COUNTRY')


def archive_country(gazette_repo_url, gazette_repo_name, gazette_repo_branch, git_repo_url, git_repo_name, git_repo_branch, country):
    '''
    Function for archiving a country repo
    '''
    #Cloning the two repo
    subprocess.call(['rm', '-rf', gazette_repo_name])
    subprocess.call(['rm', '-rf', git_repo_name])
    subprocess.call(['git', 'clone', gazette_repo_url])
    subprocess.call(['git', 'clone', git_repo_url])

    #Creating the country repo archive
    os.chdir(git_repo_name)
    country_archive = '.' + country + ".git"
    subprocess.call(['git', 'checkout', git_repo_branch])
    subprocess.call(['git', 'bundle', 'create', country_archive, 'HEAD'])

    #Pushing the archived country to gazette repo
    os.chdir('../'+gazette_repository_name)
    subprocess.call(['git', 'checkout', gazette_repo_branch])
    subprocess.call(['cp', '../'+git_repo_name+'/'+country_archive, '.'])
    subprocess.call(['git', 'add', country_archive])
    commit_message = 'ARCHIVE '+country_archive
    subprocess.call(['git', 'commit', '-m', commit_message])
    subprocess.call(['git', 'push', '-u', 'origin', gazette_repository_branch])

    #Deleting the cloned folders
    os.chdir('..')
    subprocess.call(['rm', '-rf', git_repo_name])
    subprocess.call(['rm', '-rf', gazette_repo_name])

def main():
    archive_country(
        gazette_repository_url, gazette_repository_name, gazette_repository_branch,
        country_repository_url, country_repository_name, gazette_repository_branch, country_name
    )


if __name__ == '__main__':
    main()
