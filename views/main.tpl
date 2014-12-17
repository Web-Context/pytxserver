<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8' />
<title>{{page_title}}</title>
<link rel="stylesheet" type="text/css" href="/public/css/github.css" />
<link rel="stylesheet" type="text/css" href="/public/css/doc.css" />
<link rel="stylesheet" type="text/css" href="/public/css/games.css" />
</head>
<body>
	<header class="background">
		<p class="version">PyServer V{{version}}</p>
		<h1>The Game</h1>
		<h2>{{page_title}}</h2>
		<nav>
			<ul><li class="right"><input type="search" name="search" id="search" cols="20" value="" placeholder="search game..."/></li></ul>
			<ul>
				<li><a href="/">Home</a></li>
				<li><a href="/games/">games</a></li>
			</ul>			
		</nav>
	</header>
	<aside class="menu">
		<h2>Game Platforms</h2>
		<ul>
			%for platformitem in platforms:
			<li><a 
				%if platform and platform['code'] == platformitem['code'] :
			 	class="active" 
				%end 
				href="/games/{{platformitem['code']}}">{{platformitem['name']}}</a></li>
			%end
		</ul>
		%if games : 
		<h2>Games</h2>
		%end
		<ul>
		% for gameitem in games : 
		  <li><a 
			%if game and game['id'] == gameitem['id'] :
			 	class="active" 
			%end 
		  	href="{{gameitem['id']}}" title="Show the game '{{gameitem['title']}}'">{{gameitem['title']}}</a></li>
		% end
		</ul>
	</aside>
	<div class="container">
		<div id="markup">
			<article id="content" class="markdown-body">{{!base}}</article>
		</div>
	</div>
	<footer>
		<p>
			&copy; <a href="http://mcgivrer.wordpress.com/">McGivrer</a> 2014 - <a
				href="mailto:frederic.delorme@gmail.com&subject=PyTXServer"
				title="Send a mail to author">contact</a>
		</p>
	</footer>
</body>
</html>
