<script lang="ts">
  import { onMount } from 'svelte';
  let inputText: string = '';
  let items: string[] = [];

  const placeholder = 'Option 1\nOption 2\n...'

  const addItem = () => {
    const newItems = inputText.split('\n').filter(line => line.trim() !== '');
    if (newItems.length > 0) {
      // Add new items to the list without exceeding the 20 items limit
      items = [...items, ...newItems].slice(0, 20);
      inputText = ''; // Clear the input field
    }
  };

  // Handle the Enter key to add the item
  const handleKeydown = (event: KeyboardEvent) => {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      addItem();
    }
  };

  onMount(() => {
    window.addEventListener('keydown', handleKeydown);

    return () => {
      window.removeEventListener('keydown', handleKeydown);
    };
  });
</script>

<style>
  .container {
    width: 100%;
    overflow: scroll;
    display: flex;
    align-items: flex-top;
  }
  .inner-container {
    display: flex;
    padding: 16px;
    flex-direction: column;
    align-items: center;
    width: 50%;
    height: 100%;
    gap: 8px;
  }

  textarea {
    line-height: 1.5;
    width: 100%;
    font-size: 1rem;
  }

  button {
    cursor: pointer;
    width: 50%;
    height: 3em;
  }

  .hidden {
    display: none
  }

  .items-list {
    margin-top: 1rem;
  }
</style>

<h1>To start, add items to the decision array:</h1>
<div class="container">
  <div class="inner-container">
    <textarea bind:value={inputText} rows="3" placeholder={placeholder}></textarea>
    <button on:click={addItem} disabled={items.length >= 20 || inputText.trim() === ''}>Add</button>
    {#if items.length >= 20}
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
      <button class:hidden={items.length < 2}>
        Start Race
      </button>
  </div>
</div>

