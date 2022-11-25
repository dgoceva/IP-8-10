import requests
from plotly import offline

FNAME = 'python_repos.html'
URL = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

header = {'Accept': 'application/vnd.github+json'}
r = requests.get(URL, headers=header)
print(f'Status:{r.status_code}')
req_data = r.json()

names, stars, labels, links = [], [], [], []
for element in req_data['items']:
    names.append(element['name'])
    stars.append(element['stargazers_count'])
    owner = element['owner']['login']
    description = element['description']
    labels.append(f'{owner}<br />{description}')
    name = element['name']
    url = element['html_url']
    link = f'<a href="{url}">{name}</a>'
    links.append(link)

data = [{
    'type': 'bar',
    # 'x': names,
    'x': links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(50,100,150)',
        'line': {'width': 2.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.3,
}]

layout = {
    'title': 'Most Ranking GitHub Python Projects',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 18},
        'tickfont': {'size': 16},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 18},
        'tickfont': {'size': 16},
    }

}

fig = {'data': data, 'layout': layout}

offline.plot(fig, filename=FNAME)
