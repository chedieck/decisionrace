<script>
	import { page } from '$app/stores';
	import logo from '$lib/images/svelte-logo.svg';
	import github from '$lib/images/github.svg';
</script>

<header>
	<div class="corner">
	</div>

	<nav>
	</nav>

	<div class="corner">
		<a href="https://chedieck.com">chedieck.com</a>
		<a href="https://github.com/chedieck/">
			<img src={github} alt="GitHub" />
		</a>
	</div>
</header>

<style>
	header {
		height: 3vh;
		display: flex;
		justify-content: space-between;
	}

	.corner {
		width: 18em;
		height: 3em;
		display: flex;
	}

	.corner a {
		width: 100%;
	}

	.corner img {
		width: 2em;
		height: 2em;
		object-fit: contain;
	}

	nav {
		display: flex;
		justify-content: center;
		--background: rgba(255, 255, 255, 0.7);
	}

	a {
		display: flex;
		height: 100%;
		align-items: center;
		padding: 0 0.5rem;
		color: var(--color-text);
		font-weight: 700;
		font-size: 0.8rem;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		text-decoration: none;
		transition: color 0.2s linear;
	}

	a:hover {
		color: var(--color-theme-1);
	}
</style>
