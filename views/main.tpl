<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'/>
    <title>{{page_title}}</title>
    <link rel="stylesheet" type="text/css" href="/public/css/github.css" />
    <link rel="stylesheet" type="text/css" href="/public/css/doc.css"/>
    <link rel="stylesheet" type="text/css" href="/public/css/games.css"/>
  </head>
  <body>
  	<header class="background">
      <p class="version">PyServer v1.0</p>
  		<h1>The Game</h1>
  		<h2>{{page_title}}</h2>
      <nav>
        <ul>
          <li><a href="/">Home</a></li>
        </ul>
      </nav>
  	</header>
    <aside class="menu">
      <ul>
      	%for item in platforms:
        <li><a href="/games/{{item.code}}">{{item.name}}</a></li>
        %end
      </ul>
    </aside>
    <div class="container">
      <div id="markup">
        <article id="content" class="markdown-body">
          {{!base}}
        </article>
      </div>
    </div>
    <footer><p>&copy; <a href="http://mcgivrer.wordpress.com/">McGivrer</a> 2013 - <a href="mailto:frederic.delorme@gmail.com&subject=Game 2D tutorial" title="Send a mail to author">contact</a></p></footer>
  </body>
</html>