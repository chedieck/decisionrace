<script lang="ts">
  import { onMount } from 'svelte';
  import Race from './Race.svelte'
  import { browser } from '$app/environment';
  let inputText: string = '';
  let items: string[] = [];

  let addDisabled = false
  let tooManyItems = false
  let tooManyChars = false

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

    return () => {
      window.removeEventListener('keydown', handleKeydown);
    };
  });

  $: tooManyItems = items.length >= MAX_ITEMS
  $: tooManyItemsInInput = inputText.split(/\n+/).length > (MAX_ITEMS - items.length)
  $: tooManyCharsInInput = inputText.length > MAX_INPUT_CHARS
  $: addDisabled = tooManyItems || tooManyItemsInInput || tooManyCharsInInput

</script>

<style>
  .container {
    width: 100%;
    overflow: hidden;
    display: flex;
    align-items: flex-top;
    max-width: 100vh;
    justify-content: space-around;
  }

  .container:nth-child(odd) {
  }

  .container:nth-child(odd) {
    background-color: var(--color-bg-2);
  }

  .inner-container {
    display: flex;
    padding: 24px;
    flex-direction: column;
    align-items: center;
    width: 40%;
    min-width: 40%;
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
    height: 7em;
    width: 100%;
    font-size: 20px;
    margin-bottom: 10vh;
    margin: 2em;
    border-radius: 0;
  }

  .start-race {
    width: 50%;
  }

  .hidden {
    visibility: hidden;
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

</style>

{#if !raceStarted}
<div class="top-section">
<h1>To start, add items to the decision array:</h1>
<div class="container">

  <div class="inner-container">
    <textarea on:input={handleInput} disabled={!browser || (addDisabled && inputText === '')} bind:value={inputText} rows="3" placeholder={placeholder}></textarea>
    <button on:click={addItem} disabled={addDisabled}>Add</button>
    {#if tooManyItems || tooManyItemsInInput }
      <p class="error">You cannot add more than 20 items.</p>
    {/if}
  </div>
  <div class="inner-container" class:hidden={items.length < 1}>
      <h3>Available Options</h3>
      <ul class="items-list">
        {#each items as item, index (index)}
          <li>{item}</li>
        {/each}
      </ul>
      <div class="row remove-button-container">
        <button class="remove-button" on:click={removeLast}>Remove last item</button>
        <div style:visibility='hidden'>0</div>
        <button class="remove-button" on:click={resetList}>Reset list</button>
      </div>
  </div>
</div>
</div>
<button on:click={() => raceStarted = true} class="start-race" class:hidden={items.length < 2}>
  Start Race
</button>
{/if}
{#if raceStarted}
  <Race optionNames={items} bind:raceStarted/>
{/if}
