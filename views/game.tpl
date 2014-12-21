% rebase('main.tpl', title=page_title, platforms=platforms, platform=platform, games = games)
<article class="game">
	<div class="header">
		<div class="note">{{game['rate']}}</div>
		<img class="cover" src="{{game['cover'][3]}}" title="{{game['platform']}}/{{game['title']}}"/>
		<h1 class="title"> ({{game['platform']}}) {{game['title']}}</h1>
		<ul class="rates">
<li><em>rated</em><code>{{game['rated']}}</code></li>
<li><em>gfx</em><code>[{{game['rates'][0]}}]</code></li>
<li><em>sound</em><code>[{{game['rates'][1]}}]</code></li>
<li><em>music</em><code>[{{game['rates'][2]}}]</code></li>
<li><em>feeling</em><code>[{{game['rates'][3]}}]</code></li>
		</ul>
		<div class="txt-header">{{!game['header'][language]}}</div>
		<p class="platforms">
			% for pf in game['platforms'] :
			% if pf == game['platform'] :
			<strong>{{pf}}</strong>.
			% else :
			{{pf}}.
			% end
			% end
		</p>
		<p class="author"> <strong>#{{game['id']}}</strong>:{{game['createdAt']}}:{{game['author']}}</p>
	</div>
	<div class="body">
		{{!game['content'][language]}}
	</div>
	<hr />
	<div class="swing">
		<div class="pad plus">
			<h2>+</h2>
			<ul>
				% for item in game['plus'] :
				<li>{{!item}}</li>
				% end
			</ul>
		</div>
		<div class="pad minus">
			<h2>-</h2>
			<ul>
				% for item in game['minus'] :
				<li>{{!item}}</li>
				% end
			</ul>
		</div>
	</div>
	<div class="clear"></div>
</article>	
