<script lang="ts">
  import { onMount } from 'svelte';
  import Race from './Race.svelte'
  import RaceConfig from './RaceConfig.svelte'
  import { browser } from '$app/environment';
	import type { RaceConfigType } from '$lib/types';
  import bigLogo  from '$lib/images/big-logo.png';

  let inputText: string = '';
  let items: string[] = [];

  let raceConfig: RaceConfigType

  let addDisabled = false
  let tooManyItems = false
  let loading = true

  export let raceStarted: boolean

  const placeholder = 'Option 1\nOption 2\n...'
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

  let first10Items = []
  let last10Items = []

  $: tooManyItems = items.length >= MAX_ITEMS
  $: tooManyItemsInInput = inputText.split(/\n+/).length > (MAX_ITEMS - items.length)
  $: tooManyCharsInInput = inputText.length > MAX_INPUT_CHARS
  $: addDisabled = tooManyItems || tooManyItemsInInput || tooManyCharsInInput || loading
  $: first10Items = items.slice(0, 10)
  $: last10Items = items.slice(10, 20)

</script>

<style>
  .container {
    width: 100%;
    overflow: hidden;
    display: flex;
    align-items: flex-top;
    max-width: 80vw;
    height: 60vh;
    justify-content: space-around;
  }

  .container:nth-child(odd) {
    background-color: var(--color-bg-2);
  }

  .inner-container {
    display: flex;
    padding: 24px;
    flex-direction: column;
    align-items: center;
    width: 25%;
    height: 100%;
    background-color: var(--color-bg-2);
  }

  textarea {
    line-height: 1.5;
    width: 100%;
    font-size: 1rem;
  }

  button {
    cursor: pointer;
    height: 3em;
    width: 100%;
    font-size: 20px;
    margin-bottom: 10vh;
    margin: 2em;
    border-radius: 0;
  }

  .start-race {
    width: 50%;
    margin-top: 0.5em;
  }

  .items-list {
    margin-top: 1rem;
  }

  .remove-button-container {
    width: 100%;
  }

  .remove-button {
    height: 3em;
    font-size: 14px;
    width: 50%;
    margin: 0px;
  }

  @media (max-width: 768px) {
    .container {
      width: 100vw;
      max-width: 100vw;
      justify-content: start;
      height: 60vh;
    }

    button {
      height: 2em;
      width: 100%;
      margin: 0;
    }

    .inner-container {
      display: flex;
      padding: 0;
      padding-top: 4px;
      flex-direction: column;
      align-items: center;
      width: 100%;
      height: min-content;
      background-color: var(--color-bg-2);
    }

    li {
      width: 100%;
    }

    .options {
      height: max-content;
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
      width: 50%;
    }

    .items-list.full-width {
      width: 100%;
    }
  }
</style>

{#if !raceStarted}
  <div class="row center">
    <img src={bigLogo} alt='Logo'>
    <h1>DecisionRace</h1>
  </div>
<h2>To start, add choice options to the text area below:</h2>
<div class="container mobile-undo-row">

  <div class="inner-container">
    <RaceConfig bind:raceConfig/>
  </div>
  <div class="inner-container">
    <textarea on:input={handleInput} disabled={!browser || (addDisabled && inputText === '')} bind:value={inputText} rows="3" placeholder={placeholder}></textarea>
    <button on:click={addItem} disabled={addDisabled}>Add</button>
    <div class="row remove-button-container not-on-media" class:hidden={items.length < 1}>
      <button class="remove-button" on:click={removeLast}>Remove last item</button>
      <div style:visibility='hidden'>0</div>
      <button class="remove-button" on:click={resetList}>Reset list</button>
    </div>
    {#if tooManyItems || tooManyItemsInInput }
      <p class="error not-on-media">You cannot add more than 20 items.</p>
    {/if}
  </div>
  <div class="inner-container options" class:hidden={items.length < 1}>
    <div class="row justify-between full-width">
      <button class="remove-button only-on-media" on:click={removeLast}>Remove last item</button>
      <h3>Available Options</h3>
      <button class="remove-button only-on-media" on:click={resetList}>Reset list</button>
    </div>
    <div class="row full-width">
      <ol class="items-list not-on-media">
        {#each items as item, index (index)}
          <li>{item}</li>
        {/each}
      </ol>
      <ol class="items-list only-on-media" class:full-width={items.length < 11}>
        {#each first10Items as item, index (index)}
          <li>{item}</li>
        {/each}
      </ol>
      <ol class="items-list only-on-media" class:undisplayable={items.length < 11}>
        {#each last10Items as item, index (index)}
          <li>{item}</li>
        {/each}
      </ol>
    </div>
  </div>
</div>
<button on:click={() => raceStarted = true} class="start-race" class:hidden={items.length < 2}>
  Start Race
</button>
{#if tooManyItems || tooManyItemsInInput }
  <p class="error only-on-media">You cannot add more than 20 items.</p>
{/if}
{/if}
{#if raceStarted}
  <Race optionNames={items} bind:raceStarted bind:raceConfig/>
{/if}
