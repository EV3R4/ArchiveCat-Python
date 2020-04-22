#import io
from datetime import datetime
import http.client as http
import json
import os
from subprocess import run

if not os.path.isdir('projects'):
    os.mkdir('projects')

if os.path.isfile('config.json'):
    with open('config.json', 'r') as f:
        config = json.loads(f.read())
else:
    print('No config.json found!')

last_update = datetime.min
if os.path.isfile('lastupdate.txt'):
    with open('lastupdate.txt', 'r') as f:
        last_update = datetime.fromisoformat(f.read())

headers = {
    'User-Agent': 'ArchiveCat-Python'
}
conn = http.HTTPSConnection('api.github.com')

def update(url):
    conn.request('GET', url, None, headers)
    res = conn.getresponse()
    if res.status != 200:
        print(res.status + ': ' + res.msg)
        return
    body = json.loads(res.read())
    for repo in body:
        if repo['full_name'] in config['github']['ignore']:
            print('Ignoring ' + repo['full_name'] + '!')
            continue
        project_directory = 'projects/' + repo['full_name']
        if os.path.isdir(project_directory):
            if datetime.strptime(repo['updated_at'], '%Y-%m-%dT%H:%M:%SZ') < last_update:
                print(repo['full_name'] + ' is already up to date!')
                continue
            print('Pulling ' + repo['full_name'] + '...')
            run('git pull ' + repo['clone_url'] + ' ' + repo['default_branch'], cwd=project_directory)
            print('Finished!')
        else:
            print('Cloning ' + repo['full_name'] + '...')
            os.makedirs(project_directory)
            run('git clone ' + repo['clone_url'], cwd='projects/' + repo['owner']['login'])
            print('Finished!')
    if res.getheader('link') and 'next' in res.getheader('link'):
        link = res.getheader('link').split(';')[0]
        update(link.substring(1, link.length - 1))


print('Updating...')
update('/users/' + config['github']['username'] + '/starred?per_page=100')
with open('lastupdate.txt', 'w') as f:
    f.write(datetime.now().isoformat())
