<script>
	import { page } from '$app/stores';
  import logo from '$lib/images/svelte-logo.svg';
  import github from '$lib/images/github.svg';
</script>

<div class="footer">

    <div class="occupy-space corner">
      <a href="https://github.com/chedieck/choicerace">
        &lt;/&gt;
      </a>
    </div>
    <div class="center">
      <a href="https://chedieck.com">chedieck.com</a>
    </div>
    <div class="corner">
      <a href="https://github.com/chedieck/choicerace">
        &lt;/&gt;
      </a>
    </div>

</div>

<style>
	.footer {
		height: 3vh;
		display: flex;
    flex-direction: row;
		justify-content: space-between;
		align-items: center;
    padding-top: 3px;
    padding-bottom: 3px;
    background-color: var(--color-bg-3);
	}

	.center {
		height: 100%;
		display: flex;
	}
  .corner {
		height: 100%;
		display: flex;
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

  .occupy-space {
    visibility: hidden;
	}

	a:hover {
		color: var(--color-link-text);
	}
</style>
