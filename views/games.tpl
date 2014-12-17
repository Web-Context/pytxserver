%rebase('main.tpl',	title=page_title, platforms=platforms, platform=platform, games = games)
<section class="games">
<img class="icon-platform" src="{{platform['pictures'][1]}}"/>
<h2>{{platform['code']}} / {{platform['name']}}</h2>
% for game in games :
<article class="game">
	<div class="header">
		<div class="note">{{game['rate']}}</div>
		<img class="cover" src="{{game['cover'][0]}}" title="{{game['platform']}}/{{game['title']}}"/>
		<h1 class="title"><a href="/game/{{game['id']}}">{{game['title']}}</a></h1>
		<div class="header">{{game['header'][language]}}</div>
			<ul class="platforms">
			% for pf in game['platforms'] :
			<li>{{pf}}</li>
			% end
			</ul>
	</div>
</article>	
% end
<div class="clear"></div>
</section>