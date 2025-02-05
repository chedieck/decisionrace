<script lang="ts">
  import { onMount } from 'svelte';
  import Race from './Race.svelte'
  import RaceConfig from './RaceConfig.svelte'
  import { browser } from '$app/environment';
	import type { RaceConfigType } from '$lib/types';
  import bigLogo  from '$lib/images/big-logo.png';
  import halfLogo  from '$lib/images/half-logo.png';

  let inputText: string = '';
  let items: string[] = [];
  let raceConfig: RaceConfigType = { raceStarted: false, votesToWin: 10, autoStep: 0 }


  let addDisabled = false
  let tooManyItems = false
  let loading = true

  const placeholder = 'Add candidates here...'
  const MAX_ITEMS = 20
  const MAX_INPUT_CHARS = 1000

  const addItem = () => {
    if (addDisabled) return
    const newItems = inputText.split('\n').filter(line => line.trim() !== '');
    if (newItems.length > 0) {
      // Add new items to the list without exceeding the 20 items limit
      items = [...items, ...newItems].slice(0, 20);
      inputText = ''; // Clear the input field
    }
  };
  const resetList = () => {
    items = []
  }

  const removeLast = () => {
    if (items.length < 1) {
      return
    }
    items = items.slice(0, items.length -1)
  }
  // Handle the Enter key to add the item
  const handleKeydown = (event: KeyboardEvent) => {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      addItem();
    } else if (event.key === 'Enter' && tooManyItemsInInput) {
      event.preventDefault(); // Prevent adding more lines if limit is reached
    }
  };

    // Handle input to prevent pasting too many lines or characters
  const handleInput = () => {
    const lines = inputText.split('\n');
    if (lines.length > MAX_ITEMS - items.length || inputText.length > MAX_INPUT_CHARS) {
      inputText = lines.slice(0, MAX_ITEMS - items.length).join('\n').substring(0, MAX_INPUT_CHARS);
    }
  };

  onMount(() => {
    window.addEventListener('keydown', handleKeydown);
    loading = false
    return () => {
      window.removeEventListener('keydown', handleKeydown);
    };
  });

  let first10Items: string[] = []
  let last10Items: string[] = []

  $: tooManyItems = items.length >= MAX_ITEMS
  $: tooManyItemsInInput = inputText.split(/\n+/).length > (MAX_ITEMS - items.length)
  $: tooManyCharsInInput = inputText.length > MAX_INPUT_CHARS
  $: addDisabled = tooManyItems || tooManyItemsInInput || tooManyCharsInInput || loading
  $: first10Items = items.slice(0, 10)
  $: last10Items = items.slice(10, 20)
  $: raceConfig  = raceConfig

</script>

<style>
  .container {
    width: 100%;
    overflow: hidden;
    display: flex;
    align-items: flex-top;
    height: 60vh;
    background-color: var(--color-bg-2);
  }


  .inner-container {
    display: flex;
    padding: 24px;
    flex-direction: column;
    align-items: center;
    width: 100%;
    height: 100%;
    height: max-content;
  }

  .smaller-container {
    width: 50%;
  }


  .main-prompt {
    line-height: 3;
    width: 90%;
    margin: 20px;
    font-size: 1rem;
  }

  button {
    cursor: pointer;
    height: 3em;
    font-size: 20px;
    padding: 0.8em;
    margin-bottom: 10vh;
    margin: 2em;
  }

  .start-race {
    margin-top: 0.5em;
  }

  .items-list {
    margin-top: 1rem;
  }

  .remove-button-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    padding-top: 10px;
  }

  .remove-button {
    height: 3em;
    font-size: 14px;
  }

  .logo {
    padding-right: 12px;
    padding-top: 12px;
  }

  @media (max-width: 768px) {
    .container {
      width: 100vw;
      max-width: 100vw;
      justify-content: start;
      height: 65vh;
    }

    .main-prompt {
      line-height: 1;
      width: 100%;
      font-size: 1rem;
    }

    button {
      height: 2em;
      width: 100%;
      margin: 0;
    }

    .inner-container {
      width: 100%;
      height: min-content;
      background-color: var(--color-bg-2);
    }

    .inner-container > div {
      padding-top: 12px;
    }
    li {
      width: 100%;
    }

    .error {
      margin: 0;
    }

    h3 {
      margin: 0;
    }

    button.only-on-media {
      width: 27%;
    }

    .items-list {
      line-height: 1;
      width: 50%;
    }

    .items-list.full-width {
      width: 100%;
    }

    .logo-container {
      max-height: 15vh;
    }
  }
</style>

{#if !raceConfig.raceStarted}
  <h2>Add candidates to the text area below:</h2>
  <input class="main-prompt" on:input={handleInput} disabled={!browser || (addDisabled && inputText === '')} bind:value={inputText} placeholder={placeholder}>
  <div class="row remove-button-container not-on-media" class:hidden={items.length < 1}>
    <button class="remove-button" on:click={removeLast}>Remove last item</button>
    <button on:click={() => raceConfig.raceStarted = true} class="start-race" class:hidden={items.length < 2}>
      Start Race
    </button>
    <button class="remove-button" on:click={resetList}>Reset list</button>
  </div>
  {#if tooManyItems || tooManyItemsInInput }
    <p class="error not-on-media">You cannot add more than 20 items.</p>
  {/if}

  <div class="container mobile-undo-row">
    <div class="inner-container smaller-container">
      <RaceConfig bind:raceConfig bind:items/>
    </div>
    <div class="inner-container" class:hidden={items.length < 1}>
      <div class="row justify-between full-width">
        <h3>Choice Pool</h3>
      </div>
      <div class="row full-width">
        <ol class="items-list not-on-media">
          {#each items as item, index (index)}
            <li>
              {#if raceConfig.linkToRottenTomatoes}
                <a href=https://www.rottentomatoes.com/m/{item.replace(' ', '_').toLowerCase()}>{item}</a>
              {:else}
                <span>{item}</span>
              {/if}
            </li>
          {/each}
        </ol>
        <ol class="items-list only-on-media" class:full-width={items.length < 11}>
          {#each first10Items as item, index (index)}
            <li>
              {#if raceConfig.linkToRottenTomatoes}
                <a href=https://www.rottentomatoes.com/m/{item.replace(' ', '_').toLowerCase()}>{item}</a>
              {:else}
                <span>{item}</span>
              {/if}
            </li>
          {/each}
        </ol>
        <ol class="items-list only-on-media" class:undisplayable={items.length < 11}>
          {#each last10Items as item, index (index)}
            <li>
              {#if raceConfig.linkToRottenTomatoes}
                <a href=https://www.rottentomatoes.com/m/{item.replace(' ', '_').toLowerCase()}>{item}</a>
              {:else}
                <span>{item}</span>
              {/if}
            </li>
          {/each}
        </ol>
      </div>
    </div>
  </div>
  {#if tooManyItems || tooManyItemsInInput }
    <p class="error absolute only-on-media">You cannot add more than 20 items.</p>
  {/if}
{/if}
{#if raceConfig.raceStarted}
  <Race optionNames={items} bind:raceConfig/>
{/if}
