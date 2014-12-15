%rebase('main.tpl',
	title=page_title,
	platforms=platforms)

<h2>{{game.platform}}</h2>
<nav>
	<ul>
	% for item in games :
	<li><a href="{{item.id}}" title="Show the game '{{item.title}}'">{{item.title}}</a></li>
	% end
	</ul>
</nav>
<article class="game">
	<div class="header">
		<div class="note">{{game.rate}}</div>

		<img class="cover" src="{{game.cover.medium}}" title="{{game.platform}}/{{game.title}}"/>

		<h1 class="title"> ({{game.platform}}) {{game.title}}</h1>

		<p class="rates">
			<em>rated</em> <code>{{game.rated}}</code> 
			<em>gfx</em> <code>[{{game.rates.gfx}}]</code>
			<em>sound</em> <code>[{{game.rates.sound}}]</code>
			<em>music</em> <code>[{{game.rates.music}}]</code>
			<em>feeling</em> <code>[{{game.rates.feeling}}]</code>
		</p>

		<div class="header">{{game.header.en}}</div>

		<p class="platforms">
			% for pf in game.platforms :
				% if pf == game.platform :
					<em>{{pf}}</em>.
				% else :
					{{pf}}.
				% end
			% end
		</p>

		<p class="author"> *#{{game.id}}*:{{game.createdAt}}:{{game.author}}</p>
	</div>

	<div class="body">
		{{game.content.en}}
	</div>

	<hr />

	<div class="swing">

		<div class="pad plus">
			<h2>+</h2>
			<ul>
				% for item in game.plus :
				<li>{{item}}</li>
				% end
			</ul>
		</div>

		<div class="pad minus">
			<h2>-</h2>
			<ul>
				% for item in game.minus :
				<li>{{item}}</li>
				% end
			</ul>
		</div>
	</div>
	<div class="clear"></div>
</article>	
